import requests
import base64
import json
import os

# CONFIGURATION
USERNAME = "Ikarthikmb"
OUTPUT_FILE = "_data/github_raw_data.json"
# Use a Personal Access Token (PAT) for higher rate limits, passed via env var.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_readmes():
    # FIXED: Added Authorization to headers
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} 
    all_readmes = []
    
    # FIXED: Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    print(f">> Initializing scan for user: {USERNAME}...")
    
    repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
    repos_response = requests.get(repos_url, headers=headers)
    
    if repos_response.status_code != 200:
        print(f"!! Error fetching repos: {repos_response.json().get('message')}")
        return

    repos = repos_response.json()
    
    for repo in repos:
        if repo['fork']: continue
        
        repo_name = repo['name']
        print(f"   Scanning {repo_name}...")
        
        tree_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/git/trees/{repo['default_branch']}?recursive=1"
        tree_data = requests.get(tree_url, headers=headers).json()
        
        if 'tree' not in tree_data: continue
        
        readmes = [f for f in tree_data['tree'] if f['path'].lower().endswith('readme.md')]
        
        for file in readmes:
            blob = requests.get(file['url'], headers=headers).json()
            
            # FIXED: Added check to prevent KeyError: 'content'
            if 'content' in blob:
                content = base64.b64decode(blob['content']).decode('utf-8', errors='ignore')
                
                all_readmes.append({
                    "repo": repo_name,
                    "path": file['path'],
                    "content": content,
                    "size": blob.get('size', 0),
                    "url": f"https://github.com/{USERNAME}/{repo_name}/blob/{repo['default_branch']}/{file['path']}"
                })
            else:
                print(f"      [!] Skipping {file['path']} - No content found.")


    # FIXED: Hardened JSON saving for Jekyll compatibility
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # ensure_ascii=True turns non-ascii characters into \u0000 sequences
        # which prevents Jekyll/Ruby from choking on invalid unicode
        json.dump(all_readmes, f, indent=4, ensure_ascii=True)
    
    print(f"\n>> SUCCESS: {len(all_readmes)} READMEs indexed in {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_readmes()

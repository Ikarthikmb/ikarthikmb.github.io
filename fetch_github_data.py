import requests
import base64
import json
import os

# --- CONFIGURATION ---
USERNAME = "Ikarthikmb"
OUTPUT_FILE = "assets/data/github_raw_data.json"
# ⚠️ SECURITY: Use a Personal Access Token (PAT) for higher rate limits.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_readmes():
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    all_readmes = []
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    print(f">> Initializing scan for user: {USERNAME}")
    
    try:
        # 1. Fetch all repositories
        repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
        repos = requests.get(repos_url, headers=headers).json()
        
        for repo in repos:
            if repo['fork']: continue # Skip forks
            
            repo_name = repo['name']
            branch = repo['default_branch']
            print(f"   Scanning {repo_name}...")
            
            # 2. Get recursive tree to find READMEs
            tree_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/git/trees/{branch}?recursive=1"
            tree_data = requests.get(tree_url, headers=headers).json()
            
            if 'tree' not in tree_data: continue

            # Only target README.md files
            readmes = [f for f in tree_data['tree'] if f['path'].lower().endswith('readme.md')]
            
            for file in readmes:
                blob = requests.get(file['url'], headers=headers).json()
                
                # Verify 'content' exists to avoid KeyError
                if 'content' in blob:
                    content = base64.b64decode(blob['content']).decode('utf-8', errors='ignore')
                    
                    all_readmes.append({
                        "repo": repo_name,
                        "branch": branch,
                        "path": file['path'],
                        "content": content,
                        "size": blob.get('size', 0)
                    })

        # 3. Save as Jekyll-safe JSON
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_readmes, f, indent=4, ensure_ascii=True)
        
        print(f"\n>> SUCCESS: Indexed {len(all_readmes)} READMEs to {OUTPUT_FILE}")

    except Exception as e:
        print(f"!! ERROR: {str(e)}")

if __name__ == "__main__":
    fetch_readmes()

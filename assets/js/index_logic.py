import requests
import json
import os

# --- CONFIGURATION ---
USERNAME = "Ikarthikmb"
# Loads token from your shell environment (e.g., export GITHUB_TOKEN=your_pat_here)
TOKEN = os.getenv("GITHUB_TOKEN") 
OUTPUT_FILE = "../../assets/data/logic_index.json"

def index_verilog():
    headers = {}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
        print(">> AUTH: Token detected in environment.")
    else:
        print(">> WARN: No GITHUB_TOKEN found. Proceeding with limited rate (60 req/hr).")
    
    logic_db = []
    print(f">> Initializing RTL scan for: {USERNAME}")
    
    try:
        # 1. Fetch Repositories
        repo_res = requests.get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100", headers=headers)
        repos = repo_res.json()

        if isinstance(repos, dict) and "message" in repos:
            print(f"!! API ERROR: {repos['message']}")
            return

        for repo in repos:
            if repo.get('fork'): continue # Skip forked repos
            
            name = repo['name']
            branch = repo['default_branch']
            print(f"   Scanning {name}...")
            
            # 2. Get the file tree
            tree_url = f"https://api.github.com/repos/{USERNAME}/{name}/git/trees/{branch}?recursive=1"
            tree_res = requests.get(tree_url, headers=headers).json()
            
            if 'tree' not in tree_res: 
                continue

            for file in tree_res['tree']:
                # Filter for Verilog extensions
                if file['path'].lower().endswith(('.v', '.sv', '.vh')):
                    raw_url = f"https://raw.githubusercontent.com/{USERNAME}/{name}/{branch}/{file['path']}"
                    
                    logic_db.append({
                        "module": file['path'].split('/')[-1],
                        "repo": name,
                        "path": file['path'],
                        "raw_url": raw_url,
                        "size": file.get('size', 0)
                    })
                    print(f"      [+] Found: {file['path']}")

        # 3. Save the Index
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(logic_db, f, indent=4)
        
        print(f"\n>> SUCCESS: Indexed {len(logic_db)} modules to {OUTPUT_FILE}")

    except Exception as e:
        print(f"!! CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    index_verilog()

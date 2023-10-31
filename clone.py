import os
import subprocess

repos = ["usuario/repo1", "usuario/repo2"]

for repo in repos:
    repo_dir = repo.split("/")[1]
    if not os.path.exists(repo_dir):
        subprocess.run(["git", "clone", "https://github.com/" + repo])
    else:
        print(f"O diretório {repo_dir} já existe, pulando clone...")

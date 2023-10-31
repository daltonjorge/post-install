import os
import subprocess

asdf_dir = "/home/dalton/.asdf"

if not os.path.exists(asdf_dir):
    subprocess.run(
        [
            "git",
            "clone",
            "https://github.com/asdf-vm/asdf.git",
            asdf_dir,
            "--branch",
            "v0.12.0",
        ]
    )
else:
    print(f"O diretório {asdf_dir} já existe, pulando clone...")

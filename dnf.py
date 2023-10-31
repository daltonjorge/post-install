import os
import subprocess

vscode_repo = """[code]
name=Visual Studio Code
baseurl=https://packages.microsoft.com/yumrepos/vscode
enabled=1
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc
"""

pkgs = [
    "alacritty",
    "neovim",
    "lazygit",
    "bottom",
    "gdu",
    "bat",
    "exa",
    "ripgrep",
    "starship",
    "fish",
    "gcc",
    "make",
    "code",
]

subprocess.run(["sudo", "dnf", "copr", "enable", "atim/starship"])
subprocess.run(["sudo", "dnf", "copr", "enable", "atim/lazygit"])

if not os.path.exists("/etc/yum.repos.d/vscode.repo"):
    subprocess.run(
        ["sudo", "rpm", "--import", "https://packages.microsoft.com/keys/microsoft.asc"]
    )
    subprocess.run(
        [
            "sudo",
            "sh",
            "-c",
            f"echo -e '{vscode_repo}' > /etc/yum.repos.d/vscode.repo",
        ]
    )
    subprocess.run(["dnf", "check-update"])

for pkg in pkgs:
    subprocess.run(["sudo", "dnf", "install", "-y", pkg])

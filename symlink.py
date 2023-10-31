import os

links = [
    # Usar a seguinte estrutura:
    # [<"nome-do-arquivo|*">, <"origem">, <"destino">, <True | False> ],
    ["tmux.conf", "files/tmux", "$HOME/", True],
    ["alacritty.yml", "files/alacritty", "$HOME/.config/alacritty", False],
    ["*", "files/fish", "$HOME/.config/fish", False],
]


def create_symlink(src, dest, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    if os.path.lexists(dest):
        os.unlink(dest)

    os.symlink(src, dest)


def process_link(file_name, src_dir, dest_dir, is_dotfile):
    src = os.path.join(os.getcwd(), f"{src_dir}/{file_name}")

    dest_file_name = f".{file_name}" if is_dotfile else file_name
    dest = os.path.join(dest_dir, dest_file_name)

    create_symlink(src, dest, dest_dir)


for link in links:
    file_name, src_dir, dest_dir, is_dotfile = link

    if file_name == "*":
        for each_file in os.listdir(os.path.join(os.getcwd(), src_dir)):
            process_link(each_file, src_dir, dest_dir, is_dotfile)
    else:
        process_link(file_name, src_dir, dest_dir, is_dotfile)

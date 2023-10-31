import os
import shutil


def install_fonts(src_directory, dest_directory=os.path.expanduser("~/.fonts")):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for filename in os.listdir(src_directory):
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            src_filepath = os.path.join(src_directory, filename)
            dest_filepath = os.path.join(dest_directory, filename)

            shutil.copy2(src_filepath, dest_filepath)

    # Atualize o cache de fontes
    os.system("fc-cache -fv")


if __name__ == "__main__":
    src_directory = "files/fonts"
    install_fonts(src_directory)

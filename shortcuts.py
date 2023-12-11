import subprocess

path = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings"


def dconf_read(key):
    result = subprocess.run(["dconf", "read", key], capture_output=True)
    return result.stdout.decode().strip()  # .decode("utf-8")


def dconf_list(key):
    return subprocess.run(["dconf", "list", key + "/"], capture_output=True)


def dconf_write(key, value):
    subprocess.run(["dconf", "write", key, value])


def register_custom_binding(name, command, binding):
    actual_bindings = dconf_list(path).stdout.decode("utf-8")
    arr = actual_bindings.strip().split("\n") if actual_bindings else []
    found = [x for x in arr if dconf_read(f"{path}/{x}name") == f"'{name}'"]

    if found:
        print(f"Gnome keyboard shortcut already exists for {name}.")
    else:
        arr.append(f"custom{len(arr)}/")
        bindings_updated = [f"{path}/{b}" for b in arr]
        dconf_write(path, f"{bindings_updated}")
        dconf_write(bindings_updated[-1] + "name", f"'{name}'")
        dconf_write(bindings_updated[-1] + "command", f"'{command}'")
        dconf_write(bindings_updated[-1] + "binding", f"'{binding}'")
        print(f"New Gnome keyboard shortcut registered for {name}.")


crow_command = "dbus-send --type=method_call --dest=io.crow_translate.CrowTranslate /io/crow_translate/CrowTranslate/MainWindow io.crow_translate.CrowTranslate.MainWindow.translateSelection"
register_custom_binding("Crow", crow_command, "<Ctrl><Alt>E")

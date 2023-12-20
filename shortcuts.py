import subprocess

DCONF_PATH = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings"


def run_dconf(array):
    """Run dconf binary."""
    return subprocess.run(["dconf"] + array, capture_output=True)


def read_dconf(key):
    """Read a value from the dconf database."""
    return run_dconf(["read", key]).stdout.decode("utf-8").strip()


def list_dconf(key):
    """List all values for a given key in the dconf database."""
    return run_dconf(["list", key + "/"]).stdout.decode("utf-8").strip()


def write_dconf(key, value):
    """Write a value to the dconf database."""
    run_dconf(["write", key, value])


def register_custom_binding(name, command, binding):
    """Register a custom keyboard shortcut for a given command."""
    bindings = list_dconf(DCONF_PATH).split("\n") if list_dconf(DCONF_PATH) else []

    def get_name(x):
        return read_dconf(f"{DCONF_PATH}/{x}name")

    if [x for x in bindings if get_name(x) == f"'{name}'"]:
        print(f"Gnome keyboard shortcut already exists for {name}.")
    else:
        bindings.append(f"custom{len(bindings)}/")
        bindings_updated = [f"{DCONF_PATH}/{b}" for b in bindings]
        print("updated: ", bindings_updated)
        write_dconf(DCONF_PATH, f"{bindings_updated}")
        write_dconf(f"{bindings_updated[-1]}name", f"'{name}'")
        write_dconf(f"{bindings_updated[-1]}command", f"'{command}'")
        write_dconf(f"{bindings_updated[-1]}binding", f"'{binding}'")
        print(f"New Gnome keyboard shortcut registered for {name}.")


# CROW_COMMAND = "dbus-send --type=method_call --dest=io.crow_translate.CrowTranslate /io/crow translate/CrowTranslate/MainWindow io.crow_translate.CrowTranslate.MainWindow.translateSelection"

CROW_COMMAND = "dbus-send --type=method_call --dest=io.crow_translate.CrowTranslate /io/crow_translate/CrowTranslate/MainWindow io.crow_translate.CrowTranslate.MainWindow.translateSelection"

register_custom_binding("Crow", CROW_COMMAND, "<Ctrl><Alt>E")
register_custom_binding("Monitor", "gnome-system-monitor", "<Ctrl><Shift>Escape")

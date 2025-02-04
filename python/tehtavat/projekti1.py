# python implementaatio kirjanmerkkimanagerista TOML konfiguraatio kielellä
import argparse

import platformdirs
import webbrowser
import toml

parser = argparse.ArgumentParser(prog="bopy", description="Bookmark manager")
parser.add_argument("name")
parser.add_argument("--set", "-s")

config_dir = platformdirs.user_config_dir("bo", ensure_exists=True)

with open(f"{config_dir}/config.toml", "a+") as f:
    config = toml.load(f)

args = parser.parse_args()

if args.set:
    with open(f"{config_dir}/config.toml", "w") as f:
        bookmarks = config.setdefault("bookmarks", {})
        bookmarks[args.name] = args.set
        config["bookmarks"] = bookmarks
        toml.dump(config, f)
else:
    webbrowser.open_new(config["bookmarks"][args.name])

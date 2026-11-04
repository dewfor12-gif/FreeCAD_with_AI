
"""Install the FreeCAD AI module in a selected Mod directory."""

import argparse
from pathlib import Path
import shutil


def install(mod_directory):
    project_root = Path(__file__).resolve().parents[2]
    source = project_root / "src" / "Mod" / "FreeCADAI"
    target = Path(mod_directory).expanduser().resolve() / "FreeCADAI"

    if not source.is_dir():
        raise FileNotFoundError(f"Module not found: {source}")

    if target.exists():
        raise FileExistsError(
            f"Installation already exists: {target}"
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)

    print(f"Successfully installed FreeCADAI to: {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mod-dir",
        required=True,
        help="FreeCAD Mod directory for the target installation",
    )
    args = parser.parse_args()
    install(args.mod_dir)

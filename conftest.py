from pathlib import Path


def pytest_configure(config):
    root = Path(config.rootpath)
    libs = root / "libs"

    for test_dir in libs.glob("*/tests"):
        if test_dir.is_dir():
            config.args.append(str(test_dir))

# Tensorflow (2.9) starter project

A Data Science starter project with Tensorflow 2.9 on Python 3.10+.

## Setup

To keep things tidy, this project uses `poetry` for managing dependencies inside a virtual environment.

Run the following to install poetry

    $ pip install poetry

If you're on Windows, some dependency installations might break due to [Windows long path limitation](https://pip.pypa.io/warnings/enable-long-paths). You **must** run `assets/enable-win-long-paths.reg` and reboot your system to fix this issue.

Now simply run the following to install the standard data science stack

    $ poetry install

Poetry uses the following files:
* `pyproject.toml` contains all dependencies
* `poetry.toml` contains the Poetry configuration. By default the project has configured the virtual environment to be setup inside this project itself.
* `poetry.lock` file that contains the file signatures for packages and ensures that dependency tree is frozen, identical for all installs and hence reproducable.

It will also generate a `poetry.lock` file that contains the file signatures.


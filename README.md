# Tensorflow (2.9) starter project

A Data Science starter project with Tensorflow 2.9 on Python 3.8+.

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

## Project Structure


## Provisions for Visual Studio Code

The project includes a `.vscode` directory that will configure your VS Code workspace to support Python development.

### Workspace Settings (settings.json)

For now, the workspace is configured to format code using `black`

### Debug Settings (launch.json)

A debug launch configuration has been provided that will debug the open file. To avoid any `sys.path` hacks for sibling imports, it by default injects current working directory as `PYTHONPATH`.

### Extensions (extensions.json)

The following extensions will be recommended by VS Code

* Python
* Pylance (Python language servers)
* Jupyter & Jupyter Renderers

## License

The source code for the site is licensed under the MIT license, which you can find in the [LICENSE](./LICENSE) file.
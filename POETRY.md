## Poetry

 [Install to Windows](https://python-poetry.org/docs/#installing-with-the-official-installer)

 ```cmd
 (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
 ```

Add to ```Path```:
```
%APPDATA%\pypoetry\venv\Scripts\poetry on Windows.
```

Check that poetry is install:

```
poetry --version
```
---
Update poetry:

```
poetry self update
```

Instead of creating a new project, Poetry can be used to ‘initialise’ a pre-populated directory.

```
poetry init
```
If you want to add dependencies to your project, you can specify them in the tool.poetry.dependencies section.
```
[tool.poetry.dependencies]
fastapi = "^0.85.0"
```

Also, instead of modifying the pyproject.toml file by hand, you can use the add command.
```
poetry add fastapi
poetry add pytest --group test
```
Run script:
```
poetry run python your_script.py
poetry run pytest
```
The easiest way to activate the virtual environment is to create a nested shell with ```poetry shell```.

To deactivate the virtual environment and exit this new shell type ```exit```. To deactivate the virtual environment without leaving the shell use ```deactivate```.

To install the defined dependencies for your project:
```
poetry install
```
Remove package:
```
poetry remove fastapi
poetry remove pytest --group test
```
To list all the available packages
```
poetry show
poetry show --tree
poetry show --latest
```
# <HEADLINE>

<DESCRIPTION>

## Initializing the Project

I used Miniconda to set up the project environment. I only use conda to manage the Python environment and pip to manage the dependencies.

I created a new conda environment like this:

```powershell
conda create -n <ENVIRONMENT> python=3.14
```

You can create the environment and install the the dependencies by running either of the following commands:

```powershell
conda env create -f environment.yml -n <ENVIRONMENT>
conda activate <ENVIRONMENT>

# From requirements.txt
pip install -r requirements.txt
```
> [!NOTE]
> If you prefer to use a local installed Python instead of conda, you can skip the conda environment creation step and just use pip to install the dependencies. However, using a virtual environment (like conda or venv) is recommended to avoid conflicts with other projects and to keep your global Python installation clean.

> [!IMPORTANT]
> Both files, *environment.yml* and *requirements.txt*, need to be updated whenever new packages are added to the project or existing ones are updated.

```powershell
pip list --format=freeze --not-required > requirements.txt & conda env export --no-builds --ignore-channels --from-history | Select-String -NotMatch "^prefix:" > environment.yml
```

## Updating Dependencies

You can check if there are outdated packages with:

```powershell
conda update --all --dry-run
pip list --not-required --outdated
```

The version numbers in the `requirements.txt` must be updated manually. Updating dependencies should be manually and under the developer's control.

If there are any outdated packages, you can update them with:

```powershell
conda update -n <ENVIRONMENT> --all # Only if there are any dependencies installed with conda 
pip install -r requirements.txt --upgrade
```

## Testing

To make pytest and other Pylance find imports in the folder `src` or any subfolder of it, you need to configure the `PYTHONPATH` environment variable to include them. This can be done in `tests/conftest.py`:

```python
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
```

The tests can then be run with:

```powershell
pytest
```

## Optional local VS Code terminal setup (opt-in)

Machine-specific terminal profile settings are intentionally not committed to the shared workspace file.
If you want an auto-activating conda terminal in VS Code, add this to your local `.vscode/settings.json` or into a `project.local.code-workspace` file:

```json
"settings": {
    ...,
    "terminal.integrated.profiles.windows": {
        "WorkspacePwsh": {
            "path": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
            "args": [
                "-NoExit",
                "-Command",
                "cd $env:WORKSPACE_ROOT; conda activate $env:CONDA_ENV"
            ],
            "env": {
                "WORKSPACE_ROOT": "${workspaceFolder}",
                "CONDA_ENV": "<ENVIRONMENT>"
            }
        }
    },
    "terminal.integrated.defaultProfile.windows": "WorkspacePwsh",
    "python.terminal.activateEnvironment": false,
    "python.terminal.activateEnvInCurrentTerminal": false,
},
```

Adjust the profile name, shell path, and environment name to your local machine.

> [!IMPORTANT]
> In the `local.code-workspace` file, set `"CONDA_ENV"` to the name of the conda environment you created. This will allow VS Code to automatically activate the correct environment when you open the workspace.

## Security and Privacy

Under `docs/pias` is documented what personal data is processed in the app, how it is processed, and what measures are taken to protect it. These are living documents that should be updated whenever there are changes to the data processing in the app. It is important to keep these documents up to date to ensure compliance with data protection regulations and to maintain transparency with users about how their data is being used.
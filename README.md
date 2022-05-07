# QUiZ API - DRF

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/wcreativo/quiz_api.git
$ cd quiz_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd quiz_api
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.

## VSCode Settings

```json
{
    "editor.formatOnSave": true,
    "python.pythonPath": ".venv/bin/python3",
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length=120"
    ],
    "python.sortImports.args": [
        "--profile",
        "black"
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
        "editor.rulers": [
            120
        ]
    },
    "python.linting.pylamaArgs": [
        "--ignore=E501"
    ]
}


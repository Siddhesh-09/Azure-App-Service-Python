# Python 3.14 Webapp Example

This repository contains a minimal Flask web application targeting **Python 3.14**.
It also includes a few features that make it slightly different from a generic
web app scaffold:

- **Demonstrates Python 3.14 syntax** (`match`/`case`, explicit union types, etc.)
- Uses the built-in `tomllib` to parse a `config.toml` file
- Contains Azure App Service helpers (`runtime.txt` and simple `requirements.txt`)

## Files

* `app.py` – main Flask application
* `config.toml` – sample configuration consumed by `app.py`
* `requirements.txt` – dependencies for deployment
* `runtime.txt` – instructs App Service to use Python 3.14

## Running locally

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

Browse to http://localhost:8000/ or http://localhost:8000/calc?op=mul&a=3&b=4

## Deploying to Azure App Service

Create a Python Web App resource specifying **Python 3.14** as the runtime.
Push this folder to a Git repo and configure App Service to deploy from it;
`requirements.txt` and `runtime.txt` are automatically consumed.

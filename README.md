# AnnaPet
Simple model of global aviation

## Developer Guide
First set up a virtual environment "venv"
Install UV
Use UV serve to see how it works
Check the MkDocs website for reference 


### Dependences

This repository uses [uv](https://docs.astral.sh/uv) for comprehensive use and then just use uv sync
Dependency bounds are defined in ['pyproject.toml'] (pyproject.toml) and the locked environment is specified in ['uv.lock'] (uv.lock).
To create the virtual environment from lockfile make sure you have uv installed and run:

```
uv sync
```
### Model/Anaysis
this repository contains a single analysis script, [`aviation.py`](aviation.py), which implements a simple model for global aviation.
It outputs the required global fleet.
To execute the analysis script, run:

```
uv run python aviation.py
```
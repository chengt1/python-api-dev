# Development Notes


## FastAPI

Start server
```
uvicorn main:app
```
`main` is the file and `app` is the FastAPI instance.

Add option to reload when file is modified. This way we don't need to restart the server manually every time after a change.
```
uvicorn main:app --reload
```
## Virtual Environment

Create a virtual environment:

```
python3 -m venv venv
```

Second venv is the virtual environment name

Enable venv on command line:

```
Source venv/bin/activate
```

Install libraries specified in requirements.txt
```
pip install -r /path/to/requirements.txt
```
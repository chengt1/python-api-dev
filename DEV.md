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

The above command will start uvirocn on `http://127.0.0.1:8000`
Documentation is automatically made with Swagger UI support.
Go to `http://127.0.0.1:8000/docs` for swagger UI and `http://127.0.0.1:8000/redoc` for another API documentation format.

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
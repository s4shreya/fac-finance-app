

## Installation setup for backend FastAPI
1.  Create a virtual environment for our python code in FastAPI application
        >>py -m venv env       // creates a virtual environment for the project
2.  Activate virtual environment
        >>env/Scripts/activate       // we can use any name instead of env
3.  Install dependencies
        >>pip install fastapi uvicorn sqlalchemy       // uvicorn works as a server, sqlalchemy is a database toolkit for python
4.  To start the FastAPI application
        >>uvicorn main:app --reload
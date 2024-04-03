# Finance App - Full Stack web application

## Live demo


## Technologies and tools used
1.  Frontend: React.js
2.  Backend: FastAPI
3.  Database: SQLite
4.  Tools: SQLAlchemy, CORS middleware, axios

## Installation setup for frontend
```
cd frontend/
npm install
npm run dev
```

## Installation setup for backend FastAPI
1.  Create a virtual environment for the python code in FastAPI application:
```
py -m venv env                                       // creates a virtual environment for the project
```
2.  Activate virtual environment
```
env/Scripts/activate                                 // we can use any name instead of env
```
3.  Install dependencies
```
pip install fastapi uvicorn sqlalchemy               // uvicorn works as a server, sqlalchemy is a database toolkit for python
```
4.  To start the FastAPI application
```
uvicorn main:app --reload
```

## Usage of application
The finance app is used to add new transaction details and view the list of all transactions held previously. It consists of fields such as: amount, category, description, income and date.

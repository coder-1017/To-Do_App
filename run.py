from app import app # imports the flask instance created in __init__.py file. Can also be written as 'import app' 

if __name__ == "__main__" :
    app.run(debug = True)
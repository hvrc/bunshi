IF EXIST venv (
call venv/Scripts/activate.bat
) ELSE (
py -3 -m venv venv
call venv/Scripts/activate.bat
pip install -r requirements.txt
)
start chrome "http://127.0.0.1:5000/"
set FLASK_APP=bunshi
set FLASK_ENV=development
flask run
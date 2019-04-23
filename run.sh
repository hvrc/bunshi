if [ ! -d "venv" ]
then
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
else
    . venv/bin/activate
fi
open http://127.0.0.1:5000/
export FLASK_APP=bunshi
export FLASK_ENV=development
flask run

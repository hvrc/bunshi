# Bunshi

## https://bunshi.herokuapp.com/

Displays the bond-line structure of a compound. Gets images from [PubChem](https://pubchem.ncbi.nlm.nih.gov/).

## Run locally

### Optional method for Windows

Clone
```
$ git clone "https://github.com/hvrc/Bunshi.git"
$ cd Bunshi
```
Run the .bat file...
```
$ start run.bat
```
...and refresh the page

### OR

Clone
```
$ git clone "https://github.com/hvrc/Bunshi.git"
$ cd Bunshi
```

Create a virtualenv & activate it
```
$ python3 -m venv venv
$ . venv/bin/activate
```

...on Windows
```
$ py -3 -m venv venv
$ . venv/Scripts/activate

```
...on Windows cmd
```
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

Install requirements
```
$ pip install -r requirements.txt
```

Run
```
$ export FLASK_APP=bunshi
$ export FLASK_ENV=development
$ flask run
```

... on Windows cmd
```
> set FLASK_APP=bunshi
> set FLASK_ENV=development
> flask run
```

Open [localhost:5000](http://127.0.0.1:5000) in a browser

![alt text](https://i.imgur.com/W18Itgg.png)

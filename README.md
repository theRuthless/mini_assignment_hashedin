# ![Mini assignment](hashedin.png)

> ### HUex Python 9.1 Track which include FastAPI, SQLAlchemy, Alembic



This repo is under developement — suggestions and issues welcome!

## Installation

1. Clone this repository: `git clone https://github.com/theRuthless/mini_assignment_hashedin.git`.
2. `cd` into `mini_assignment_hashedin`
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
5. Install Python 3.5.2: `pyenv install 3.5.2`.
6. Create a new virtualenv called `productionready`: `pyenv virtualenv 3.5.2 productionready`.
7. Set the local virtualenv to `productionready`: `pyenv local productionready`.
8. Reload the `pyenv` environment: `pyenv rehash`.

If all went well then your command line prompt should now start with `(productionready)`.

If your command line prompt does not start with `(productionready)` at this point, try running `pyenv activate productionready` or `cd ../mini_assignment_hashedin`. 

## Coverage Report

----------- coverage: platform win32, python 3.9.7-final-0 -----------
Name               Stmts   Miss  Cover
--------------------------------------
app\crud.py           56     11    80%
app\database.py        7      0   100%
app\main.py           83      3    96%
app\models.py         48      3    94%
app\schemas.py        55      0   100%
app\test_main.py       9      0   100%
app\utils.py           4      0   100%
--------------------------------------
TOTAL                262     17    94%
If your command line prompt does not start with `(productionready)` at this point, try running `pyenv activate productionready` or `cd ../fast_api`. 

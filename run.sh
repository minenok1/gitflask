#!bin/bash/


cd ./py_env
source ./my_env/bin/activate
export FLASK_APP=app
nohup flask run 2>&1 &

#Falcon Test
##How to run
clone it

create your virtual environment running: 'virtualenv venv'

and activate it running '. /venv/bin/activate'

pip install -r requirements.txt

gunicorn app:app --restart


Tutorial on SQLalchemy: http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html


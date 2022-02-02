at conda cmd:

cd Documents
cd CreditScore
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1
flask run

--database
cd model
sqlite3 creditscore.db
.mode csv customer
.import Result.csv customer
.tables
.schema customer

# This is the boilerplate for the FASTAPI

## This includes:

- Database connection (Default: postgres in localhost)
- uses Alembic for migration of the models
- Cors setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.base.txt
python main.py
celery -A base.worker.celery worker
celery -A base.worker.celery flower
```

# tests/integration/test_database.py
from app.database.sql import Session

def test_sql_data_persistence():
    # Trigger your pipeline
    test_data = {"name": "DB Test", "email": "db@test.com"}
    # ... call your service that writes to SQL
    
    # Verify SQL write
    db = Session()
    user = db.execute("SELECT * FROM users WHERE email = 'db@test.com'").fetchone()
    assert user is not None
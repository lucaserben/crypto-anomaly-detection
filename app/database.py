from sqlalchemy import create_engine, text


database_url = ( "postgresql+psycopg2://"
    "postgres:postgres@localhost:5432/crypto_db")
engine = create_engine(database_url)

def test_connection():

    with engine.connect() as conn:
        result = conn.execute(text("select version()"))
        print(result.fetchone())
              
        





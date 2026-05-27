from sqlalchemy import create_engine, text


database_url = ( "postgresql+psycopg2://"
    "postgres:postgres@localhost:5432/crypto_db")
engine = create_engine(database_url)

def insert_anomalous_trade(trade, anomaly):

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO anomalous_trades (
                    trade_id,
                    symbol,
                    price,
                    quantity,
                    trade_value,
                    trade_time,
                    anomaly_type,
                    anomaly_score,
                    details
                )
                VALUES (
                    :trade_id,
                    :symbol,
                    :price,
                    :quantity,
                    :trade_value,
                    :trade_time,
                    :anomaly_type,
                    :anomaly_score,
                    :details
                )
                ON CONFLICT (trade_id, anomaly_type)
                DO NOTHING
            """),
            {
                "trade_id": trade["trade_id"],
                "symbol": trade["symbol"],
                "price": trade["price"],
                "quantity": trade["quantity"],
                "trade_value": trade["trade_value"],
                "trade_time": trade["trade_time"],
                "anomaly_type": anomaly["type"],
                "anomaly_score": anomaly["score"],
                "details": anomaly["details"]
            }
        )
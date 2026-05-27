SYMBOL = "btcusdt"
BINANCE_URL = f"wss://stream.binance.com:9443/ws/{SYMBOL}@trade"
DATABASE_URL = ( "postgresql+psycopg2://"
    "postgres:postgres@localhost:5432/crypto_db")

MIN_WINDOW_SIZE = 30

# whales
WHALE_FIX_TRESHOLD = 10000000
WHALE_Z_SCORE_THRESHOLD = 5

# price anomaly
PRICE_Z_SCORE_THRESHOLD = 3

# volume spike
QUANTITY_Z_SCORE_THRESHOLD = 3
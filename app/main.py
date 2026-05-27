from app.config import BINANCE_URL
from app.collector import start_collector
from app.database import test_connection
import time



def main():
    test_connection()
    print("Starting crypto anomaly detection...")
    ws, thread = start_collector(BINANCE_URL, run_in_thread=True)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping collector...")
        try:
            ws.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()

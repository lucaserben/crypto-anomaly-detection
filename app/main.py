from .config import BINANCE_URL
from .collector import start_collector


def main():
    print("Starting crypto anomaly detection...")
    start_collector(BINANCE_URL)


if __name__ == "__main__":
    main()

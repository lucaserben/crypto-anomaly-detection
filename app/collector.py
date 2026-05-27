from websocket import WebSocketApp
from collections import deque

from app.parser import parser_trade_message
from app.anomalies import detect_anomalies

recent_trade_values = deque(maxlen=100)
recent_prices = deque(maxlen=100)


def on_message(ws, message):
    trade_data = parser_trade_message(message)
    anomalies = detect_anomalies(trade_data, 
                                 recent_trade_values,
                                 recent_prices)

    recent_trade_values.append(trade_data["trade_value"])
    recent_prices.append(trade_data["price"])

    if anomalies:
        print(f"Anomalies detected for trade: {anomalies}") 

def start_collector(url):
    ws = WebSocketApp(url, on_message=on_message)
    ws.run_forever()



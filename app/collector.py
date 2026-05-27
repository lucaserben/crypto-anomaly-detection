
import threading
import time
from websocket import WebSocketApp
from collections import deque
from app.database import insert_anomalous_trade
from app.parser import parser_trade_message
from app.anomalies import detect_anomalies
import inspect


# Determine at import-time whether the anomalies function accepts recent_quantities
_detect_anomalies_params = len(inspect.signature(detect_anomalies).parameters)
_detect_anomalies_accepts_quantities = _detect_anomalies_params >= 4

recent_trade_values = deque(maxlen=100)
recent_prices = deque(maxlen=100)
recent_quantities = deque(maxlen=100)


def on_open(ws):
    print("WebSocket opened")


def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket closed: {close_status_code} {close_msg}")


def on_error(ws, error):
    print(f"WebSocket error: {error}")


def on_message(ws, message):
    trade_data = parser_trade_message(message)

    if _detect_anomalies_accepts_quantities:
        anomalies = detect_anomalies(
            trade_data,
            recent_trade_values,
            recent_prices,
            recent_quantities,
        )
    else:
        anomalies = detect_anomalies(trade_data, recent_trade_values, recent_prices)

    recent_trade_values.append(trade_data["trade_value"])
    recent_prices.append(trade_data["price"])
    recent_quantities.append(trade_data["quantity"])

   if anomalies:

    print(f"Anomalies detected for trade: {anomalies}")

    for anomaly in anomalies:
        insert_anomalous_trade(
            trade_data,
            anomaly
        )

def start_collector(url, run_in_thread=True):

    ws = WebSocketApp(
        url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close
    )
    if run_in_thread:
        t = threading.Thread(target=ws.run_forever, daemon=True)
        t.start()
        time.sleep(0.1)
        return ws, t
    else:
        ws.run_forever()
        return ws, None





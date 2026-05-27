from websocket import WebSocketApp
from collections import deque

from app.parser import parser_trade_message
from app.detector import detect_whale_trade

recent_trade_values = deque(maxlen=100)



def on_message(ws, message):
    trade_data = parser_trade_message(message)
    anomalies = detect_whale_trade(trade_data, recent_trade_values)

    recent_trade_values.append(trade_data["trade_value"])
    
    if anomalies:
        print(f"Anomalies detected for trade: {anomalies}") 

def start_collector(url):
    ws = WebSocketApp(url, on_message=on_message)
    ws.run_forever()



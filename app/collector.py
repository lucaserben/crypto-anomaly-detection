from websocket import WebSocketApp
from .parser import parser_trade_message


def on_message(ws, message):
    trade_data = parser_trade_message(message)
    print(trade_data)


def start_collector(url):
    ws = WebSocketApp(url, on_message=on_message)
    ws.run_forever()

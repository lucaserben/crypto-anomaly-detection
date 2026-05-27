import json
from datetime import datetime


def parser_trade_message(message):
    data = json.loads(message)
    trade_data = {
        "symbol": data["s"],
        "price": float(data["p"]),
        "quantity": float(data["q"]),
        "trade_value": round(float(data["p"]) * float(data["q"]),2),
        "trade_time": datetime.fromtimestamp(data["T"] / 1000),
    }
    return trade_data

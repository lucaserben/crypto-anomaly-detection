import numpy as np

min_window_size = 30

# whales
whale_fix_treshold = 10000000
whale_z_score_treshold = 5

# price anomaly
price_z_score_threshold = 3

def calculator_z_score(value, values):
    mean = np.mean(values)
    std = np.std(values)
    if std == 0:
        return 0
    return (value - mean) / std

def detect_price_anomaly(trade, recent_prices):
    anomalies = []
    price = trade["price"]
    if len(recent_prices) < min_window_size:
        return anomalies
    z_score = calculator_z_score(price, recent_prices)
    if abs(z_score) >= price_z_score_threshold:
        anomalies.append({
            "type": "price_anomaly",
            "score": abs(z_score),
            "details": "Price is unusually high or low compared to recent trades"
        })
    return anomalies

def detect_whale_trade(trade, recent_trade_values):
    anomalies = []
    trade_value = trade["trade_value"]
    if trade_value >= whale_fix_treshold:
        anomalies.append({
            "type": "whale_trade_fixed",
            "score": trade_value,
            "details": "trade value exceeds fixed whale threshold"
        })
    if len(recent_trade_values) < min_window_size:
        return anomalies
    z_score = calculator_z_score(trade_value, recent_trade_values)
    if z_score >= whale_z_score_treshold:
        anomalies.append({
            "type": "whale_trade_statistical",
            "score": z_score,
            "details": "Trade value is unusually high compared to recent trades"
        })
    return anomalies

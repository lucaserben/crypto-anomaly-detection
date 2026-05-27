import numpy as np

whale_fix_treshold = 200
whale_z_score_treshold = 5

def calculator_z_score(value, values):
    mean = np.mean(values)
    std = np.std(values)
    if std == 0:
        return 0
    return (value - mean) / std


def detect_whale_trade(trade, recent_trade_values):
    anomalies = []

    trade_value = trade["trade_value"]

    if trade_value >= whale_fix_treshold:
        anomalies.append({
            "type": "whale_trade_fixed",
            "score": trade_value,
            "details": "trade value exceeds fixed whale threshold"
        })


    z_score = calculator_z_score(trade_value, recent_trade_values)
    if z_score >= whale_z_score_treshold:
        anomalies.append({
            "type": "whale_trade_statistical",
            "score": z_score,
            "details": "Trade value is unusually high compared to recent trades"
        })

    return anomalies


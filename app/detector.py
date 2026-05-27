import numpy as np
from app.config import MIN_WINDOW_SIZE, PRICE_Z_SCORE_THRESHOLD, QUANTITY_Z_SCORE_THRESHOLD, WHALE_FIX_TRESHOLD, WHALE_Z_SCORE_THRESHOLD


#######################################################################################

def calculator_z_score(value, values):
    mean = np.mean(values)
    std = np.std(values)

    if std == 0:
        return 0

    return (value - mean) / std

#######################################################################################

def detect_price_anomaly(trade, recent_prices):

    anomalies = []

    if len(recent_prices) < MIN_WINDOW_SIZE:
        return anomalies

    price = trade["price"]

    z_score = calculator_z_score(
        price,
        recent_prices
    )

    if abs(z_score) >= PRICE_Z_SCORE_THRESHOLD:

        anomalies.append({
            "type": "price_anomaly",
            "score": round(float(abs(z_score)), 2),
            "details": "Price is unusually high or low compared to recent trades"
        })

    return anomalies

#######################################################################################

def detect_volume_spike_anomaly(trade, recent_quantities):

    anomalies = []

    if len(recent_quantities) < MIN_WINDOW_SIZE:
        return anomalies

    quantity = trade["quantity"]

    z_score = calculator_z_score(
        quantity,
        recent_quantities
    )

    if z_score >= QUANTITY_Z_SCORE_THRESHOLD:

        anomalies.append({
            "type": "volume_spike_anomaly",
            "score": round(float(z_score), 2),
            "details": "Trade quantity is unusually high compared to recent trades"
        })

    return anomalies

#######################################################################################

def detect_whale_trade(trade, recent_trade_values):

    anomalies = []

    trade_value = trade["trade_value"]

    if trade_value >= WHALE_FIX_TRESHOLD:

        anomalies.append({
            "type": "whale_trade_fixed",
            "score": round(float(trade_value), 2),
            "details": "Trade value exceeds fixed whale threshold"
        })

    if len(recent_trade_values) < MIN_WINDOW_SIZE:
        return anomalies

    z_score = calculator_z_score(
        trade_value,
        recent_trade_values
    )

    if z_score >= WHALE_Z_SCORE_THRESHOLD:

        anomalies.append({
            "type": "whale_trade_statistical",
            "score": round(float(z_score), 2),
            "details": "Trade value is unusually high compared to recent trades"
        })

    return anomalies

#######################################################################################
from app.detector import detect_whale_trade, detect_price_anomaly, detect_volume_spike_anomaly


def detect_anomalies(trade, recent_trade_values, recent_prices, recent_quantities=None):
    anomalies = []
    anomalies.extend(detect_whale_trade(trade, recent_trade_values))
    anomalies.extend(detect_price_anomaly(trade, recent_prices))
    if recent_quantities is not None:
        anomalies.extend(detect_volume_spike_anomaly(trade, recent_quantities))

    return anomalies


from app.detector import detect_whale_trade, detect_price_anomaly

def detect_anomalies(trade, recent_trade_values, recent_prices):
    anomalies = []
    anomalies.extend(detect_whale_trade(trade, recent_trade_values))
    anomalies.extend(detect_price_anomaly(trade, recent_prices))
    return anomalies


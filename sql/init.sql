CREATE TABLE IF NOT EXISTS anomalous_trades (

    trade_id BIGINT NOT NULL,

    symbol VARCHAR(20) NOT NULL,

    price NUMERIC(18,8) NOT NULL,
    quantity NUMERIC(18,8) NOT NULL,
    trade_value NUMERIC(18,8) NOT NULL,

    trade_time TIMESTAMP NOT NULL,

    anomaly_type VARCHAR(50) NOT NULL,
    anomaly_score NUMERIC(10,2),

    details TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (trade_id, anomaly_type)
);
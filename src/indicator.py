import pandas as pd


def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # === Moving Average ===
    df["ma50"] = df["close"].rolling(window=50).mean()

    # === MA Slope (%) ===
    df["ma50_slope"] = (df["ma50"] - df["ma50"].shift(1)) / df["ma50"].shift(1)

    # === RSI (14) ===
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    # === MACD (12,26,9) ===
    ema12 = df["close"].ewm(span=12, adjust=False).mean()
    ema26 = df["close"].ewm(span=26, adjust=False).mean()

    df["macd"] = ema12 - ema26
    df["signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    df["macd_hist"] = df["macd"] - df["signal"]

    return df

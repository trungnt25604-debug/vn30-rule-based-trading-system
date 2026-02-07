import pandas as pd


def load_stock_data(stock_code):
    file_path = f"data/{stock_code}.xlsx"
    df = pd.read_excel(file_path)

    # Chuẩn hoá cột
    df.columns = [col.lower() for col in df.columns]

    # Chuyển time sang datetime
    df["time"] = pd.to_datetime(df["time"])

    return df


def get_price_by_date(stock_code, date):
    df = load_stock_data(stock_code)
    date = pd.to_datetime(date)

    # Chỉ lấy dữ liệu tới thời điểm hệ thống
    df = df[df["time"] <= date]

    if df.empty:
        return None

    # Lấy giá đóng cửa gần nhất
    return df.iloc[-1]["close"]

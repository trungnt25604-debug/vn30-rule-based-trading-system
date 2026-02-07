from data_loader import load_stock_data
from indicator import calculate_indicators
from rule_engine import apply_rules


def get_recommendation(stock_code, current_date):
    # Load data
    df = load_stock_data(stock_code)

    # Chỉ lấy dữ liệu tới ngày hệ thống
    df = df[df["time"] <= current_date]

    if len(df) < 60:
        return "NO DATA", "Không đủ dữ liệu để tính chỉ báo"

    # Tính toàn bộ chỉ báo
    df = calculate_indicators(df)

    # Lấy dòng cuối cùng (thời điểm t)
    latest = df.iloc[-1]

    # Đưa vào rule engine
    action, explanation = apply_rules(latest)

    return action, explanation

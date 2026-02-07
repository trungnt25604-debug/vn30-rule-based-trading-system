from collections import Counter
from data_loader import load_stock_data
from indicator import calculate_indicators
from rule_engine import apply_rules


def backtest_stock(stock_code):
    df = load_stock_data(stock_code)
    df = calculate_indicators(df)

    actions = []
    records = []

    for i in range(50, len(df)):
        row = df.iloc[i]
        action, reason = apply_rules(row)

        actions.append(action)
        records.append({
            "time": row["time"],
            "close": row["close"],
            "action": action,
            "reason": reason
        })

    return records, actions


def summarize_actions(actions):
    counter = Counter(actions)
    total = sum(counter.values())

    print("\n📊 THỐNG KÊ KHUYẾN NGHỊ")
    print("-" * 40)

    for action, count in counter.items():
        ratio = count / total * 100
        print(f"{action}: {count} lần ({ratio:.2f}%)")


if __name__ == "__main__":
    # Backtest VIC
    records_vic, actions_vic = backtest_stock("VIC")

    print("\n📅 KẾT QUẢ CUỐI KỲ - VIC")
    for r in records_vic[-30:]:
        print(
            f"{r['time'].date()} | "
            f"Giá: {r['close']} | "
            f"{r['action']}"
        )

    summarize_actions(actions_vic)

    # Backtest HPG
    records_hpg, actions_hpg = backtest_stock("HPG")

    print("\n📅 KẾT QUẢ CUỐI KỲ - HPG")
    for r in records_hpg[-30:]:
        print(
            f"{r['time'].date()} | "
            f"Giá: {r['close']} | "
            f"{r['action']}"
        )

    summarize_actions(actions_hpg)



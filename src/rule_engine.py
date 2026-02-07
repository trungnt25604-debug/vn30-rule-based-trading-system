def apply_rules(row: dict):
    price = row["close"]
    ma50 = row["ma50"]
    slope = row["ma50_slope"]
    rsi = row["rsi"]
    macd = row["macd"]

    macd_threshold = 0.02 * price   # 2% * Ct
    slope_threshold = 0.0005        # 0.05%

    # ===== RULE 7: OVERSOLD BOUNCE =====
    if rsi < 30 and abs(macd) < macd_threshold:
        return (
            "HOLD",
            "RSI < 30, MACD yếu → quá bán, khả năng hồi kỹ thuật"
        )

    # ===== RULE 1 =====
    if (
        price > ma50
        and slope > slope_threshold
        and macd >= macd_threshold
        and rsi <= 70
    ):
        return (
            "HOLD",
            "Xu hướng tăng mạnh, MA dốc lên, động lượng tốt"
        )

    # ===== RULE 2 =====
    if (
        price > ma50
        and slope > slope_threshold
        and macd >= macd_threshold
        and rsi > 70
    ):
        return (
            "CONSIDER SELL",
            "Giá tăng mạnh nhưng RSI quá mua, rủi ro điều chỉnh"
        )

    # ===== RULE 3 =====
    if (
        price > ma50
        and abs(slope) <= slope_threshold
        and 30 <= rsi <= 70
        and macd >= macd_threshold
    ):
        return (
            "HOLD",
            "Xu hướng tăng nhưng động lượng yếu, tiếp tục nắm giữ"
        )

    # ===== RULE 4 =====
    if (
        price < ma50
        and slope < -slope_threshold
        and rsi >= 30
        and macd <= -macd_threshold
    ):
        return (
            "SELL",
            "Xu hướng giảm mạnh, MA dốc xuống, động lượng âm"
        )

    # ===== RULE 5 =====
    if (
        price < ma50
        and abs(slope) <= slope_threshold
        and 30 <= rsi <= 70
        and macd <= -macd_threshold
    ):
        return (
            "SELL",
            "Xu hướng yếu, động lượng giảm"
        )

    # ===== RULE 6: CHUYỂN PHA =====
    if (
        abs(price - ma50) / ma50 <= 0.01
        and 30 <= rsi <= 70
        and abs(macd) < macd_threshold
    ):
        return (
            "HOLD / SELL",
            "Giai đoạn chuyển pha, xu hướng chưa rõ ràng"
        )

    # ===== DEFAULT =====
    return (
        "SELL",
        "Chỉ báo chưa có tín hiệu, có thể bán để bảo toàn lợi nhuận"
    )

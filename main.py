from portfolio import Portfolio

current_date = "2025-10-15"

portfolio = Portfolio()

# 1. Khởi tạo danh mục (giả lập user đã mua trước đó)
portfolio.add_stock(
    stock_code="VIC",
    buy_price=50000,
    quantity=1000,
    target_price=100000,
    buy_date="2024-01-15"
)

# 2. Cập nhật danh mục theo ngày hệ thống
portfolio.update_portfolio(current_date)
# 3. Hiển thị danh mục (có highlight 🔔)
portfolio.show_portfolio()
# 4. Kiểm tra cổ phiếu đạt giá mục tiêu
portfolio.check_target_reached()

alerts = portfolio.check_target_reached()

if alerts:
    print("\n🔔 CÓ CỔ PHIẾU ĐẠT GIÁ MỤC TIÊU!")

# 5. User vào xem thông báo & quyết định
portfolio.handle_alerts(current_date)




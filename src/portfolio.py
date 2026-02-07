from data_loader import get_price_by_date
from recommendation import get_recommendation

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock_code, buy_price, quantity, target_price, buy_date):
        current_price = get_price_by_date(stock_code, buy_date)

        profit = (current_price - buy_price) * quantity

        stock = {
            "code": stock_code,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
            "profit": profit,
            "target_price": target_price,
            "buy_date": buy_date,
            "status": "NORMAL",
            "notified": False
        }

        self.stocks.append(stock)

    def show_portfolio(self):
        if not self.stocks:
            print("Danh mục hiện tại đang trống.")
            return

        print("\nDANH MỤC HIỆN TẠI")
        print("-" * 60)

        for idx, stock in enumerate(self.stocks, start=1):
            status_flag = " 🔔" if stock["status"] == "TARGET_REACHED" else ""

            print(
                f"{idx}. {stock['code']}{status_flag} | "
                f"Giá mua: {stock['buy_price']} | "
                f"KL: {stock['quantity']} | "
                f"Giá hiện tại: {stock['current_price']} | "
                f"Lãi/Lỗ: {stock['profit']:.2f} | "
                f"Mục tiêu: {stock['target_price']}"
            )

    #Thêm hàm update danh mục
    def update_portfolio(self, current_date):
        for stock in self.stocks:
            latest_price = get_price_by_date(stock["code"], current_date)
            stock["current_price"] = latest_price
            stock["profit"] = (latest_price - stock["buy_price"]) * stock["quantity"]
    #Thêm hàm kiểm tra đạt giá target
    def check_target_reached(self):
        alerts = []

        for stock in self.stocks:
            if (
                    stock["current_price"] >= stock["target_price"]
                    and stock["status"] == "NORMAL"
            ):
                stock["status"] = "TARGET_REACHED"
                alerts.append(stock)

        return alerts

#Click vào thông báo
    def handle_alerts(self, current_date):
        alerts = [s for s in self.stocks if s["status"] == "TARGET_REACHED"]

        if not alerts:
            print("\nKhông có cổ phiếu nào cần xử lý.")
            return

        print("\n📌 CỔ PHIẾU ĐẠT GIÁ MỤC TIÊU:")

        for idx, stock in enumerate(alerts, start=1):
            print(f"{idx}. {stock['code']} | Giá hiện tại: {stock['current_price']}")

        choice = input("\nChọn số cổ phiếu để xem khuyến nghị (0 để thoát): ")

        if choice == "0":
            return

        stock = alerts[int(choice) - 1]

        action, reason = get_recommendation(stock["code"], current_date)

        print("\n📊 KHUYẾN NGHỊ")
        print(f"Cổ phiếu: {stock['code']}")
        print(f"Hành động đề xuất: {action}")
        print(f"Lý do: {reason}")

        self.handle_user_decision(stock)

#Chọn hành động bán/hold
    def handle_user_decision(self, stock):
        print("\n👉 Bạn muốn làm gì?")
        print("1. Bán cổ phiếu")
        print("2. Tiếp tục nắm giữ (nhập giá mục tiêu mới)")
        print("0. Chưa quyết định")

        decision = input("Lựa chọn: ")

        if decision == "1":
            self.stocks.remove(stock)
            print(f"✅ Đã bán cổ phiếu {stock['code']} và loại khỏi danh mục.")

        elif decision == "2":
            new_target = float(input("Nhập giá mục tiêu mới: "))
            stock["target_price"] = new_target
            stock["status"] = "NORMAL"
            print(f"🔄 Đã cập nhật giá mục tiêu mới cho {stock['code']}.")

        else:
            print("⏳ Chưa có hành động. Cổ phiếu vẫn được theo dõi.")




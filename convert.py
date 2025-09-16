def convert_dollar(usd):
    """Convert USD to INR, GBP, CNY. Returns multiple values."""
    rate_inr = 83.50   # 1 USD = 83.50 INR
    rate_gbp = 0.78    # 1 USD = 0.78 GBP
    rate_cny = 7.20    # 1 USD = 7.20 CNY

    inr = usd * rate_inr
    gbp = usd * rate_gbp
    cny = usd * rate_cny

    return inr, gbp, cny

def main():
    while True:
        s = input("Enter dollar ($) (* to exit): ").strip()
        if s == "*":
            print("Bye")
            break

        parts = s.split("@")
        usd_values = []
        for part in parts:
            try:
                usd_values.append(float(part))
            except ValueError:
                print(f"Ignored invalid entry: {part}")

        if not usd_values:
            continue

        print(f"{'Dollar ($)':<15}{'Indian Rupee (R)':<20}{'British (Pound)':<20}{'China (Y)':<20}")
        for usd in usd_values:
            inr, gbp, cny = convert_dollar(usd)
            print(f"{usd:<15.2f}{inr:<20.2f}{gbp:<20.2f}{cny:<20.2f}")

if __name__ == "__main__":
    main()

def get_demand_forecast_input():
    product_id = input("Enter Product ID: ")
    forecast_date = input("Enter Forecast Date (YYYY-MM-DD): ")
    print(f"\nReceived Demand Forecasting Input:")
    print(f"  Product ID: {product_id}")
    print(f"  Forecast Date: {forecast_date}")
    return {"product_id": product_id, "forecast_date": forecast_date}

def get_visibility_platform_input():
    tracking_id = input("Enter Tracking ID: ")
    print(f"\nReceived Visibility Platform Input:")
    print(f"  Tracking ID: {tracking_id}")
    return {"tracking_id": tracking_id}

def get_logistics_optimization_input():
    departure = input("Enter Departure Location: ")
    arrival = input("Enter Arrival Location: ")
    print(f"\nReceived Logistics Optimization Input:")
    print(f"  Departure Location: {departure}")
    print(f"  Arrival Location: {arrival}")
    return {"departure": departure, "arrival": arrival}

def get_risk_management_input():
    risk_factors = ["supplier", "logistics", "demand"]
    print("Available Risk Factors:")
    for i, factor in enumerate(risk_factors):
        print(f"{i+1}. {factor}")
    while True:
        try:
            choice = int(input("Select Risk Factor (enter the number): "))
            if 1 <= choice <= len(risk_factors):
                risk_factor = risk_factors[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"\nReceived Risk Management Input:")
    print(f"  Risk Factor: {risk_factor}")
    return {"risk_factor": risk_factor}

if __name__ == "__main__":
    while True:
        print("\nSCM Management Interface (Console)")
        print("1. Demand Forecasting")
        print("2. Visibility Platform")
        print("3. Logistics Optimization")
        print("4. Risk Management")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_demand_forecast_input()
        elif choice == '2':
            get_visibility_platform_input()
        elif choice == '3':
            get_logistics_optimization_input()
        elif choice == '4':
            get_risk_management_input()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

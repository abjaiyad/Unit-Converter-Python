# Unit Converter

while True:

    print("\n===== UNIT CONVERTER =====")
    print("1. KM -> Meter")
    print("2. Celsius -> Fahrenheit")
    print("3. KG -> Gram")
    print("4. Minutes -> Hours")
    print("5. Rupees -> Dollars")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        km = float(input("Enter the distance in kilometers: "))
        meter = km * 1000
        print(f"{km}km is {meter}m")

    elif choice == 2:
        celsius = float(input("Enter the temperature in celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"{celsius}℃ is {fahrenheit}℉")

    elif choice == 3:
        kg = float(input("Enter the weight in kilograms: "))
        gram = kg * 1000
        print(f"{kg}kg is {gram}g")

    elif choice == 4:
        minutes = int(input("Enter the time in minutes: "))
        hours = minutes // 60
        minutes_left = minutes % 60
        print(f"{minutes} min = {hours} hours and {minutes_left} minutes")

    elif choice == 5:
        rupees = int(input("Enter the amount of money in rupees: "))
        dollars = rupees / 96.50
        print(f"{rupees}INR is {dollars:.2f}$")

    elif choice == 6:
        print("Thank you for using unit converter.")
        break
    
    else:
        print("Invalid choice.")
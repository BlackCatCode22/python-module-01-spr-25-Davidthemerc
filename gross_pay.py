# Prompt the user for weekly hours worked and hourly rate
weeklyHours = input("Weekly hours worked? ")

try:
    hourlyRate = input("Hourly pay rate? ")

    try:

        # Convert string values to float
        weeklyHours = float(weeklyHours)
        hourlyRate = float(hourlyRate)

        # Calculate gross pay
        grossPay = weeklyHours * hourlyRate

        # If user worked more than 40 hours in the week, calculate overtime pay
        if weeklyHours > 40:
            grossPay = hourlyRate * 40
            overHours = weeklyHours - 40
            overPay = overHours * (hourlyRate * 1.5)
            grossPay += overPay
            overPay = str(overPay)

            # Round pay
            grossPay = round(grossPay, 2)

            # Stringify gross pay
            grossPay = str(grossPay)

            # Print gross pay
            print("Your gross pay is: $" + grossPay + ". This includes $" + overPay + " of overtime pay.")

        else:

            # Stringify gross pay
            grossPay = str(grossPay)

            # Print gross pay (no overtime)
            print("Your gross pay is: $" + grossPay)

    except:
        print("Please enter numbers only.")

except:
    print("Please enter numbers only.")

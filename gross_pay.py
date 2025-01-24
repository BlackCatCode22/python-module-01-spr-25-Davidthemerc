# Prompt the user for weekly hours worked and hourly rate
weeklyHours = input("Weekly hours worked? ")

try:
    hourlyRate = input("Hourly pay rate? ")

    try:

        # Convert string values to float
        weeklyHours = float(weeklyHours)
        hourlyRate = float(hourlyRate)

        # Calculate gross pay
        grossPay = round(weeklyHours * hourlyRate,2)

        # If user worked more than 40 hours in the week, calculate overtime pay
        if weeklyHours > 40:
            grossPay = round((hourlyRate * 40) + (weeklyHours - 40) * (hourlyRate * 1.5),2)

            # Print gross pay
            print("Your gross pay is: $" + str(grossPay) + ". This includes $" + str(grossPay) + " of overtime pay.")

        else:
            # Print gross pay (no overtime)
            print("Your gross pay is: $" + str(grossPay))

    except:
        print("Please enter numbers only.")

except:
    print("Please enter numbers only.")

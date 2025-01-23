# Import datetime
from datetime import datetime

# Accept name as input for variable userName
userName = input("What is your name? ")

# Get the time
time = datetime.now()
hour = time.hour
#print (hour)

# Set greeting
if hour < 12:
    greeting = "morning"
elif hour >= 17:
    greeting = "evening"
else:
    greeting = "afternoon"

# Print Greeting
print("Hello " + userName + ". Good " + greeting + "!" )
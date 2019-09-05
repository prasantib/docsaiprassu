hours = int(input("Enter the number of hours worked: "))
rate = int(input("What is the pay rate? "))

if hours > 40:
        overtimeRate = 1.5 * rate
        overtime = (hours - 40) * overtimeRate
        hours = 40
else:
        overtime = 0

regular = hours * rate
pay = regular + overtime

print("You earned", (hours*3-min(40,hours))*rate/2)
        





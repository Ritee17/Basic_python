#Write a program that converts a given number of days into weeks and days 
num_days = int(input("Enter the number of days: "))
weeks = num_days // 7
days = num_days % 7
print(f"{num_days} days is equal to {weeks} weeks and {days} days.")
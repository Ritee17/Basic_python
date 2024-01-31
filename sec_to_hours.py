# create a program that converts a given number of seconds into hours,minutes,and seconds /
second=int(input("Enter the number of seconds: "))
hours=second//3600
minutes=(second%3600)//60
seconds=(second%3600)%60
print("The given number of seconds is equal to",hours,"hours",minutes,"minutes and",seconds,"seconds")


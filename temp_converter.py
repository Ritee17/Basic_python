#develop a temperature converter program that converts between celcius, fahrenheit and kelvin
temperature=int(input("enter the temperature in celcius: "))
celcius=temperature
fahrenheit=celcius*9/5+32
kelvin=celcius+273.15
print("the temperature in celcius is: ",celcius)
print("the temperature in fahrenheit is: ",fahrenheit)
print("the temperature in kelvin is: ",kelvin)


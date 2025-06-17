def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Main program
temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C, F, K): ").upper()

if unit == "C":
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
elif unit == "F":
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
elif unit == "K":
    print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
    print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
else:
    print("Invalid unit entered!")

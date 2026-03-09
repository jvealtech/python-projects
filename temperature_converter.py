print("Temperature Converter")
print("--------------------------------------")


fahrenheit = float(input("Enter temperature in Fahrenheit :  "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equal to {celsius: .2f}°C")


if celsius < 0:
    print("Category: Freezing")
elif celsius <= 25:
    print("Category: Cool")
else:
    print("Category: Warm")
    
    
except ValueError:
    print("Please enter a valid number.")
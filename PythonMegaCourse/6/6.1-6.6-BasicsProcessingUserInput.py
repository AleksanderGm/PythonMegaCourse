def weather_condition(temperature):
    if temperature > 7:
        return("Warm")
    else:
        return("Cold")

print(weather_condition(10))

user_input = float(input("Enter temperature:"))

print(weather_condition(user_input))

print(type(user_input))



### input_from_user = input("Enter your name: ")

### message = "Hello %s!" % input_from_user ###

### message = f"Hello {input_from_user}"
### print(message)

### Over ser du med bare en variable, under viser jeg hvis jeg skal ha førstenavn og etternavn  ###

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

### message = "Hello %s %s!" % (first_name, surname)
message = f"Hello {first_name} {surname}!"
print(message)
monday_temperatures = [9.1, 8.8, 7.6]

#   print(round(monday_temperatures[0]))
#   print(round(monday_temperatures[1]))
#   print(round(monday_temperatures[2]))

for temperature in monday_temperatures:
    print(round(temperature))


for letter in "hello":
    print(letter)

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.values():
    print((grades))

for grades in student_grades.items():
    print((grades))

for grades in student_grades.keys():
    print((grades))


# a = 3

# while a > 0:
    # print(1)
    # print(2)

#   username = ""
#   while username != "pypy":
    #   username = input("Enter username: ")

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean


student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
monday_temperatures = [1.0, 4.0, 5.0]
print(mean(student_grades))
print(mean(monday_temperatures))

if 10 < 1:
    print("Not greater")
else:
    print("Greater")

x = 10
y = 10
if x < y:
    print("x is Greater than y")
elif x == y:
    print("x is the same as y")
else:
    print("x is Smaller than y")


message = "Hello there"
if "Hello" in message:
    print("Hi")
else:
    print("I dont understand")

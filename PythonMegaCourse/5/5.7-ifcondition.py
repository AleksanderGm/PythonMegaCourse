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


def nice(value):
    if type(value) == dict:
        are_sure = sum(value.values()) / len(value)
    else:
        are_sure = sum(value) / len(value)
    
    return are_sure

print(nice(student_grades))

print(type(student_grades))
print(type(monday_temperatures))


def cube_volume(a):
    return a * a * a


message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")


message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")


x = 1
y = 1

if x == 1 and y==1:
    print("Yes")
else:
    print("No")


x = 1
y = 2

if x == 1 or y==2:
    print("Yes")
else:
    print("No")

isinstance("abc", str)
isinstance([1, 2, 3], list)
or

type("abc") == str
type([1, 2, 3]) == lst
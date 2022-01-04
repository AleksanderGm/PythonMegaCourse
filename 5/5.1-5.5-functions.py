def mean(mylist):
    print("Function started!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))

mymean = mean([0, 3, 4])
print(mymean + 10)
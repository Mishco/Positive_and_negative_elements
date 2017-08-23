# number of test case
T = int(input())
i = 0
while i < T:
    N = int(input())

    array = input().strip().split(" ")
    array = list(map(int, array))

    positiveArray = [y for y in array if y >= 0]
    negaviteArray = [x for x in array if x<0]

    array = ["{} {:02}".format(b_, a_) for a_, b_ in zip(negaviteArray, positiveArray)]
    print(*array)
    i=i+1
# End of while
# Code by Michal Slovik

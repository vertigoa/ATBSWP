def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
jerk = ['some', 42]
print(spam)
eggs(jerk)
print(jerk)
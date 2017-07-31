mySiblings = []
while True:
    print('Enter the name of sibling: ' + str(len(mySiblings) + 1) + ' (Or press enter to stop.)')
    name = input()
    if name == '':
        break
    mySiblings = mySiblings + [name]
print('Your sibling names are: ')
for name in mySiblings:
    print(' ' + name)

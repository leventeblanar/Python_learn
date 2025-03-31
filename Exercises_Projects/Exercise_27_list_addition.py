# dogNames = []

# while True:
#     print('Enter the name of cat ' + str(len(dogNames) + 1) +
#       ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     dogNames = dogNames + [name]
#     print('The dof names are:')
#     for name in dogNames:
#         print(' ' + name)



supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
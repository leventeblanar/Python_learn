dogNames = []

while True:
    print('Enter the name of cat ' + str(len(dogNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dogNames = dogNames + [name]
    print('The dof names are:')
    for name in dogNames:
        print(' ' + name)
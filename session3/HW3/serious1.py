items = ['T-shirt', 'Sweater']

x = True
while x:
    w = input("Welcome to our shop, what do you want:(C, R, U, D)? ")

    if w == 'R' or w == 'r':
        print('Our items: ', end='')
        print(*items, sep=', ')

    elif w == 'C' or w == 'c':
        new_item = input('Enter new item: ')
        items.append(new_item)
        print('Our items: ', end='')
        print(*items, sep=', ')

    elif w == 'U' or w == 'u':
        while True:
            pos = int(input('Update postion: '))
            if pos < 0 or pos > len(items):
                print('Invalid position')
            else:
                new_item = input('Enter new item: ')
                items[pos - 1] = new_item
                print('Our items: ', end='')
                print(*items, sep=', ')
                break

    elif w == 'D' or w == 'd':
        pos = int(input('Delete position: '))
        while True:
            if pos < 0 or pos > len(items):
                print('Invalid position')
            else:
                del items[pos - 1]
                #items.pop(pos - 1)
                # items.remove(items[pos -1])
                print('Our items: ', end='')
                print(*items, sep=', ')
                break

    else:
        print('Invalid option')

    quit = input('Enter Q to quit or anything else to continue: ')

    if quit == 'q' or quit == 'Q':
        x = False

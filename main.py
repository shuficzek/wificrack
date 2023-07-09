with open('list.txt', 'w') as file:
    for i in range(1, 100000000):
        number = str(i).zfill(8)
        file.write(number + '\n')

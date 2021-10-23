def maopao(number):
    for j in range(len(number) -1, -1, -1):
        for i in range(j):
            if number[i] > number[i +1]:
                number[i], number[i+1] = number[i+1], number[i]

            print (number)


def main():
    number = [23, 12, 9, 15, 6]
    maopao(number)


if __name__== '__main__':
    main()

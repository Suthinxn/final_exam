def get_coins(input_change):
    count = 0
    while(input_change > 0):

        if input_change == 6:
            # print("6",input_change)
            input_change -= 6
            count += 2

        elif input_change >= 4:
            # print("4",input_change)
            input_change -= 4
            count += 1
        elif input_change > 3:
            # print("3", input_change)
            input_change -=3
            count += 1
        else:
            # print("1",input_change)
            input_change -=1
            count += 1

    print("The minimum coin is ",count)
if __name__ == '__main__':
    input_change = int(input("Enter change: "))

    result = get_coins(input_change)



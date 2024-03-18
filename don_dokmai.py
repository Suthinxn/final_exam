def get_flower(input_don, input_pirce):
    count = 0
    budget = int(input_don[1])
    for i in range(int(input_don[0])):
        # print("i",i)
        if budget > int(input_pirce[i]):
            budget -= int(input_pirce[i])
            count +=1

    print(count)
    # print(budget)



if __name__ == '__main__':
    input_don = input().split()
    input_pirce = input().split()

    result = get_flower(input_don, input_pirce)
    # print(input_don)
    # print(input_pirce)

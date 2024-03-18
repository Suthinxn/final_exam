def get_monhkol(input_number_mongkol):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    for i in str(input_number_momgkol):
        print("i", i)
        # count += 1
        for j in nums:
            if input_number_momgkol % int(j) == 0:
                count += 1
    
    print("c",count)
    if count % 2 == 0:
            print("No")
    else:
        print("Yes")
    count = 0


if __name__ == '__main__':
    input_round = int(input())

    for i in range(input_round):
        input_number_momgkol = int(input())
        result = get_monhkol(input_number_momgkol)

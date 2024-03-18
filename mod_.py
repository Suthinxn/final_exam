def get_result(input_nums):
    count = 0
    for i in str(input_nums):
        
        if int(i) == 0:
            pass 
        elif input_nums % int(i) == 0:
            count += 1
        
    print(count)

if __name__ == '__main__':
    input_round = int(input())

    for i in range(input_round):
        
        input_nums = int(input())
        result = get_result(input_nums)

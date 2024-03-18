
def get_time_english(input_hour, input_minute):
    
    numbers = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]
    


    if input_minute == 0:
        print(numbers[input_hour],"o' clock")

    elif input_minute <= 30:
        if input_minute == 15:
            print("quarter past", numbers[input_hour])
        elif input_minute == 30:
            print("half past",numbers[input_hour])
        elif input_minute == 1:
            print(numbers[input_minute],"minute past",numbers[input_hour])
        else:
            print(numbers[input_minute],"minutes past",numbers[input_hour]) 

    else:
        if input_minute == 45:
            print("quarter past", numbers[input_hour+1])
        elif input_minute == 59:
            print("one minute to",numbers[input_hour+1])
        else:
            print(numbers[60-input_minute],"minutes to",numbers[input_hour+1])


if __name__ == '__main__':


    input_hour = int(input())
    input_minute = int(input())

    result = get_time_english(input_hour, input_minute)

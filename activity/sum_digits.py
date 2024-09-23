def sum_digits(number):
    sum = 0 
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def run_sum_digits():
    num = 123
    # num = 12345678
    # num = 123456789012345678901234567890
    print(f"sum of the digits: {sum_digits(num)}")
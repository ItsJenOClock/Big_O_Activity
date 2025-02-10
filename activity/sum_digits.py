# Time complexity: O(log n)
# Space complexity: O(1)
def sum_digits(number):
    sum = 0 
    while number > 0:
        sum += number % 10
        print(sum)
        number //= 10
        print(number)
    return sum

def run_sum_digits():
    num = 123
    print(f"sum of the digits: {sum_digits(num)}")
    num = 12345678
    print(f"sum of the digits: {sum_digits(num)}")
    num = 123456789012345678901234567890
    print(f"sum of the digits: {sum_digits(num)}")
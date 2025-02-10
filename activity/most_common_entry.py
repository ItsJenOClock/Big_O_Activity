def most_common_entry(numbers):
    # Time complexity: O(n)
    # Space complexity: O(n) - worst case scenario
    counts = {}

    for num in numbers:
        count = count.get(num, 0)
        counts[num] = count + 1
    
    entry = None
    max_number_of_occurrences = 0

    for num, count in counts.items():
        if count > max_number_of_occurrences:
            entry = num
            max_number_of_occurrences = count

        return entry

    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # entry = numbers[0]
    # max_number_of_occurences = 1

    # current_index = 0
    # while current_index < len(numbers):
    #     j = current_index + 1
    #     current_entry = numbers[current_index]

    #     current_count = 1
    #     while j < len(numbers):
    #         if numbers[j] == current_entry:
    #             current_count += 1

    #         j += 1

    #     if current_count > max_number_of_occurences:
    #         max_number_of_occurences = current_count
    #         entry = numbers[current_index]

    #     current_index += 1

    # return entry

def run_most_common_entry():
    numbers = [1, 1, 2, 3, 5, 8, 13, 5, 21, 5]
    print(f"most common entry is: {most_common_entry(numbers)}")
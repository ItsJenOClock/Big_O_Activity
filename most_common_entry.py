def most_common_entry(numbers):
    entry = numbers[0]
    max_number_of_occurences = 1

    current_index = 0
    while current_index < len(numbers):
        j = current_index + 1
        current_entry = numbers[current_index]

        current_count = 1
        while j < len(numbers):
            if numbers[j] == current_entry:
                current_count += 1

            j += 1

        if current_count > max_number_of_occurences:
            max_number_of_occurences = current_count
            entry = numbers[current_index]

        current_index += 1

    return entry

def run_most_common_entry():
    numbers = [1, 1, 2, 3, 5, 8, 13, 5, 21, 5]
    print(f"most common entry is: {most_common_entry(numbers)}")
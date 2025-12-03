def get_highest_number_in_string(number_as_string: str):
    sorted_list_of_digits = sorted(list(set(number_as_string)), reverse=True)
    highest_digit = sorted_list_of_digits[0]
    return highest_digit


def get_highest_joltage(bank):
    highest_digit = get_highest_number_in_string(bank)
    highest_digit_index = bank.index(highest_digit)

    if highest_digit_index == len(bank)-1: # for last index, 
        highest_digit = get_highest_number_in_string(bank[:-1])
        highest_digit_index = bank.index(highest_digit)

    subsequence_after_highest_digit = bank[highest_digit_index+1:]
    next_highest_digit = get_highest_number_in_string(subsequence_after_highest_digit)

    return highest_digit+next_highest_digit
    
if __name__ == "__main__":
    joltage_banks = []
    # Read the input fil"e
    with open("input.txt") as input_file:
        joltage_banks = input_file.readlines()

    total_joltage = 0
    for bank in joltage_banks:
        joltage = get_highest_joltage(bank.strip())
        print(f"Joltage is {joltage=} for bank {bank=}")
        total_joltage += int(joltage)
    
    print(f"Total Joltage = {total_joltage=}")
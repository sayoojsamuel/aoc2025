def get_highest_number_in_string(number_as_string: str):
    sorted_list_of_digits = sorted(list(set(number_as_string)), reverse=True)
    highest_digit = sorted_list_of_digits[0]
    # print(f"get_highest_number_in_string: Got {highest_digit} in {number_as_string}")
    return highest_digit


def get_highest_joltage(bank):
    highest_digit = get_highest_number_in_string(bank)
    highest_digit_index = bank.index(highest_digit)

    if highest_digit_index == len(bank) - 1:  # for last index,
        highest_digit = get_highest_number_in_string(bank[:-1])
        highest_digit_index = bank.index(highest_digit)

    subsequence_after_highest_digit = bank[highest_digit_index + 1 :]
    next_highest_digit = get_highest_number_in_string(subsequence_after_highest_digit)

    return highest_digit + next_highest_digit


def get_highest_12_digit_joltage(bank):
    print(f"get_highest_12_digit_joltage: {bank=}")
    len_bank = len(bank)

    final_joltage = ""
    highest_digit_index = 0
    sub_sequence = bank
    for i in range(12):
        sub_sequence = bank[highest_digit_index : len_bank - 11 + i]

        highest_digit = get_highest_number_in_string(sub_sequence)
        highest_digit_index = (
            bank[highest_digit_index:].index(highest_digit) + highest_digit_index
        )

        print(
            f"{i=}; Got {highest_digit} in {sub_sequence}; \t\t\t{highest_digit_index=}"
        )
        final_joltage += highest_digit

        # increment highest_digit_index for next interation of slicing
        highest_digit_index += 1

    return final_joltage


if __name__ == "__main__":
    joltage_banks = []
    # Read the input fil"e
    with open("input.txt") as input_file:
        joltage_banks = input_file.readlines()

    total_joltage = 0
    for bank in joltage_banks:
        joltage = get_highest_12_digit_joltage(bank.strip())
        print(f"Joltage is {joltage=} for bank {bank=}")
        total_joltage += int(joltage)

    print(f"Total Joltage = {total_joltage=}")

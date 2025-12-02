from collections import namedtuple

ProductRange = namedtuple("ProductRange", "starting_id ending_id")


def extract_product_ranges(product_ids_input) -> list[ProductRange]:
    product_pair_strings = product_ids_input.split(",")

    product_range_list: list[ProductRange] = []
    for product_pair in product_pair_strings:
        product_range_list.append(tuple(map(int, product_pair.split("-"))))

    return product_range_list


def check_for_invalid_id(number) -> bool:
    number_of_digits = len(str(number))

    # needs to be even
    if number_of_digits % 2 != 0:
        return False

    half_number_of_digits = number_of_digits // 2

    lsb = number % 10**half_number_of_digits
    msb = (number - lsb) // 10**half_number_of_digits

    return lsb == msb


def get_next_invalid_id(number) -> int:
    number_of_digits = len(str(number))

    # for odd digit count numbers, upgrade to the next even digit count numbers
    if number_of_digits % 2 != 0:
        # next nearest even number of digits
        next_even_digit_number = 10**number_of_digits
        number = next_even_digit_number
        number_of_digits += 1

    half_number_of_digits = number_of_digits // 2

    lsb = number % 10**half_number_of_digits
    msb = number // 10**half_number_of_digits

    next_number = 0
    # if lsb is less than msb, next_number is MSB|MSB
    if lsb < msb:
        next_number = msb * 10**half_number_of_digits + msb

    # is lsb is greater than msb, we should increment msb
    if lsb >= msb:
        msb += 1
        # since we are incrementing msb, the number of digits of msb might change
        msb_number_of_digits = len(str(msb))
        next_number = msb * 10**msb_number_of_digits + msb

    return next_number


if __name__ == "__main__":
    product_range_list: list[ProductRange] = []

    with open("input.txt") as input_file:
        product_ids_input = input_file.read()
        product_range_list = extract_product_ranges(product_ids_input)

    invalid_ids = []
    for starting_id, ending_id in product_range_list:
        print(f"{starting_id=};; {ending_id=}")
        local_invalid_ids = []

        if check_for_invalid_id(starting_id):
            local_invalid_ids.append(starting_id)

        next_invalid_id = get_next_invalid_id(starting_id)
        while next_invalid_id <= ending_id:
            local_invalid_ids.append(next_invalid_id)
            next_invalid_id = get_next_invalid_id(next_invalid_id)

        print(f"{local_invalid_ids=}")
        invalid_ids.extend(local_invalid_ids)

    print(f"{invalid_ids=}")
    print(f"{sum(invalid_ids)=}")

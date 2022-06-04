def get_new_num(num: int):
    tens = num // 10
    units = num % 10

    sum_of_tens_and_units = tens + units

    return (units * 10) + (sum_of_tens_and_units % 10)


def main(new_number, standard, cycle_count=1):
    if new_number is None:
        new_number = get_new_num(standard)
        main(new_number, standard)

    condition = new_number == standard

    return cycle_count if condition else main(get_new_num(new_number), standard, cycle_count + 1)


number = int(input())
print(main(new_number=None, standard=number, cycle_count=1))

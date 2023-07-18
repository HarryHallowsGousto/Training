
def odd_or_even(input_value: int) -> str:
    if input_value % 3 == 0:
        return "three"
    if input_value % 2 == 0:
        return "even"
    else:
        return "odd"

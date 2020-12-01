def load_data(input_filename: str) -> list:
    with open("day1.in", "rb") as fp:
        entries = [int(x) for x in fp.readlines()]

    return entries

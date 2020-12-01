from day1_lib import load_data


def twosum(target_sum: int, entries: list) -> int:
    """
    O(N)
    """
    seen = dict()
    for entry in entries:
        if seen.get(target_sum - entry, None):
            product = entry * (target_sum - entry)
            print(f"{entry} * {target_sum-entry} = {product}")
            return product

        else:
            seen[entry] = True


if __name__ == "__main__":
    entries = load_data("day1.in")
    print(twosum(2020, entries))

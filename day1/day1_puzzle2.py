from day1_lib import load_data


def threesum(target_sum: int, entries: list) -> int:
    """
    n log n + n^2
    """
    entries.sort()
    print(entries[:10])
    for i, entry in enumerate(entries):
        j = i + 1
        k = len(entries) - 1

        while j < k and i < j:
            temp_sum = entries[i] + entries[j] + entries[k]
            # print(temp_sum)
            if temp_sum > target_sum:
                k -= 1

            elif temp_sum < target_sum:
                j += 1

            elif temp_sum == target_sum:
                product = entries[i] * entries[j] * entries[k]
                print(f"{entries[i]} * {entries[j]} * {entries[k]} = {product}")
                return product


if __name__ == "__main__":
    entries = load_data("day1.in")
    print(threesum(2020, entries))

with open("day1.in", "rb") as fp:
    lines = [int(x) for x in fp.readlines()]

seen = dict()
SUM = 2020

for entry in lines:
    if seen.get(SUM - entry, None):
        print(f"{entry} * {SUM-entry} = {entry * (SUM - entry) }")

    else:
        seen[entry] = True

print(len(lines))

valid = 0
valids = []

with open("day2.in", "r") as fp:
    lines = fp.readlines()

for line in lines:
    line = line.strip()
    ch_count = 0
    invalidated = False

    p1, p3 = line.split(":")
    p1, p2 = p1.split(" ")

    nums = p1.split("-")
    pos1, pos2 = int(nums[0]), int(nums[1])

    print(p2)
    p3 = p3.strip()
    if int(p3[pos1 - 1] == p2) + int(p3[pos2 - 1] == p2) == 1:
        valid += 1
        valids.append((line, p3, p3[pos1 - 1], p3[pos2 - 2], (pos1, pos2))),

print(valid)
print(valids[:6])

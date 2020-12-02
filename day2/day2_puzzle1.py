invalid = 0
invalids = []
with open("day2.in", "r") as fp:
    lines = fp.readlines()
    ret = []
    for line in lines:
        line = line.strip()
        ch_count = 0
        invalidated = False

        p1, p3 = line.split(":")
        p1, p2 = p1.split(" ")

        nums = p1.split("-")
        min_c, max_c = int(nums[0]), int(nums[1])

        for ch in p3:
            if ch == p2:
                ch_count += 1
                if ch_count > max_c:
                    invalid += 1
                    invalids.append(line)
                    invalidated = True
                    break

        if ch_count < min_c and not invalidated:
            invalid += 1
            invalids.append(line)

    #     ret.append(dict(min=min_c, max=max_c, letter=p2, string=p3))

    # print(ret[3])
    print(invalids[:5])
    print(len(lines))
    print(len(lines) - invalid)

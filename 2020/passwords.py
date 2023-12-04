'https://adventofcode.com/2020/day/2'
import sys


def count_valid_range(passwords):
    ans = 0
    for x in passwords:
        b, u, c, p = x
        n = sum([int(c == x) for x in p])
        if b <= n <= u:
            ans += 1

    return ans


def count_valid_pos(passwords):
    ans = 0
    for x in passwords:
        b, u, c, p = x
        if int(p[b-1] == c) + int(p[u-1] == c) == 1:
            ans += 1

    return ans


with open(sys.argv[1]) as fp:
    passwords = []
    for line in fp.readlines():
        bounds, char, pw = line.strip().split(' ')
        l, h = bounds.split('-')
        c = char[0]
        passwords.append((int(l), int(h), c, pw))
    print(count_valid_pos(passwords))

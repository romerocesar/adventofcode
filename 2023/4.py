import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def numbers(line):
    logger.debug(f'{line=}')
    nums = line.split(':')[1]
    left, right = nums.split('|')
    logger.debug(f'{left=}')
    logger.debug(f'{right=}')
    w = set([int(x) for x in left.split(' ') if x.isnumeric()])
    m = set([int(x) for x in right.split(' ') if x.isnumeric()])
    return w, m


def part_two(fname):
    ans = 0
    cards = {}
    # read initial cards
    for i, line in enumerate(open(fname).readlines()):
        w, m = numbers(line.strip())
        both = w.intersection(m)
        cards[i+1] = (len(both), 1)  # (winning, copies)
    # process cards
    for c in cards:
        copies = cards[c][1]
        ans += copies
        winning = cards[c][0]
        logger.debug(f'processing card {c} with {winning=} {copies=}')
        for i in range(c+1, c+winning+1):
            if i not in cards:
                continue
            cards[i] = (cards[i][0], cards[i][1] + copies)
    return ans


def part_one(fname):
    ans = 0
    for line in open(fname).readlines():
        w, m = numbers(line.strip())
        both = w.intersection(m)
        if len(both) == 0:
            continue
        ans += 2**(len(both)-1)
    return ans


if __name__ == '__main__':
    logger.info(part_two(sys.argv[1]))

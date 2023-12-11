import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def extrapolate(numbers):
    logger.debug(f'extrapolate {numbers=}')
    ans = [numbers[-1]]
    row = numbers[:]
    while True:
        diffs = []
        for i in range(len(row)-1):
            diffs.append(row[i+1] - row[i])
        logger.debug(f'{diffs=}')
        if sum(diffs) == 0:
            return sum(ans)
        elif len(diffs) == 1:
            return 0
        ans.append(diffs[-1])
        row = diffs[:]


def part_one(fname):
    ans = 0
    history = []
    with open(fname) as fp:
        for line in fp.readlines():
            numbers = [int(x) for x in line.strip().split(' ')]
            logger.debug(f'{numbers=}')
            history.append(numbers)
    logger.debug(f'{history=}')
    for numbers in history:
        ans += extrapolate(numbers)

    return ans


def extrapolate_left(numbers):
    logger.debug(f'extrapolate left {numbers=}')
    ans = [numbers[0]]
    row = numbers[:]
    while True:
        diffs = []
        for i in range(len(row)-1):
            diffs.append(row[i+1] - row[i])
        logger.debug(f'{diffs=}')
        if sum(diffs) == 0:
            b = 0
            logger.debug(f'{ans=}')
            for r in reversed(ans):
                b = r - b
            logger.info(f'{b=}')
            return b

        ans.append(diffs[0])
        row = diffs[:]


def part_two(fname):
    ans = 0
    history = []
    with open(fname) as fp:
        for line in fp.readlines():
            numbers = [int(x) for x in line.strip().split(' ')]
            logger.debug(f'{numbers=}')
            history.append(numbers)
    logger.debug(f'{history=}')
    for numbers in history:
        ans += extrapolate_left(numbers)

    return ans


logger.info(f'Part one: {part_one(sys.argv[1])}')
logger.info(f'Part two: {part_two(sys.argv[1])}')

import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def part_one(fname):
    ans = 1
    races = []
    with open(fname) as fp:
        times = [int(x) for x in fp.readline().strip().split(':')[1].split(' ') if x.isnumeric()]
        distances = [int(x) for x in fp.readline().strip().split(':')[1].split(' ') if x.isnumeric()]
        races = zip(times, distances)

    for time, record in races:
        logger.debug(f'{time=} {record=}')
        win = 0
        for x in range(1, time//2+1):
            logger.debug(f'{x=}')
            if (time-x)*x > record:
                logger.debug(f'{(time-x)*x=} > {record=}')
                win += 2
        if time % 2 == 0:
            win -= 1
        ans *= win

    return ans


def part_two(fname):
    ans = 0
    with open(fname) as fp:
        time = int(fp.readline().strip().split(':')[1].replace(' ', ''))
        distance = int(fp.readline().strip().split(':')[1].replace(' ', ''))
    logger.debug(f'{time=} {distance=}')

    left, right = 1, time
    # bin search to find the first x where (time-x)*x > distance
    while left <= right:
        mid = (left + right) // 2
        logger.debug(f'{left=} {right=} {mid=}')
        if (time-mid)*mid > distance:
            right = mid - 1
        else:
            left = mid + 1
    ans = time - left - left + 1

    return ans


logger.info(f'Part one: {part_one(sys.argv[1])}')
logger.info(f'Part two: {part_two(sys.argv[1])}')

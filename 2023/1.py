import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def part_one():
    with open(sys.argv[1]) as fp:
        ans = 0
        for line in fp.readlines():
            logger.debug(line)
            a, b = None, None
            for c in line.strip():
                if c.isdigit():
                    if a is None:
                        a = c
                    b = c
            val = int(a+b)
            ans += val
        logger.info(ans)


def part_two():
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    wtod = {w: str(i+1) for i, w in enumerate(numbers[:9])}
    with open(sys.argv[1]) as fp:
        ans = 0
        for line in fp.readlines():
            logger.debug(line.strip())
            firstpos, lastpos = len(line), -1
            first, last = None, None
            for num in numbers:
                try:
                    left = line.index(num)
                    right = line.rindex(num)
                    if firstpos > left:
                        firstpos = left
                        first = num
                    if lastpos < right:
                        lastpos = right
                        last = num
                except ValueError as e:
                    continue
            logger.debug(f'{first=} {last=}')
            val = int(wtod.get(first, first)+wtod.get(last, last))
            ans += val
        logger.info(ans)


part_two()

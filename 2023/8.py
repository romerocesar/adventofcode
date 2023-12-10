import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def part_one(fname):
    g = {}
    with open(fname) as fp:
        table = str.maketrans('LR', '01')
        directions = fp.readline().strip().translate(table)
        directions = [int(x) for x in directions]
        logger.debug(f'{directions=}')
        fp.readline()
        for line in fp.readlines():
            pattern = r'(\w+)\s=\s\((\w+),\s(\w+)\)'
            m = re.match(pattern, line.strip())
            k, l, r = m.groups()
            g[k] = (l, r)

    logger.debug(f'{g=}')
    node = 'AAA'
    pos = 0
    steps = 0
    while node != 'ZZZ':
        node = g[node][directions[pos]]
        pos = (pos + 1) % len(directions)
        steps += 1

    return steps


logger.info(f'Part one: {part_one(sys.argv[1])}')

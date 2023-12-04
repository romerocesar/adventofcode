import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def samples(cubes):
    for sample in cubes.split(';'):
        t = sample.split(',')
        r, g, b = 0, 0, 0
        for c in t:
            c = c.strip()
            if 'red' in c:
                r = int(c.split(' ')[0])
            elif 'green' in c:
                g = int(c.split(' ')[0])
            elif 'blue' in c:
                logger.debug(c.split(' '))
                b = int(c.split(' ')[0])
        yield int(r), int(g), int(b)


def parse(line):
    game, cubes = line.split(':')
    game = int(game.split(' ')[-1])
    return game, cubes


def part_one(fname):
    limit = 12, 13, 14
    ans = 0
    with open(fname) as fp:
        for line in fp.readlines():
            game, cubes = parse(line.strip())
            for r, g, b in samples(cubes):
                if r > limit[0] or g > limit[1] or b > limit[2]:
                    break
            else:
                logger.debug(f'adding {game=}')
                ans += game
    return ans


def part_two(fname):
    ans = 0
    with open(fname) as fp:
        for line in fp.readlines():
            game, cubes = parse(line.strip())
            maxr, maxg, maxb = 0, 0, 0
            for r, g, b in samples(cubes):
                maxr = max(maxr, r)
                maxg = max(maxg, g)
                maxb = max(maxb, b)
            ans += maxr*maxg*maxb
    return ans


if __name__ == '__main__':
    logger.info(part_two(sys.argv[1]))

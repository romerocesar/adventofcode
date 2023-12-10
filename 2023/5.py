import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def part_one(fname):
    ans = float('inf')
    all_maps = []
    with open(fname) as fp:
        line = fp.readline().strip()
        seeds = [int(x) for x in line.split(':')[1].split(' ') if x.isnumeric()]
        logger.debug(f'{seeds=}')
        fp.readline()  # skip blank line
        for i in range(7):
            tmap = []
            fp.readline()  # skip header
            while line := fp.readline().strip():
                if not line:
                    break
                d, s, r = [int(x) for x in line.strip().split(' ')]
                tmap.append((d, s, r))
            all_maps.append(tmap)
        logger.debug(f'{all_maps=}')

    for seed in seeds:
        logger.debug(f'{seed=}')
        location = seed
        for m in all_maps:
            for d, s, r in m:
                if location in range(s, s+r):
                    location = d + location - s
                    break
        logger.debug(f'{seed=} {location=}')
        ans = min(ans, location)

    return ans


def part_two(fname):
    ans = float('inf')
    all_maps = []
    with open(fname) as fp:
        line = fp.readline().strip()
        seeds = [int(x) for x in line.split(':')[1].split(' ') if x.isnumeric()]
        logger.debug(f'{seeds=}')
        fp.readline()  # skip blank line
        for i in range(7):
            tmap = []
            fp.readline()  # skip header
            while line := fp.readline().strip():
                if not line:
                    break
                d, s, r = [int(x) for x in line.strip().split(' ')]
                tmap.append((d, s, r))
            all_maps.append(tmap)
        logger.debug(f'{all_maps=}')

    pairs = [(seeds[i], seeds[i+1]) for i in range(len(seeds)-1)]
    all_seeds = (x for x in range(s, s+r) for s, r in pairs)
    for seed in all_seeds:
        logger.debug(f'{seed=}')
        location = seed
        for m in all_maps:
            for d, s, r in m:
                if location in range(s, s+r):
                    location = d + location - s
                    break
        logger.debug(f'{seed=} {location=}')
        ans = min(ans, location)

    return ans


logger.info(part_two(sys.argv[1]))

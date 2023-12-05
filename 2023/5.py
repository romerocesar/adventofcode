import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def init_map(fp):
    ans = {}
    while line := fp.readline().strip():
        if not line:
            break
        d, s, r = [int(x) for x in line.strip().split(' ')]
        for i in range(r):
            ans[s+i] = d+i
    return ans


def part_one(fname):
    ans = 0
    with open(fname) as fp:
        line = fp.readline().strip()
        seeds = [int(x) for x in line.split(':')[1].split(' ') if x.isnumeric()]
        logger.debug(f'{seeds=}')
        fp.readline()  # skip blank line
        fp.readline()  # skip seed to soil
        s2s = init_map(fp)
        logger.debug(f'{s2s=}')
        fp.readline()  # skip soil to fertilizer header
        s2f = init_map(fp)
        logger.debug(f'{s2f=}')
        fp.readline()  # skip fertilizer to water header
        f2w = init_map(fp)
        logger.debug(f'{f2w=}')
        fp.readline()  # skip water to light header
        w2l = init_map(fp)
        logger.debug(f'{w2l=}')
        fp.readline()  # skip light to temperature header
        l2t = init_map(fp)
        logger.debug(f'{l2t=}')
        fp.readline()  # skip temperature to humidity header
        t2h = init_map(fp)
        logger.debug(f'{t2h=}')
        fp.readline()  # skip humidity to location header
        h2l = init_map(fp)
        logger.debug(f'{h2l=}')

    for seed in seeds:
        logger.debug(f'{seed=}')
        soil = s2s[seed]
        logger.debug(f'{soil=}')
        fertilizer = s2f[soil]
        logger.debug(f'{fertilizer=}')
        water = f2w[fertilizer]
        logger.debug(f'{water=}')
        light = w2l[water]
        logger.debug(f'{light=}')
        temperature = l2t[light]
        logger.debug(f'{temperature=}')
        humidity = t2h[temperature]
        logger.debug(f'{humidity=}')
        location = h2l[humidity]
        logger.debug(f'{location=}')
        ans += location
    return ans


logger.info(part_one(sys.argv[1]))

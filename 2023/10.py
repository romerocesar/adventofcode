import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('advent')


def neighbors(node, g):
    logger.debug(f'{node=}')
    x = node[0]
    y = node[1]
    d = node[2]
    match g[x][y]:
        case '|':
            yield (x-1, y, d+1)
            yield (x+1, y, d+1)
        case '-':
            yield (x, y-1, d+1)
            yield (x, y+1, d+1)
        case 'L':
            yield (node[0]-1, node[1], node[2]+1)
            yield (node[0], node[1]+1, node[2]+1)
        case 'J':
            yield (node[0]-1, node[1], node[2]+1)
            yield (node[0], node[1]-1, node[2]+1)
        case '7':
            yield (node[0]+1, node[1], node[2]+1)
            yield (node[0], node[1]-1, node[2]+1)
        case 'F':
            yield (node[0]+1, node[1], node[2]+1)
            yield (node[0], node[1]+1, node[2]+1)
        case '.':
            return []
        case 'S':
            if x-1 >= 0 and g[x-1][y] in '|7F':
                yield (x-1, y, d+1)
            if x+1 < len(g) and g[x+1][y] in '|JL':
                yield (x+1, y, d+1)
            if y-1 >= 0 and g[x][y-1] in '-FL':
                yield (x, y-1, d+1)
            if y+1 < len(g[0]) and g[x][y+1] in '-J7':
                yield (x, y+1, d+1)


def bfs(g):
    # find the start
    ans = -1
    start = None
    for i, row in enumerate(g):
        if 'S' in row:
            start = (i, row.index('S'), 0)
            break
    logger.debug(f'{start=}')
    q = [start]
    seen = set()
    while q:
        node = q.pop(0)
        # check both directions
        for n in neighbors(node, g):
            if n[:2] in seen:
                continue
            logger.debug(f'{n=}')
            q.append(n)
            seen.add(n[:2])
            ans = max(ans, n[2])
        logger.debug(f'{q=}')

    return ans


def part_one(fname):
    g = []
    with open(fname) as fp:
        for line in fp.readlines():
            line = line.strip()
            g.append(line)
    logger.info(f'parsed {g}')
    ans = bfs(g)
    return ans


logger.info(part_one(sys.argv[1]))

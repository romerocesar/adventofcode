import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def neighbors(row, col, schematic):
    logger.debug(f'neighbors {row=} {col=} {schematic[row][col]=}')
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if 0 <= i < len(schematic) and 0 <= j < len(schematic[i]):
                logger.info(f'neighbors {row=} {col=} {i=} {j=} {schematic[i][j]=}')
                yield i, j


def number(row, col, schematic):
    logger.debug(f'number {row=} {col=} {schematic[row][col]=}')
    start = col
    while start > 0 and schematic[row][start-1].isnumeric():
        start -= 1
    end = col
    while end < len(schematic[row]) and schematic[row][end].isnumeric():
        end += 1
    logger.info(f'number {row=} {col=} {start=} {end=} {schematic[row][start:end]=}')
    return start, end, int(schematic[row][start:end])


def part_one(fname):
    ans = 0
    schematic = []
    included = set()
    with open(fname) as fp:
        for line in fp.readlines():
            schematic.append(line.strip())
    logger.debug(schematic)
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] == '.' or schematic[row][col].isnumeric():
                continue
            for i, j in neighbors(row, col, schematic):
                if schematic[i][j].isnumeric():
                    n = number(i, j, schematic)
                    if n not in included:
                        ans += n[2]
                        included.add(n)
    return ans


if __name__ == '__main__':
    logger.info(part_one(sys.argv[1]))

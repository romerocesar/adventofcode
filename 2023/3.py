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
    return start, int(schematic[row][start:end])


def part_two(fname):
    ans = 0
    schematic = []
    with open(fname) as fp:
        for line in fp.readlines():
            schematic.append(line.strip())
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] != '*':
                continue
            part_numbers = []
            included = set()
            for i, j in neighbors(row, col, schematic):
                if schematic[i][j].isnumeric():
                    s, n = number(i, j, schematic)
                    if (i, s) in included:
                        continue
                    part_numbers.append(n)
                    included.add((i, s))
                    logger.debug(f'{part_numbers=}')
            if len(part_numbers) == 2:
                logger.debug(f'{part_numbers=}')
                gear_ratio = part_numbers[0] * part_numbers[1]
                ans += gear_ratio
    return ans


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
                    s, n = number(i, j, schematic)
                    if (i, s) not in included:
                        ans += n
                        included.add((i, s))
    return ans


if __name__ == '__main__':
    logger.info(part_two(sys.argv[1]))

from collections import Counter
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('adventofcode')


def hand_type(hand):
    logger.debug(f'{hand=}')
    counts = Counter(hand['c'])
    logger.debug(f'{counts=}')
    if len(counts) == 1:
        return 7
    a, b = list(sorted(counts.values(), reverse=True))[:2]
    logger.debug(f'{a=} {b=}')
    if a == 5:
        return 7
    elif a == 4:
        return 6
    elif a == 3 and b == 2:
        return 5
    elif a == 3:
        return 4
    elif a == 2 and b == 2:
        return 3
    elif a == 2:
        return 2
    else:
        return 1


def add_rank(hands):
    table = str.maketrans('TJQKA', 'ABCDE')
    for i, hand in enumerate(sorted(hands, key=lambda x: (x['t'], x['c'].translate(table)))):
        hand['r'] = i+1


def part_one(fname):
    ans = 0
    hands = []
    with open(fname) as fp:
        for line in fp.readlines():
            cards, bid = line.strip().split(' ')
            bid = int(bid)
            hands.append({'c': cards, 'b': bid})

    for hand in hands:
        hand['t'] = hand_type(hand)

    add_rank(hands)

    for hand in hands:
        logger.debug(f'{hand=}')
        ans += hand['b'] * hand['r']
    return ans


def joker_hand_type(hand):
    logger.debug(f'{hand=}')
    cards = hand['c']
    counts = Counter(cards)
    if len(counts) == 1:
        return 7

    if 'J' in cards:
        # replace J with the most common non J card
        counts = [c[0] for c in counts.most_common() if c[0] != 'J']
        mode = counts[0]
        logger.debug(f'{mode=}')
        logger.debug(f'{cards=}')
        cards = cards.replace('J', mode)
        logger.debug(f'{cards=}')
        counts = Counter(cards)

    if len(counts) == 1:
        return 7

    a, b = list(sorted(counts.values(), reverse=True))[:2]
    logger.debug(f'{a=} {b=}')
    if a == 4:
        return 6
    elif a == 3 and b == 2:
        return 5
    elif a == 3:
        return 4
    elif a == 2 and b == 2:
        return 3
    elif a == 2:
        return 2
    else:
        return 1


def joker_add_rank(hands):
    table = str.maketrans('TJQKA', 'A1CDE')
    for i, hand in enumerate(sorted(hands, key=lambda x: (x['t'], x['c'].translate(table)))):
        hand['r'] = i+1


def part_two(fname):
    ans = 0
    hands = []
    with open(fname) as fp:
        for line in fp.readlines():
            cards, bid = line.strip().split(' ')
            bid = int(bid)
            hands.append({'c': cards, 'b': bid})

    for hand in hands:
        hand['t'] = joker_hand_type(hand)

    joker_add_rank(hands)

    for hand in sorted(hands, key=lambda x: x['r']):
        logger.debug(f'{hand=}')
        ans += hand['b'] * hand['r']
    return ans


logger.info(f'Part one: {part_one(sys.argv[1])}')
logger.info(f'Part two: {part_two(sys.argv[1])}')

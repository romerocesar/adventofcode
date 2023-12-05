import logging
import re
import sys

logger = logging.getLogger('advent')
logging.basicConfig(level=logging.DEBUG)


class Monkey:

    def __init__(self):
        self.n = 0
        self.inspections = 0
        self.items = None
        self.operation = None
        self.test = [0, 0, 0]

    def inspect(self, item):
        self.inspections += 1
        value = item if self.operation[1] == 'old' else int(self.operation[1])
        item = item*value if self.operation[0] == '*' else item+value
        return item

    def toss(self, item):
        if item % self.test[0]:
            return self.test[2]
        else:
            return self.test[1]

    def __repr__(self):
        return str(self.__dict__)


def parse(fname):
    monkeys = []
    with open(fname) as fp:
        monkey = Monkey()
        for line in fp.readlines():
            line = line.strip()
            logger.debug(f'parsing {line=}')
            if not line:
                monkeys.append(monkey)
                monkey = Monkey()
            elif m := re.match(r'Monkey (\d+):', line):
                monkey.n = int(m.group(1))
            elif m := re.match(r'Starting items: (.+)', line):
                logger.debug('parsing items')
                monkey.items = [int(x) for x in m.group(1).split(',')]
                logger.debug(monkey)
            elif m := re.match(r'Operation: new = old (.) (\d+|old)', line):
                o = m.group(1)
                v = m.group(2)
                monkey.operation = (o, v)
            elif m := re.match(r'Test: divisible by (\d+)', line):
                d = int(m.group(1))
                monkey.test[0] = d
            elif m := re.match(r'If true:.+?(\d+)$', line):
                t = int(m.group(1))
                monkey.test[1] = t
            elif m := re.match(r'If false:.+?(\d+)$', line):
                f = int(m.group(1))
                monkey.test[2] = f
        else:
            monkeys.append(monkey)

    return monkeys


def simulate(monkeys, rounds=20):
    for r in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                # logger.debug(f'{r=} {monkey.n=} {item=}')
                item = monkey.inspect(item)
                dest = monkey.toss(item)
                # logger.debug(f'tossing {item=} to monkey {dest}')
                monkeys[dest].items.append(item)
            monkey.items.clear()


def monkey_business(monkeys, rounds=20):
    simulate(monkeys, rounds=rounds)
    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    logger.debug(f'{monkeys=}')
    return monkeys[0].inspections*monkeys[1].inspections


monkeys = parse(sys.argv[1])
logger.info(monkeys)
logger.info(monkey_business(monkeys, rounds=10000))

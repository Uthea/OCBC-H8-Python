def conditional():
    # Conditionals , Control Flow, Looping

    x = 0
    y = 5

    if x < y:
        print('yes x < y')

    if y < x:
        print('yes y < x')

    if x:
        print('yes x')

    if y:
        print('yes y')

    if 'aul' in 'grault':
        print('yes ault in grault')

    # 2
    weather = 'nice'
    # weather = 'cloudy'

    if weather == 'nice':
        print('Mow the lawn')
        print('Weed the garden')
        print('Take the dog for a walk')

    # 3
    if 'qux' in ['bar', 'baz', 'qux']:
        print('Expression was true')
        print('Executing statement in suite')
        print('...')
        print('Done')

    # 4
    weather = 'cloudy'

    if weather == 'nice':
        print('Mow the lawn')
        print('Weed the garden')
        print('Take the dog for a walk')
    else:
        print('Read a book')
        print('Watch the movies')

    # Ternary operator
    lottery_num = 80
    prize = 'box1' if lottery_num < 100 else 'box2'

    print(prize)


def loops():
    n = 5
    while n > 0:
        n -= 1
        print(n)


if __name__ == '__main__':
    loops()

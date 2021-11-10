
def my_generator():
    print('Inside my generator')
    yield 'a'
    yield 'b'
    yield 'c'

if __name__ == '__main__':
    print(my_generator())
    print(list(my_generator()))

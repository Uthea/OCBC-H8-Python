from book import book

def save_personal_info(name, age=18):
    print('name', name)
    print('age', age)


def buy(customer_name,address, *items):
    print(customer_name)
    print(address)
    print(items)

def print_boolean(answer):
    print('The answer is', answer)


def calculate_rect(length, width):
    '''This function is used to calculate area of rectangle'''
    print('Area : ', length * width)


if __name__ == '__main__':
    # save_personal_info(37, 'adi')
    # save_personal_info(age=27, name='lucy')

    buy('roy', 'chocolate bar')
    buy('tia', 'wheet', 'flour', 'chocolate bar')
    # print_boolean(True)
    # calculate_rect(10, 20)

    # sum = lambda num1, num2: num1 + num2
    # print(sum(1, 2))
    #
    # calculated_rect_area = lambda length, width: length * width

    print(book)
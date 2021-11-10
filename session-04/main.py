def os_interaction():
    assert ('win32' in sys.platform), "This code runs on windows"
    assert ('linux' in sys.platform), "Function can only run on linux"
    print('do something')


if __name__ == '__main__':
    # file = open('Hack8_Sample_Text.txt')
    # # print(file.read())
    # file.close()
    #
    # try:
    #     file = open('Hack8_Sample_Text100.txt')
    #     print('opening the file')
    # finally:
    #     print('closing the file')
    #     file.close()

    # with open("sample.txt", 'w', encoding='utf-8') as f:
    #     f.write("my first file\n")
    #     f.write("the file\n")
    #     f.write("contains three lines\n")

    # f = open('sample.txt', 'r', encoding='utf-8')
    # data = f.read(4)
    # print(data)

    with open("sample.txt", 'r', encoding='utf-8') as f:
        # data = f.read(4)
        # print(data)
        # data = f.read(4)
        # print(data)
        # print(f.tell())
        # f.seek(0)
        #
        # data = f.read(3)
        # print(data)

        # f.seek(0)
        #
        # for line in f:
        #     print(line)

        # f.seek(0)
        # data = f.readline()
        # print(data)

        import sys

        try:
            os_interaction()
        except:
            print('something is wrong')



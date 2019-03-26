def create_file():
    f = open('test.txt', mode='w')  # 如果文件不存在，会创建，存在则会覆盖
    for i in range(10):
        f.write("IT technology has giant power")
        f.write('I love China' + str(i) + '\n')
    f.close()


def append_file():
    f = open('test.txt', mode='w')
    dict1 = {'country': ['china', 'canada', 'america'], 'income': [12, 32, 23]}
    for key in dict1:
        dict1[key].insert(0, key)
        f.write(str(tuple(dict1[key]))) # 只能写str？
        f.write('\n')


append_file()

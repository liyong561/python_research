import math


def rotate_list(ls, idx):
    length = len(ls)
    ls1 = ls.copy()
    ls1[0:length - idx] = ls[idx:length]
    ls1[length - idx:length] = ls[0:idx]
    return ls1


def read_table(file):
    data = {}
    # i = 0;第一个字段为key，使用dict,很方便访问
    with open(file) as f:
        for line in f:  # 直接是line
            record = line.strip()
            if record.startswith('#'):  # 跳过注释。
                continue
            '''
            eval()这个函数非常的神奇，读取这种数据，简直不要太方便
            把字符串变成了元组，而元组和列表的转换非常方便。但是元组的修改不如列表方便。（12，，，12，，）
            '''
            ls = list(eval(record))
            data[ls[0]] = ls  # add item to the dictionary,去掉制表符，换行符。
    return data


def get_road_id(ls, ls1):
    for x in ls:
        if x != -1:
            for y in ls1:
                if x == y:
                    return x


def number_position(theta_rel):
    sin = int(math.sin(theta_rel))
    cos = int(math.cos(theta_rel))
    if cos == 0:
        if sin == 1:
            return 1
        else:
            return 3
    else:
        if cos == 1:
            return 0
        else:
            return 2


def new_number_position(number, x, y, l):
    if number == 0:
        return [x + l, y]
    if number == 1:
        return [x, y + l]
    if number == 2:
        return [x - l, y]
    if number == 3:
        return [x, y - l]


def build_route_map(road_data, cross_data):
    route_map = dict()

    cross_id = cross_data[1][0]
    start_item = dict()
    start_item['cross_id_pos'] = [0, 0, cross_id]
    start_item['connect'] = [-1, -1, -1, -1]
    # 确立坐标的方向：
    cross_road__list = cross_data[cross_id][1:]
    # print(len(cross_road__list))

    next_cross_list = []
    next_road_list = []
    for road_i in range(len(cross_road__list)):
        road_id = cross_road__list[road_i]
        next_road_list.append(road_id)

        # 该路不存在，或者该方向不通。
        if road_id == -1 or road_data[road_id][6] == 0 and road_data[road_id][4] != cross_id:
            # start_item['connect'][road_i] = -1
            print("no road")
            continue
        # 如果可通，则将该位置记录下来,这里涉及起始位置的选择
        else:

            next_cross_id = road_data[road_id][5] if road_data[road_id][5] != cross_id else road_data[road_id][4]

            # 该cross已经访问,不需要定位了
            if next_cross_id in route_map:
                start_item['connect'][road_i] = next_cross_id
                continue

            # 该节点的未访问的邻接节点
            next_cross_item = dict()

            # 对start-next的域进行完善
            start_item['connect'][road_i] = next_cross_id

            road_length = road_data[road_id][1]
            co_x = start_item['cross_id_pos'][0]
            co_y = start_item['cross_id_pos'][1]
            new_co_x = 0
            new_co_y = 0
            # 注意这个是顺序排列的，顺序的第一个作为x轴
            if road_i == 0:
                new_co_x = co_x + road_length
                new_co_y = co_y

            if road_i == 1:
                new_co_x = co_x
                new_co_y = co_y - road_length

            if road_i == 2:
                new_co_x = co_x - road_length
                new_co_y = co_y

            if road_i == 3:
                new_co_x = co_x
                new_co_y = co_y + road_length

            next_cross_item['cross_id_pos'] = [new_co_x, new_co_y, next_cross_id]
            # 先确定它的类型。
            next_cross_item['connect'] = [-1, -1, -1, -1]
            next_cross_list.append(next_cross_item)

    route_map[cross_id] = start_item

    for i in range(len(next_cross_list)):
        visit_graph(next_cross_list[i], start_item, next_road_list[i], cross_data, road_data, route_map)

    return route_map


def search(start, end, start_time, car_id, cross_data, road_data, car_route):
    # 所有路段的起点为start的路段(正向),或者终点是start，且为双行道

    next_cross_list = []
    for road_id, road_item in road_data.items():

        if road_item[6] == 0:
            if start == road_item[4]:
                next_cross_list.append(road_item[5])
                continue
        if start == road_item[4] or start == road_item[5]:
            next_cross_list.append(road_item[5])

    # 是否已到达终点。
    if end in next_cross_list:
        car_route[car_id].appedn(end)
        return
    '''
    for next_cross in next_cross_list:

        # 如果已到达终点，python使用in的更简单的方法
        if next_cross == end:
            car_route[car_id].append(next_cross)
    '''
    # 使用以存在的路径不一定是最短的，并且可能会造成拥堵。
    for next_cross in next_cross_list:
        search(next_cross, end, start_time, car_id, cross_data, road_data, car_route)


def visit_graph(start_item, pre_item, start_road_id, cross_data, road_data, route_map):
    # 不重复访问
    if start_item['cross_id_pos'][2] in route_map:
        return
    co_x = start_item['cross_id_pos'][0]
    co_y = start_item['cross_id_pos'][1]
    cross_id = start_item['cross_id_pos'][2]

    # 找到原来的路口，并以该路口为顺时针的第一个路口
    cross_road__list_init = cross_data[cross_id][1:]
    start_road_id_idx = cross_road__list_init.index(start_road_id)
    cross_road__list = rotate_list(cross_road__list_init, start_road_id_idx)[1:]
    # print(len(cross_road__list)) 3

    co_x1 = pre_item['cross_id_pos'][0]
    co_y1 = pre_item['cross_id_pos'][1]

    if cross_id == 2:
        print(cross_road__list)

    # 旧点在新点的哪个方位,co_x为参考点
    if co_x == co_x1:
        if co_y1 < co_y:
            theta = -math.pi / 2
            position = 3
        else:
            theta = math.pi / 2
            position = 1
    else:
        if co_x1 < co_x:
            theta = -math.pi
            position = 2
        else:
            theta = 0
            position = 0

    if road_data[start_road_id][6] == 0 and road_data[start_road_id][4] != cross_id:
        start_item['connect'][position] = -1
    else:
        next_cross_id = road_data[start_road_id][5] if road_data[start_road_id][5] != cross_id else \
            road_data[start_road_id][4]
        start_item['connect'][position] = next_cross_id

    # print(len(cross_road__list))

    next_cross_list = []
    next_road_list = []

    # 对剩下的3个点定位
    for road_i in range(len(cross_road__list)):
        road_id = cross_road__list[road_i]
        theta_rel = theta - (road_i + 1) * math.pi / 2
        position = number_position(theta_rel)

        # 该路不存在，或者该方向不通。
        if road_id == -1 or road_data[road_id][6] == 0 and road_data[road_id][4] != cross_id:
            start_item['connect'][position] = -1
            continue

        # 如果可通，则将该位置记录下来,这里涉及起始位置的选择
        else:
            next_cross_id = road_data[road_id][5] if road_data[road_id][5] != cross_id else \
                road_data[road_id][4]

            # 该路口已经在地图中，则不应该入栈，否则就是重复访问
            if next_cross_id in route_map:
                start_item['connect'][position] = next_cross_id
                continue

            road_length = road_data[road_id][1]

            # 对start-next的域进行完善
            start_item['connect'][position] = next_cross_id
            # 该节点的未访问的邻接节点
            next_cross_item = dict()
            next_cross_item['cross_id_pos'] = new_number_position(position, co_x, co_y, road_length)
            next_cross_item['cross_id_pos'].append(next_cross_id)
            next_cross_item['connect'] = [-1, -1, -1, -1]
            next_cross_list.append(next_cross_item)
            next_road_list.append(road_id)

    route_map[cross_id] = start_item

    # dfs遍历
    for i in range(len(next_cross_list)):
        visit_graph(next_cross_list[i], start_item, next_road_list[i], cross_data, road_data, route_map)


def build_route(road_data, cross_data, car_data):
    my_map = build_route_map(road_data, cross_data)
    car_route = dict()

    for car_item in car_data.values():
        # route中存储的路径信息，my_map中存在的是路口信息，注意转换
        car_id = car_item[0]
        start_time = car_item[4]

        # 要构造的每辆车的路径数据
        car_route[car_id] = [car_id, start_time]

        start_cross_id = car_item[1]
        end_cross_id = car_item[2]

        sx, sy = my_map[start_cross_id]['cross_id_pos'][:2]
        ex, ey = my_map[end_cross_id]['cross_id_pos'][:2]
        flag = straight_route(sx, sy, ex, ey, start_cross_id, cross_data, my_map)
        if flag != 1:
            for road_id in flag:
                car_route[car_id].append(road_id)
            continue

        cross_visited = dict()
        for cross_id in cross_data:
            cross_visited[cross_id] = 0

        cross_visited[start_cross_id] = 1

        path = []
        all_path = []
        curve_route1(start_cross_id, end_cross_id, cross_data, my_map, cross_visited, path, all_path)
        all_path.sort(key=lambda x: len(x))
        short_path = all_path[0]
        for road_id in short_path:
            car_route[car_id].append(road_id)

    # f = open('car_route_test.txt',mode='w')
    # f.write(str(car_route))
    return car_route


def straight_route(sx, sy, ex, ey, start_cross_id, cross_data, my_map):
    # return 1表示路径有问题
    road_list = []
    start_next_cross_list = my_map[start_cross_id]['connect']
    while sx < ex:

        # next_cross_list是否一定存在？如果构建的地图是一个矩形，就符合，如果不是，比如凹形就不符合。
        next_cross_id = start_next_cross_list[0]

        # 遇到这种情况，更换路径搜索算法，从最初的起始点开始。
        if next_cross_id == -1:
            return 1
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = get_road_id(r1, r2)
        road_list.append(road_id)

        # 新一轮的迭代
        start_cross_id = next_cross_id
        start_next_cross_list = my_map[start_cross_id]['connect']
        sx, sy = my_map[next_cross_id]['cross_id_pos'][:2]
    while sx > ex:
        next_cross_id = start_next_cross_list[2]

        if next_cross_id == -1:
            return 1
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = get_road_id(r1, r2)
        road_list.append(road_id)

        # 新一轮的迭代
        start_cross_id = next_cross_id
        start_next_cross_list = my_map[start_cross_id]['connect']
        sx, sy = my_map[next_cross_id]['cross_id_pos'][:2]
    # 起始点在目的点下方
    while sy < ey:
        next_cross_id = start_next_cross_list[1]

        if next_cross_id == -1:
            return 1
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = get_road_id(r1, r2)
        road_list.append(road_id)

        # 新一轮的迭代
        start_cross_id = next_cross_id
        start_next_cross_list = my_map[start_cross_id]['connect']
        sx, sy = my_map[next_cross_id]['cross_id_pos'][:2]

    while sy > ey:
        next_cross_id = start_next_cross_list[3]
        if next_cross_id == -1:
            return 1
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = get_road_id(r1, r2)
        road_list.append(road_id)

        # 新一轮的迭代
        start_cross_id = next_cross_id
        start_next_cross_list = my_map[start_cross_id]['connect']
        sx, sy = my_map[next_cross_id]['cross_id_pos'][:2]

    return road_list


# 这是一个遍历算法的原型，遍历的时候使用枝减方法，并且使用递归。
# path是我要想得到的结果。
def curve_route1(start_cross_id, end_cross_id, cross_data, my_map, cross_visited, path, all_path):
    # 只有到达终点，才加入path中
    if start_cross_id == end_cross_id:
        all_path.append(path.copy())
        return path

    next_cross_list = my_map[start_cross_id]['connect']
    next_cross_list = [x for x in next_cross_list if x != -1]
    next_cross_list = [x for x in next_cross_list if cross_visited[x] == 0]

    if len(next_cross_list) == 0:
        return 1

    for next_cross_id in next_cross_list:
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = get_road_id(r1, r2)
        path.append(road_id)
        cross_visited[start_cross_id] = 1

        curve_route1(next_cross_id, end_cross_id, cross_data, my_map, cross_visited, path, all_path)
        path.pop()


def dispatch_on_road(t, car_data, route_data, road_data, road_with_car):
    # 先获取t-1时刻的状态。从1开始，0时刻都在原地
    # 太多的车上路，就会死锁。
    counter = 0
    car_item_start_list = [car_item1 for car_item1 in car_data.values() if car_item1[4] == t]  # 遍历字典,和列表的差异
    # 车到达计划出发时间，可以出发，也可以等，简单模型中，直接出发,这样会堵塞。

    print('car_number' + str(counter))
    for car_item in car_item_start_list:

        # 更距时间简单调节车流量
        if t < 20 or t > 400:
            if counter > 10:
                break

        else:
            if counter > 20:
                break

        car_id = car_item[0]
        road_id = route_data[car_id][2]  # 车辆第一段路id，

        start = road_data[road_id][4]  # 这条道路的正向起点
        direction = 0 if start == car_item[1] else 1  # 0表示同向

        s = min(car_item[3], road_data[road_id][2])  # 可行的最大速度，还要看是否能走。不堵塞。

        if road_id not in road_with_car:  # 该道路没有车辆时

            # 在这里构造了road_with_car数据
            road_with_car[road_id] = []
            first_record = [car_item[0], s, car_item[3], 0, direction, 1]

            counter += 1
            road_with_car[road_id].append(first_record)
            route_data[car_id][1] = t
            # 上路后，从上路的列表中移除
            car_item_start_list.remove(car_item)
            print(str(car_id) + '开始上路,一点都不拥堵')
            continue

        road_item = road_with_car[road_id]  # 获得道路的车况信息.
        channel = road_data[road_id][3]

        for channel_i in range(channel):

            #  print("channel:"+str(channel_i))
            # 字段的类型都是之前定义好的，更改一点，就可能影响整个程序。road_item是一个列表中嵌套列表。
            if len(road_item) == 0:
                channel_with_car = []
            else:
                channel_with_car = [record for record in road_item if
                                    record[3] == channel_i and record[4] == direction]
            if len(channel_with_car) == 0:  # 车道上没有车辆
                record = [car_item[0], s, car_item[3], channel_i, direction, 1]
                counter += 1
                road_with_car[road_id].append(record)
                route_data[car_id][1] = t
                car_item_start_list.remove(car_item)
                print(str(car_id) + '开始上路,车道不拥堵')  # 考虑，这个要跳出多重循环
                break

            # print('cc:' + str(channel_with_car))

            # 车道上有车
            channel_with_car.sort(key=lambda x: x[1])
            record = channel_with_car[0]

            if record[1] > 2 * s:
                # 如果有空就可以上路,车不是一个质点，要确定是以车头为坐标，还是以车尾为坐标,最终商定以车头为坐标。尽量按照最大速度出发。
                new_record = [car_item[0], s, car_item[3], channel_i, direction, 1]  # 符合条件，上路。
                counter += 1
                road_with_car[road_id].append(new_record)
                route_data[car_id][1] = t
                car_item_start_list.remove(car_item)
                print(str(car_id) + '开始上路, 车有点多')
                break

    for car_item in car_item_start_list:
        # 什么情况下回延迟上路？
        if car_item[3] >= 6:
            car_item[4] += 4
        else:
            car_item[4] += 9

def dispatch():
    road_data = read_table('road.txt')
    cross_data = read_table('cross.txt')
    car_data = read_table('car.txt')
    route_data = build_route(road_data, cross_data, car_data)
    road_with_car = dict()
    dispatch_on_road(1, car_data, route_data, road_data, road_with_car)

    # t为调度的总时间
    t = 2
    while 1:

        das.dispatch_car_run(cross_data, road_data, route_data, road_with_car)
        dor.dispatch_on_road(t, car_data, route_data, road_data, road_with_car)
        print(road_with_car)
        flag = True
        for road_id in road_data:
            if road_id in road_with_car:
                if len(road_with_car[road_id]) > 0:
                    flag = False
                    break
        if flag:
            break

        t += 1
        if t == 1000:
            print('500次了')
        print(t)

    print("调度完毕")
    return t
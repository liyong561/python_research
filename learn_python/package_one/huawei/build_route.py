import package_one.huawei.build_map as build_map
import package_one.huawei.utils as utils

'''
变成在直角坐标系中搜索路径，这将会变得非常简单，要注意尽量避免拥堵。
先使用最简单的算法：先x,后y.
 [1002, 1, 513, 504, 518, 508, 509, 524]  # 出发时间在调度时确定，然后插入列表中。
map的结构，{cross_id_1:value1,cross_id_2,value2}
value的结构，{cross_id_pos:[100,1200,cs0],connect:[cs2,cs3,cs4,cs5]},在坐标系的顺序依次是x轴，然后逆时针
'''


# 不用重复读入数据
def build_route(road_data, cross_data, car_data):
    my_map = build_map.build_route_map(road_data, cross_data)
    car_route = dict()

    for car_item in car_data.values():
        # route中存储的路径信息，my_map中存在的是路口信息，注意转换
        car_id = car_item[0]
        start_time = car_item[4]

        # 要构造的每辆车的路径数据
        car_route[car_id] = [car_id, start_time]

        start_cross_id = car_item[1]
        end_cross_id = car_item[2]

        # id传递的是副本，改变了没关系
        flag = straight_route(start_cross_id,end_cross_id, cross_data, my_map)
        if flag != 1:
            for road_id in flag:
                car_route[car_id].append(road_id)
            continue

        cross_visited = dict()
        for cross_id  in cross_data:
            cross_visited[cross_id] =0

        cross_visited[start_cross_id] =1

        path = []
        all_path = []
        curve_route1(start_cross_id, end_cross_id, cross_data, my_map,cross_visited,path,all_path)
        all_path.sort(key=lambda x :len(x))
        short_path = all_path[0]
        for road_id in short_path:
            car_route[car_id].append(road_id)

    # f = open('car_route_test.txt',mode='w')
    # f.write(str(car_route))
    return car_route


def straight_route(start_cross_id,end_cross_id, cross_data, my_map):
    # return 1表示路径有问题
    sx, sy = my_map[start_cross_id]['cross_id_pos'][:2]
    ex, ey = my_map[end_cross_id]['cross_id_pos'][:2]
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
        road_id = utils.get_road_id(r1, r2)
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
        road_id = utils.get_road_id(r1, r2)
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
        road_id = utils.get_road_id(r1, r2)
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
        road_id = utils.get_road_id(r1, r2)
        road_list.append(road_id)

        # 新一轮的迭代
        start_cross_id = next_cross_id
        start_next_cross_list = my_map[start_cross_id]['connect']
        sx, sy = my_map[next_cross_id]['cross_id_pos'][:2]

    return road_list

# 这是一个遍历算法的原型，遍历的时候使用枝减方法，并且使用递归。
# path是我要想得到的结果。
def curve_route1(start_cross_id, end_cross_id, cross_data, my_map,cross_visited,path,all_path):

    # 只有到达终点，才加入path中
    if start_cross_id == end_cross_id:
        all_path.append(path.copy())
        return path

    next_cross_list = my_map[start_cross_id]['connect']
    next_cross_list = [x for x in next_cross_list if x != -1]
    next_cross_list = [x for x in next_cross_list if cross_visited[x] == 0]

    if len(next_cross_list) ==0:
        return 1

    for next_cross_id in next_cross_list:
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = utils.get_road_id(r1,r2)
        path.append(road_id)
        cross_visited[start_cross_id] = 1

        curve_route1(next_cross_id, end_cross_id, cross_data, my_map, cross_visited, path,all_path)

        path.pop()


def tt():
    road_data = utils.read_table('road.txt')
    cross_data = utils.read_table('cross.txt')
    car_data = utils.read_table('car.txt')
    route_data = build_route(road_data, cross_data, car_data)
    # 10000: [10000, 3, 5023, 5016, 5017, 5018,
    print(route_data)
    print(route_data[10601])

'''
[18869, 6, 5031, 5032, 5033, 5027, 5020, 5021, 5014, 5006, 5005, 5004, 5003, 5002, 5001, 5000, 5007, 5015, 5023, 5030, 
5035, 5041, 5042, 5043, 5044, 5045, 5046, 5047, 5055, 5061, 5060, 5059, 5058, 5065, 5080, 5093]

'''
# tt()
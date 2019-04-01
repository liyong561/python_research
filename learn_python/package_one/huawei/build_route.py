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
        if car_id == 10018:
            print("10018")
        start_time = car_item[4]

        # 要构造的每辆车的路径数据
        car_route[car_id] = [car_id, start_time]

        start_cross_id = car_item[1]
        end_cross_id = car_item[2]

        '''
        # id传递的是副本，改变了没关系
        flag = straight_route(start_cross_id,end_cross_id, cross_data, my_map)
        if flag != 1:
            for road_id in flag:
                car_route[car_id].append(road_id)
            continue
        '''
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


# 这是一个遍历算法的原型，遍历的时候使用枝减方法，并且使用递归。
# path是我要想得到的结果。
def curve_route1(start_cross_id, end_cross_id, cross_data, my_map, cross_visited, path, all_path):
    # 只有到达终点，才加入path中
    if start_cross_id == end_cross_id:
        all_path.append(path.copy())
        return path

    next_cross_list = my_map[start_cross_id]['connect']
    # 如果不设置一个访问标志位，就会出现图中的环出现死循环。
    next_cross_list = [x for x in next_cross_list if x != -1 and cross_visited[x] == 0]

    if len(next_cross_list) == 0:
        return 1

    for next_cross_id in next_cross_list:
        r1 = cross_data[start_cross_id][1:]
        r2 = cross_data[next_cross_id][1:]
        road_id = utils.get_road_id(r1, r2)
        path.append(road_id)

        cross_visited[next_cross_id] = 1

        curve_route1(next_cross_id, end_cross_id, cross_data, my_map, cross_visited, path, all_path)

        path.pop()

def tt():
    road_data = utils.read_table('road.txt')
    cross_data = utils.read_table('cross.txt')
    car_data = utils.read_table('car.txt')
    route_data = build_route(road_data, cross_data, car_data)
    with open('map.txt',mode='w') as f:
        for i in route_data:
            print(route_data[i])
            print("\n")
    # 10000: [10000, 3, 5023, 5016, 5017, 5018,
    for i in range(10600,14000):
        print(route_data[i])


# tt()
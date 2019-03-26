import package_one.huawei.utils as utils
import math

'''
这个赛题的核心就是生产路径文件，即类似c_route.txt这样的文件。
还有出发时间，一旦出发后是不能停的。
(1001, 1, 501, 502, 503, 516, 506, 505, 518, 508, 509, 524)
Depth-First Traversal

'''


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


'''
使用深度优先方法，遍历整个图节点，建立新的地图表示。
很多点，应该只有一个原点，
map的结构，{cross_id_1:value1,cross_id_2,value2}
value的结构，{cross_id_pos:[100,1200,cs0],connect:[cs2,cs3,cs4,cs5]}
# 这个visit是一个递归结构的。
'''


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
    cross_road__list = utils.rotate_list(cross_road__list_init, start_road_id_idx)[1:]
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
        position = utils.number_position(theta_rel)

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
            next_cross_item['cross_id_pos'] = utils.new_number_position(position, co_x, co_y, road_length)
            next_cross_item['cross_id_pos'].append(next_cross_id)
            next_cross_item['connect'] = [-1, -1, -1, -1]
            next_cross_list.append(next_cross_item)
            next_road_list.append(road_id)

    route_map[cross_id] = start_item

    # dfs遍历
    for i in range(len(next_cross_list)):
        visit_graph(next_cross_list[i], start_item, next_road_list[i], cross_data, road_data, route_map)



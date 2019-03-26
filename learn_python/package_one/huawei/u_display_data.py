import package_one.huawei.utils as utils
import package_one.huawei.build_route as build_map


def tt():
    file = 'car.txt'
    data = utils.read_table(file)
    print(data[10018])
    '''
    count = 0
    for car_id in data:
        if data[car_id][1] == 20 and data[car_id][2] == 7:
            count += 1
            print(data[car_id])
    print(count)
    '''


def tt1():
    file = 'cross.txt'
    data = utils.read_table(file)
    print(data[6])


def tt2():
    file = 'road.txt'
    data = utils.read_table(file)
    print(data[34])


def rt():
    road_data = utils.read_table('road.txt')
    cross_data = utils.read_table('cross.txt')
    car_data = utils.read_table('car.txt')
    route_data = build_map.build_route(road_data, cross_data, car_data)
    print(route_data[10018])


tt1()

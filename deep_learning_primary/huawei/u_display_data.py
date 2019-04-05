#!/usr/bin/python
# -*- coding:utf8 -*-
import package_one.huawei.utils as utils
import package_one.huawei.build_route as build_route
import package_one.huawei.build_map as build_map


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
    for road_item in data.values():
        if road_item[6] == 0:
            print(road_item)
    print(data[5068])


def rt():
    road_data = utils.read_table('road.txt')
    cross_data = utils.read_table('cross.txt')
    car_data = utils.read_table('car.txt')
    my_map = build_map.build_route_map(road_data, cross_data)
    route_data = build_route.build_route(road_data, cross_data, car_data)

    direction = dict() # not in for local variables
    for car_id in range(10005, 12000):
        start_cross_id = car_data[car_id][1]
        end_cross_id = car_data[car_id][2]
        next_cross_id = start_cross_id
        i = 2
        while next_cross_id != end_cross_id:
            road_id = route_data[car_id][i]

            back_cross_id = road_data[road_id][4] if road_data[road_id][4] != next_cross_id else road_data[road_id][5]

            back_cross_id_idx = my_map[next_cross_id]['connect'].index(back_cross_id)
            if car_id not in direction:
                direction[car_id] = []
            direction[car_id].append(back_cross_id_idx)

            next_cross_id = back_cross_id
            i += 1

    print(direction)
    for car_id,route in direction.items():
        direction[car_id] = set(direction[car_id])
    print(direction)

# rt()

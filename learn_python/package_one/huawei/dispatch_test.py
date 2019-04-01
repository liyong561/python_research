'''
1.先让能够上路的车上路。2.让能够到达终点的车到达终点（路口），并消失。3.调度在路上的车辆。
所以调度也分为几种调度场景。
            [car_id,s,v,channel，direction,status]，构造这个数据块，非常的重要。
            尽量地写的清楚，好理解一些。这个速度的确定依赖于多方面因素，1,car velocity，2，road velocity,3,最重要的，前方是否有车辆，多远处。
            在确定速度时还要确定其路况信息。
            1001: [1001,1, 16, 6, 1] car_item
            1001: (1001, 1, 501, 502, 503, 516, 506, 505, 518, 508, 509, 524) ,route_item 还要根据起点来确定方向是正向还是反向。
            501: [501, 10, 6, 5, 1, 2, 1] route_item,
            1:[1, 501, 513, -1, -1] # cross_id,路的地点
'''


def dispatch_on_road(t, car_data, route_data, road_data, road_with_car):
    # 先获取t-1时刻的状态。从1开始，0时刻都在原地

    car_item_start = [car_item for car_item in car_data.values() if car_item[4] == t]  # 遍历字典,和列表的差异
    print(car_item_start)
    # 车到达计划出发时间，可以出发，也可以等，简单模型中，直接出发,这样会堵塞。

    for car_item in car_item_start:
        car_id = car_item[0]
        road_id = route_data[car_id][2]  # 车辆第一段路id，
        channel = road_data[road_id][3]

        start = road_data[road_id][4]  # 这条道路的正向起点
        direction = 0 if start == car_item[1] else 1  # 0表示同向

        s = min(car_item[3], road_data[road_id][3])  # 可行的最大速度，还要看是否能走。不堵塞。

        if road_id not in road_with_car:  # 该道路没有车辆时
            road_with_car[road_id] = []
            first_record = [car_item[0], s, s, 0, direction, 1]
            road_with_car[road_id].append(first_record)
            continue

        road_item = road_with_car[road_id]  # 获得道路的车况信息.

        flag1 = False
        flag2 = False
        for channel_i in range(channel):

            #  print("channel:"+str(channel_i))
            # 字段的类型都是之前定义好的，更改一点，就可能影响整个程序。
            channel_with_car = [record for record in road_item if
                                record[2] == channel_i and record[3] == direction]
            if len(channel_with_car) == 0:  # 车道上没有车辆
                record = [car_item[0], s, s, channel_i, direction, 1]
                road_with_car[road_id].append(record)
                flag2 = True
                break

            print('cc:' + str(channel_with_car))
            for record in channel_with_car:
                if record[1] > s:
                    # 如果有空就可以上路,车不是一个质点，要确定是以车头为坐标，还是以车尾为坐标,最终商定以车头为坐标。尽量按照最大速度出发。
                    new_record = [car_item[0], s, s, channel_i, direction, 1]  # 符合条件，上路。
                    road_with_car[road_id].append(new_record)
                    flag1 = True
                    break

            if flag1:
                flag2 = True
                break
        if flag2:
            continue

        car_item[4] += 1  # 该道路所有车道都没有空闲，t时刻没有上路，则等待下一次，也可随机等待时间。

    print("t时刻调度完毕")



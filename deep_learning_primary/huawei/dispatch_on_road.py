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
    counter = 0
    car_on_road = 0
    for car_item in road_with_car.values():
        car_on_road += len(car_item)
    print("car on the road" + str(car_on_road))

    road_num = len(road_data)

    car_item_start_list = [car_item1 for car_item1 in car_data.values() if
                           car_item1[4] == t or car_item1[4] == t + 1]  # 遍历字典,和列表的差异
    # 车到达计划出发时间，可以出发，也可以等，简单模型中，直接出发,这样会堵塞。
    for car_item in car_item_start_list:
        # 更距时间简单调节车流量
        if t < 1000:
            if 12 * road_num < car_on_road + counter:
                print('车况很糟糕')
                break
   
        else:
            if 10 * road_num < car_on_road + counter:
                print('车况很糟糕')
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

            # road_with_car这个数据进行实时更新
            counter += 1
            road_with_car[road_id].append(first_record)

            # 上路后，从上路的列表中移除
            car_item[4] = 0
            route_data[car_id][1] = t

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
                car_item[4] = 0
                route_data[car_id][1] = t

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
                # 置零，表示已出发
                car_item[4] = 0
                route_data[car_id][1] = t

                break

    car_item_start_list_wait = [car_item1 for car_item1 in car_data.values() if car_item1[4] >= t]  # 遍历字典,和列表的差异

    print('还有车等待出发：' + str(len(car_item_start_list_wait)))
    print(car_item_start_list_wait)

    for car_item in car_item_start_list_wait:
        # 什么情况下回延迟上路？
        if len(route_data[car_item[0]]) < 10:
            car_item[4] += 2
        if len(route_data[car_item[0]]) < 24:
            car_item[4] += 3
        else:
            car_item[4] += 5

    # 一个轮次，对其状态初始化一次
    if t % 20 == 0 or t % 37 == 0 :
        for car_item in car_item_start_list_wait:
            # 什么情况下回延迟上路？
            car_item[4] = t + 3

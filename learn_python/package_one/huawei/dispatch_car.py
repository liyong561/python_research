import math
from package_one.huawei import dispatch_channel_car_go_cross as dc

'''
1.扫描每一条路段，标记不会出路口，也没有车辆阻挡的车辆，这种车具有最高优先级，调度。调度之后将其标识为终止车辆。
2.扫描每一条路段，标记不会出路口，阻挡车辆为终止车辆的车，这种车具有次优先级，调度v = min(最高车速，道路限速，s/t) 其中t=1，还受车距的影响。
[car_id,s,v,channel，direction，status]，构造这个数据块，非常的重要。
'''


# 在这个方法中，要对road_with_car的数据进行分类
def dispatch_car_run(cross_data, road_data, route_data, road_with_car):
    road_with_car1 = dict()
    for road_id, item_road in road_with_car.items():
        if len(item_road) == 0:
            continue

        road_length = road_data[road_id][1]
        channel = road_data[road_id][3]
        rv = road_data[road_id][2]

        # 还要具体到车道
        for channel_i in range(channel):

            for direction in range(2):

                # 使用了原来数据的引用
                item_channel = [x for x in item_road if x[3] == channel_i and x[4] == direction]
                if len(item_channel) == 0:
                    # 使用了continue就可以不使用else
                    continue

                item_channel.sort(key=lambda x: x[1], reverse=True)
                first_record = item_channel[0]  # 处于车道最前面的车辆。
                s = first_record[1]
                v = min(first_record[2], rv)

                # 一定不会出路口
                if s + v <= road_length:
                    if road_id not in road_with_car1:
                        road_with_car1[road_id] = []

                    for i in range(len(item_channel)):
                        # 谨记，road_with_car1只是持有road_with_car中元素的引用。
                        road_with_car1[road_id].append(item_channel[i])

    # 先调度一定不会出路口的车辆
    dispatch_straight(road_data, road_with_car1)

    # 再调度可能出路口的车辆
    dispatch_cross(road_data, cross_data, route_data, road_with_car)

    for road_id in road_with_car:
        for record in road_with_car[road_id]:
            # 变成为调度的在状态
            if record[5] == 0 :
                print('发生了死锁')

    for road_id in road_with_car:
        for record in road_with_car[road_id]:
            # 变成为调度的在状态
            record[5] = 0


# 第一步：对于一定不会出路口车，及其后面的车的调度
def dispatch_straight(road_data, road_with_car):
    # t时刻，变成t+1时刻的状态。先找到每个车道上的第一辆车
    for road_id, road_with_car_item in road_with_car.items():
        if len(road_with_car_item) == 0:
            continue

        rv = road_data[road_id][2]
        channel = road_data[road_id][3]
        for channel_i in range(channel):

            # 这里，正向车道和反向车道还要分开
            for i in range(2):
                road_with_car_item_channel = [x for x in road_with_car_item if
                                              x[3] == channel_i and x[4] == i and x[5] == 0]
                if len(road_with_car_item_channel) == 0:
                    continue

                # 直接排序,从大到小，取车道上距路口最近的车辆
                road_with_car_item_channel.sort(key=lambda x: x[1], reverse=True)

                # 这里输出就有问题了
                # print(road_with_car_item_channel)

                first_record = road_with_car_item_channel[0]  # 处于车道最前面的车辆。
                record_pre = first_record
                for record in road_with_car_item_channel:
                    v = min(record[2], rv)
                    if record == first_record:
                        # 对基本数据的修改会直接影响到road_with_car,因为它们持有同一个对象。
                        record[1] += v
                        record[5] = 1
                        # record_pre获得record的引用，record_pre是非核心变量，并且未修改record值
                        continue

                    # 接下来应该调度其后的车辆
                    max_s = record_pre[1] - record[1] - 1  # 车长为1
                    if max_s < 0:
                        print('why')  # 这句话没有执行到
                    record[1] += min(v, max_s)
                    record[5] = 1
                    record_pre = record


# 第二步：对于可能会出路口的车，及其后面的车的调度
# 这个调度可能对路口循环几遍，那么怎么跳出循环呢？
# cross,road注意命名的规范
def dispatch_cross(road_data, cross_data, route_data, road_with_car):
    # 保证路口是按照cross_id排序的。
    for cross_id, cross_item in cross_data.items():
        road_list_init = cross_item[1:]  # 去掉路口id字段,路口的顺序
        road_list = [x for x in road_list_init if x != -1]
        road_list.sort()  # 从小到大的顺序

        # 一个路口，车道循环若干遍，若循环一圈后，没有发生车辆调度，则因退出循环。
        while 1:
            count = []
            for road_id in road_list:

                # 车道内没有车辆，不需要调度
                if road_id not in road_with_car or len(road_with_car[road_id]) == 0:

                    # road_with_car_item_channel_wait = []
                    if road_id not in road_with_car:
                        road_with_car[road_id] = []
                    continue

                channel = road_data[road_id][3]
                for channel_id in range(channel):

                    # 只调度向路口走的车辆,目的地是路口
                    road_direction = 0 if road_data[road_id][5] == cross_id else 1

                    # key error,这个lambda表达式有点复杂,严谨，判断列表是否为空，否则lambda表达式会报错
                    # 调度的车辆都是为调度的车辆
                    road_with_car_item_channel_wait = [x for x in road_with_car[road_id] if
                                                       x[3] == channel_id and x[4] == road_direction and
                                                       x[5] == 0]

                    # 车道无车，不需要调度，如果为空，不会调用那个函数的。
                    if len(road_with_car_item_channel_wait) == 0:
                        continue

                    road_with_car_item_channel_wait.sort(key=lambda x: x[1], reverse=True)
                    record = road_with_car_item_channel_wait[0]  # record不会再小于零了

                    if record[1] > 20:
                        print("s >20")

                    car_id = record[0]
                    road_id_idx = route_data[car_id].index(road_id)

                    # 车辆的终点，直接入库。
                    if road_id_idx == len(route_data[car_id]) - 1:
                        # 应该在原有的引用上操作
                        # road_with_car_item_channel_wait.pop(0)
                        delete_record = road_with_car_item_channel_wait.pop(0)
                        road_with_car[road_id].remove(delete_record)
                        print(str(car_id)+": 入库")
                        continue

                    #  从这里拆分出一个函数，
                    next_road_id = route_data[car_id][road_id_idx + 1]
                    go_cross(record, cross_id, road_list_init, road_id, next_road_id, road_with_car_item_channel_wait,
                             route_data, road_data, road_with_car, count)

            # 遍历一圈后没有车调动,应该换到下一个路口
            if len(count) == 0:
                break


# 调度该车辆，及其车道后的车辆
# 传入两个路况状态对象
def go_cross(record, cross_id, cross_list_init, road_id, next_road_id, road_with_car_item_channel_wait,
             route_data, road_data, road_with_car, count):
    start_idx = cross_list_init.index(road_id)
    end_idx = cross_list_init.index(next_road_id)
    dlr = int(math.fabs(start_idx - end_idx))

    # D，直接通行
    if dlr == 2:
        dc.car_go_cross_road(record, cross_id, road_id, next_road_id, road_with_car_item_channel_wait, road_data,
                             road_with_car, count)
        return

    #  左通行，record左转，按照交通规则，应该查看是否有直行车辆通过next_road
    if (dlr == 1 and start_idx < end_idx) or (dlr == 3 and start_idx > end_idx):
        opposite_idx = (end_idx + 2) % 4
        opposite_road_id = cross_list_init[opposite_idx]  # 该路上如果有直行车辆，则优先，该车道等待。
        # 对面的路不存在，最理想的情况，直接通行。
        if opposite_road_id == -1:
            dc.car_go_cross_road(record, cross_id, road_id, next_road_id, road_with_car_item_channel_wait, road_data,
                                 road_with_car, count)
            return

        opposite_direction = 0 if road_data[opposite_road_id][5] == cross_id else 1

        # 看是否有等待直行的车辆,是不是还要判断其能否通过路口？
        road_with_car_item_opposite = [x for x in road_with_car[opposite_road_id] if
                                       x[4] == opposite_direction and x[5] == 0]
        # 该路上存在要过路口的车辆，且其next_road是左转的道路。
        if len(road_with_car_item_opposite) != 0:
            opposite_channel = road_data[opposite_road_id][3]
            for channel_i in range(opposite_channel):
                opposite_item = [x for x in road_with_car_item_opposite if x[3] == 3]
                if len(opposite_item) != 0:
                    opposite_item.sort(key=lambda x: x[1], reverse=True)
                    opposite_record = opposite_item[0]
                    # 会不会出现直接入库的车？相当于直行车
                    car_id = opposite_record[0]
                    opposite_road_id_idx = route_data[car_id].index(opposite_road_id)
                    if opposite_road_id_idx < len(route_data[car_id]) - 1:
                        opposite_next_road_id = route_data[car_id][opposite_road_id_idx + 1]

                        # 确定有直行车要过该路口，则等待
                        if opposite_next_road_id == next_road_id:
                            return
                            #  函数没有返回，则直接过去
        dc.car_go_cross_road(record, cross_id, road_id, next_road_id, road_with_car_item_channel_wait, road_data,
                             road_with_car, count)

    # 右通行,判断有没有直行车，有没有左行车通过。
    else:
        opposite_idx = (end_idx + 2) % 4
        opposite_road_id = cross_list_init[opposite_idx]  #
        left_idx = (start_idx + 2) % 4
        left_road_id = cross_list_init[left_idx]

        # 寻找要等待的情况，看有无直行车辆
        if opposite_road_id != -1:
            opposite_direction = 0 if road_data[opposite_road_id][5] == cross_id else 1
            road_with_car_item_opposite = [x for x in road_with_car[opposite_road_id] if
                                           x[4] == opposite_direction and x[5] == 0]
            if len(road_with_car_item_opposite) != 0:

                # channel
                opposite_channel = road_data[opposite_road_id][3]
                for channel_i in range(opposite_channel):
                    opposite_item = [x for x in road_with_car_item_opposite if x[3] == channel_i]
                    if len(opposite_item) != 0:
                        opposite_item.sort(key=lambda x: x[1], reverse=True)
                        opposite_record = opposite_item[0]
                        # 会不会出现直接入库的车？相当于直行车
                        car_id = opposite_record[0]
                        opposite_road_id_idx = route_data[car_id].index(opposite_road_id)

                        #
                        if opposite_road_id_idx < len(route_data[car_id]) - 1:
                            opposite_next_road_id = route_data[car_id][opposite_road_id_idx + 1]
                            # 确定有直行车要过该路口，则等待
                            if opposite_next_road_id == next_road_id:
                                return
                                #  看有无左行车辆
        if left_road_id != -1:
            # 易懂的名字也有利于检查
            left_direction = 0 if road_data[left_road_id][5] == cross_id else 1
            road_with_car_item_left = [x for x in road_with_car[left_road_id] if x[4] == left_direction and x[5] == 0]
            if len(road_with_car_item_left) != 0:
                left_channel = road_data[left_road_id][3]

                for channel_i in range(left_channel):
                    left_item = [x for x in road_with_car_item_left if x[3] == channel_i]
                    if len(left_item) != 0:
                        left_item.sort(key=lambda x: x[1], reverse=True)
                        left_record = left_item[0]
                        car_id = left_record[0]
                        left_road_id_idx = route_data[car_id].index(left_road_id)
                        if left_road_id_idx < len(route_data[car_id]) - 1:
                            left_next_road_id = route_data[car_id][left_road_id_idx + 1]
                            if left_next_road_id == next_road_id:
                                return

        dc.car_go_cross_road(record, cross_id, road_id, next_road_id, road_with_car_item_channel_wait, road_data,
                             road_with_car, count)

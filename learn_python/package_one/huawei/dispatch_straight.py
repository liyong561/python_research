'''
1.扫描每一条路段，标记不会出路口，也没有车辆阻挡的车辆，这种车具有最高优先级，调度。调度之后将其标识为终止车辆。
2.扫描每一条路段，标记不会出路口，阻挡车辆为终止车辆的车，这种车具有次优先级，调度v = min(最高车速，道路限速，s/t) 其中t=1，还受车距的影响。
[car_id,s,v,channel，direction，status]，构造这个数据块，非常的重要。
'''


def dispatch_straight(t, road_data,road_with_car):
    # t时刻，变成t+1时刻的状态。先找到每个车道上的第一辆车
    for road_id, road_with_car_item in road_with_car.items():
        road_length = road_data[road_id][1]
        channel = road_data[road_id][3]

        for channel_i in range(channel):
            # 处于同一车道，并且未调度的车辆记录
            road_with_car_item_channel = [x for x in road_with_car_item if x[3] == channel_i and x[5] == 0]
            if len(road_with_car_item_channel) == 0:
                continue

            # 取车道上距路口最近的车辆
            '''
            s_seq = [x[1] for x in road_with_car_item_channel]
            s_max = max(s_seq)
            record_index = s_seq.index(s_max)
            record = road_with_car_item_channel[record_index]
            '''
            # 直接排序
            road_with_car_item_channel.sort(key=lambda x: x[1])
            flag = True

            for record in road_with_car_item_channel:
                if flag and (record[1] + record[2]) <= road_length:
                    #  调度，并且标志其为终止状态
                    flag = False  #
                    record[1] = record[1] + record[2]
                    record[5] = 1
                    record_pre = record
                    continue

                # 接下来应该调度其后的车辆
                velocity = min(record[2], record_pre[1] - record[1])
                record[1] += velocity
                record[2] = velocity
                record[5] = 1
    '''
      接下来以路口id为顺序进行调度
    '''
def dispatch_cross(t,cross_data,road_with_car):
    # 保证路口是按照cross_id排序的。
    for cross_id,cross_item in cross_data.items():

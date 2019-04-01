'''
author:liyong
[car_id,s,v,channel，direction，status] # 0,表示和路的正方向同向,v表示汽车的最高速度
从这个调度过程中抽象一个车道内的汽车，在路口可能要进入下一个路段的函数,即满足v1>road_length-s
在满足条件时调用该函数
思考一下该函数需要传入哪些参数。
最重要的是,第一步干啥？万世开头难
该算法的复杂之处之一就是路口的调度
'''


# 该车record,及其后的车road_with_car_item_channel_wait，调用了走的函数即返回
def car_go_cross_road(record, cross_id, road_id, next_road_id, road_with_car_item_channel_wait, road_data,
                      road_with_car, count):
    # 由最基本的数据，获得路况
    next_channel = road_data[next_road_id][3]
    next_road_direction = 0 if road_data[next_road_id][4] == cross_id else 1

    # chanel to channel,车辆最终定位到一个车道内。
    for next_channel_i in range(next_channel):

        # 获得将要进入车道信息
        next_road_with_car_item_channel = [x for x in road_with_car[next_road_id] if
                                           x[3] == next_channel_i and x[4] == next_road_direction]
        v1 = min(record[2], road_data[road_id][2])
        v2 = min(record[2], road_data[next_road_id][2])
        x1 = road_data[road_id][1] - record[1]
        # 前方车道内无车，则可进行调度
        if len(next_road_with_car_item_channel) == 0:

            # x2来自原始数据，不会有问题
            x2 = road_data[next_road_id][1]
            count.append(1)
            car_go_cross_channel(v1, v2, x1, x2, road_id, next_road_id, next_channel_i, next_road_direction,
                                 road_with_car_item_channel_wait, road_with_car, road_data)
            return

        # 有车，获取最后一辆车的调度状态
        else:
            next_road_with_car_item_channel.sort(key=lambda x: x[1])
            next_record = next_road_with_car_item_channel[0]

            # 注意这里x2的取值，正反向时s的值。

            x2 = next_record[1] - 1

            # 前方车辆为终止车辆，如果有空，就必须走
            if next_record[5] == 1:

                # 两车之间没有间隙，寻找下一个车道。
                if x1 == 0 and x2 == 0:
                    # 发生了堵塞，该车不能行走，变为已调度状态。
                    if next_channel_i == next_channel -1 :
                        count.append(1)
                        car_go_cross_channel(v1, v2, x1, x2, road_id, next_road_id, next_channel_i, next_road_direction,
                                             road_with_car_item_channel_wait, road_with_car, road_data)
                    continue

                else:
                    count.append(1)
                    car_go_cross_channel(v1, v2, x1, x2, road_id, next_road_id, next_channel_i, next_road_direction,
                                         road_with_car_item_channel_wait, road_with_car, road_data)
                    return

            # 前车为等待车辆
            else:
                # 不满足最大行车距离，该车辆也为等待车辆。
                if min(v1, v2) > x1 and v2 - x1 > x2:
                    continue

                else:
                    # 调用了这个函数后，本函数不一定返回，所以使用return不好。
                    count.append(1)
                    # 该函数可以看出，同一个车道可能出现后面终止，前面等待的情况，这对于之前的调度有些参考价值。
                    car_go_cross_channel(v1, v2, x1, x2, road_id, next_road_id, next_channel_i, next_road_direction,
                                         road_with_car_item_channel_wait, road_with_car, road_data)
                    return


'''
这个函数的功能就是在第二个路段最大可行驶距离为x2时，到路的状态,最好前方车辆为终止状态。
在road_with_car的原始数据集上修改对象的引用
'''


def car_go_cross_channel(v1, v2, x1, x2, road_id, next_road_id, next_channel_i, next_road_direction,
                         road_with_car_item_channel_wait, road_with_car, road_data):
    # 默认传过来的road_with_car_item_channel_wait至少有一个元素,且以排好序
    record = road_with_car_item_channel_wait[0]

    # 会出路口的条件,进入下一个路口
    if v1 > x1 and v2 > x1 and x2 > 0 :
        new_record = road_with_car_item_channel_wait.pop(0)
        road_with_car[road_id].remove(new_record)
        new_record[1] = min(v2 - x1, x2)  # 防止撞车,这里有问题，s可能为0

        new_record[3] = next_channel_i
        new_record[4] = 0 if next_road_direction == 0 else 1
        new_record[5] = 1  # 已调度状态
        road_with_car[next_road_id].append(new_record)
        return

    # 剩下这种情况，会刚好卡在路口
    if v1 >= x1:
        record[1] += x1
        record[5] = 1

    else:
        record[1] += v1
        record[5] = 1
        # 不会出路口，则调度该车辆和其后的车辆
    record_pre = record

    for rd in road_with_car_item_channel_wait:
        if rd == record:
                continue
            # 这里的数据排好序了，也不会有问题
        new_v1 = min(rd[2], road_data[road_id][2])
        max_s = record_pre[1] - rd[1] - 1  # 车长为1
        rd[1] += min(new_v1, max_s)
        rd[5] = 1
        record_pre = rd

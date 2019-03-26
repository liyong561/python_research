'''
优先处理t+1时刻可以出路口的车辆，将这些车辆标记为等待车辆。只是标记，并没有调度。
在调度的过程中，动态的生成t
'''
import package_one.huawei.dispatch_car as das
import package_one.huawei.dispatch_on_road as dor
import package_one.huawei.utils as utils
import package_one.huawei.build_route as route


def dispatch():
    road_data = utils.read_table('road.txt')
    cross_data = utils.read_table('cross.txt')
    car_data = utils.read_table('car.txt')
    route_data = route.build_route(road_data, cross_data, car_data)
    road_with_car = dict()
    dor.dispatch_on_road(1, car_data, route_data, road_data, road_with_car)

    # t为调度的总时间
    t = 2
    while 1:

        das.dispatch_car_run(cross_data, road_data, route_data, road_with_car)

        # dor.dispatch_on_road(t, car_data, route_data, road_data, road_with_car)
        print(road_with_car)
        flag = True
        for road_id in road_data:
            if road_id in road_with_car:
                if len(road_with_car[road_id]) > 0:
                    flag = False
                    break
        if flag:
            break

        t += 1
        if t == 1000:
            print('500次了')
        print(t)

    print("调度完毕")
    return t


dispatch()

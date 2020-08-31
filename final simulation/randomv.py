# generate random vehicles and write them to SUMO's route files
import random
from decimal import Decimal
import os

source_dir = "C:\\Users\\shaw1\\Desktop\\sumo\\hete"

num = 4000
r = 1.0 # AV rate
rate = 1 - r
value = []
for j in range(0, num):
    value.append(j)

car = random.sample(value, int(rate * num * 0.8))
tru = random.sample(set(value) - set(car), int(rate * num * 0.2))
car_a = random.sample(set(value) - set(car) - set(tru), int((1-rate) * num * 0.8))
tru_a = set(value) - set(car) - set(tru) - set(car_a)

print('car number = ' + str(len(car)))
print('tru number = ' + str(len(tru)))
print('a car number = ' + str(len(car_a)))
print('a truck number = ' + str(len(tru_a)))

vehicle_list = []

for i in range(0, num):



    vLane = int(random.choice('2356'))
    vPos = Decimal(random.uniform(0, 420)).quantize(Decimal('0.00'))
    vSpeed = round(random.uniform(0, 70), 2)
    my_name = i+1
    totLanes = 4
    if totLanes == 4:
        # For the dataset with 4 lanes: 2 lower lanes are 2,3; 2 upper lanes are 5,6
        if vLane < 4:
            my_route = "route0"
            my_pos = 0
            my_speed = vSpeed
            my_lane = vLane - 2
        else:
            my_route = "route1"
            my_pos = 0
            my_speed = vSpeed
            my_lane = vLane - 5
    elif totLanes == 6:
        # For the dataset with 6 lanes: 3 lower lanes are 2,3,4; 3 upper lanes are 6,7,8
        if vLane < 5:
            my_route = "route0"
            my_pos = 420 - vPos
            my_speed = vSpeed
            my_lane = vLane - 2
        else:
            my_route = "route1"
            my_pos = vPos
            my_speed = vSpeed
            my_lane = vLane - 6

# set different color for vehicles
    if i in car:
        my_type = "car_IDM"
        my_color = '0,0,1'
    elif i in tru:
        my_type = "truck_IDM"
        my_color = '1,0,0'
    elif i in car_a:
        my_type = "car_IDM_a"
        my_color = '0,1,0'
    else:
        my_type = "truck_IDM_a"
        my_color = '1,1,0'

    if my_type is 'truck_IDM' or my_type is 'car_IDM':
        vehicle_list.append('   <vehicle id=\"%s'%(str(my_name))+'\" type=\"%s'%(my_type) +'\" depart=\"0\" route=\"%s'
                            %(my_route)+'\" departLane=\"%s'%(str(my_lane))+'\" departPos=\"%s'%(str(my_pos))
                            +'\" departSpeed=\"%s'%(str(my_speed)) + '\" color=\"%s"'%(my_color)+
                            '>\n   <param key=\"has.driverstate.device\" value=\"true\"/> \n   </vehicle> \n')
    else:
        vehicle_list.append('   <vehicle id=\"%s'%(str(my_name))+'\" type=\"%s'%(my_type) +'\" depart=\"0\" route=\"%s'
                            %(my_route)+'\" departLane=\"%s'%(str(my_lane))+'\" departPos=\"%s'%(str(my_pos))
                            +'\" departSpeed=\"%s'%(str(my_speed)) + '\" color=\"%s"/>'%(my_color)+'\n')


content1 = []

with open(os.path.join(source_dir, 'myroutes2.rou.xml'), 'r') as ff:
    header_text1 = ff.readlines()
    for i in range(0, 42):
        content1.append(header_text1[i])


content2 = []

with open(os.path.join(source_dir, 'myroutes3.rou.xml'), 'r') as ff:
    header_text2 = ff.readlines()
    for i in range(0, 42):
        content2.append(header_text2[i])

content3 = []

with open(os.path.join(source_dir, 'myroutes4.rou.xml'), 'r') as ff:
    header_text3 = ff.readlines()
    for i in range(0, 42):
        content3.append(header_text3[i])

with open(os.path.join(source_dir, 'myroutes2.rou.xml'), 'w') as file:
    file.writelines(content1)
    file.writelines(vehicle_list)
    file.write("\r\n</routes>\r\n")


with open(os.path.join(source_dir, 'myroutes3.rou.xml'), 'w') as file:
    file.writelines(content2)
    file.writelines(vehicle_list)
    file.write("\r\n</routes>\r\n")

with open(os.path.join(source_dir, 'myroutes4.rou.xml'), 'w') as file:
    file.writelines(content3)
    file.writelines(vehicle_list)
    file.write("\r\n</routes>\r\n")
    #if my_type is 'truck_IDM' or my_type is 'car_IDM':
    #    print('   <vehicle id="' + str(my_name) + '" ', 'type="' + my_type + '" depart="0"', 'route="' + my_route + '"',
    #          'departLane="' +
    #          str(my_lane) + '"', 'departPos="' + str(my_pos) + '"', 'departSpeed="' + str(my_speed) + '"',
    #          'color="' + my_color + '">\n   '
    #          + '<param key="has.driverstate.device" value="true"/> \n   </vehicle>')
    #else:
    #    print('   <vehicle id="' + str(my_name) + '" ', 'type="' + my_type + '" depart="0"', 'route="' + my_route + '"',
    #          'departLane="' +
    #          str(my_lane) + '"', 'departPos="' + str(my_pos) + '"', 'departSpeed="' + str(my_speed) + '"',
    #          'color="' + my_color + '"/>')




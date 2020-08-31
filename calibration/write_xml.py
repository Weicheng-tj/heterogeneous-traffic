import statistics
import csv
from decimal import Decimal

highd_filename = "comb_initial_states.csv"


def read_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vName = row['id']
            vLenght = row['length']
            vType = row['class']
            vLane = int(row['initial_lane'])
            vPos = Decimal(float(row['initial_position'])).quantize(Decimal('0.00'))
            vSpeed = round(float(row['initial_speed']), 2)
            my_name = str(vName)
            totLanes = 4
            if totLanes == 4:
                # For the dataset with 4 lanes: 2 lower lanes are 2,3; 2 upper lanes are 5,6
                if vLane < 4:
                    my_route = "route0"
                    my_pos = 420 - vPos
                    my_speed = -1 * vSpeed
                    my_lane = vLane - 2
                else:
                    my_route = "route1"
                    my_pos = vPos
                    my_speed = vSpeed
                    my_lane = vLane - 5
            elif totLanes == 6:
                # For the dataset with 6 lanes: 3 lower lanes are 2,3,4; 3 upper lanes are 6,7,8
                if vLane < 5:
                    my_route = "route0"
                    my_pos = 420 - vPos
                    my_speed = -1 * vSpeed
                    my_lane = vLane - 2
                else:
                    my_route = "route1"
                    my_pos = vPos
                    my_speed = vSpeed
                    my_lane = vLane - 6
            if vType == "Car":
                my_type = "car_IDM"
                my_color = '0,0,1'
            else:
                my_type = "truck_IDM"
                my_color = '0,1,0'

            print(
            '   <vehicle id="' + str(my_name) + '" ', 'type="' + my_type + '" depart="0"', 'route="' + my_route + '"',
            'departLane="' +
            str(my_lane) + '"', 'departPos="' + str(my_pos) + '"', 'departSpeed="' + str(my_speed) + '"',
            'color="' + my_color + '">\n   '
            + '<param key="has.driverstate.device" value="true"/> \n   </vehicle>')
#<vehicle id="leader_1" type="car_IDM" route="route0" departLane="0" depart="0" color="0,0,1"/>

read_csv(highd_filename)




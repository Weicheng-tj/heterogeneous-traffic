# A file for reading data from the SUMO's "full_output" file and save them into csv files

import xml.etree.ElementTree as ET
import pandas as pd

results_dir = 'results/'
root = ET.parse(results_dir+'full_output.xml').getroot()

vehicle_speed = []
vehicle_position = []
speed_dic = {}

for data in root:
    time = data.get('timestep')
    vehicles = data.find('vehicles')
    n_vehicles = len(vehicles.findall('vehicle'))
    speed_dic = {"time": time}
    position_dic = {"time": time}
    for vehicle in vehicles.iter('vehicle'):
        speed_dic[vehicle.get('id')] = vehicle.get('speed')
        position_dic[vehicle.get('id')] = vehicle.get('pos')

    vehicle_speed.append(speed_dic)
    vehicle_position.append(position_dic)

pd.DataFrame(vehicle_speed).to_csv(results_dir+"speed.csv", index=False)
pd.DataFrame(vehicle_position).to_csv(results_dir+"position.csv", index=False)

vehicle_speed_df = pd.DataFrame(vehicle_speed,dtype='float')
## Uncomment the line below if you want to fill NaN with 0
#vehicle_speed_df = vehicle_speed_df.fillna(0)
vehicle_speed_df.to_csv(results_dir+"sumo_vehicle_speed_df.csv", index=False)

vehicle_position_df = pd.DataFrame(vehicle_position,dtype='float')
## Uncomment the line below if you want to fill NaN with 0
#vehicle_position_df = vehicle_position_df.fillna(0)
vehicle_position_df.to_csv(results_dir+"sumo_vehicle_position_df.csv", index=False)

vehicle_speed_df_by_time = vehicle_speed_df.set_index('time')

vehicle_speed_df = vehicle_speed_df.drop('time', 1)
print(vehicle_speed_df)

## Calculate "meta-data" of the results
vehicle_speed_min = vehicle_speed_df.min().to_frame(name='min')
vehicle_speed_max = vehicle_speed_df.max().to_frame(name='max')
vehicle_speed_mean =vehicle_speed_df.mean().to_frame(name='mean')

vehicle_speed_stats = vehicle_speed_min.join(vehicle_speed_max).join(vehicle_speed_mean)
vehicle_speed_stats.to_csv(results_dir+"sumo_vehicle_speed_stats.csv", index=True)
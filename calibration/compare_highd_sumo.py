# get the speed performance indicator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_management.read_csv_from_path import *
from track_data_processing.find_car_following import *
from track_data_processing.find_initial_stats import *
from car_following_data_processing.extract_safety import *

data_id = []
plot = False

#Array of data id
for number in np.arange(60):
    data_id.append((str((number + 1)) if (number + 1) >= 10 else "0" + str(number + 1)))

#define the directory where you have the dataset
data_dir = "C:\\Users\\shaw1\\Desktop\\heterogeneous-highd-master\\python\\src/"

#define the directory where you have the SUMO results
sumo_results_dir = "C:\\Users\\shaw1\\Desktop\\sumo\\hete/results/"
sumo_filename = "sumo_vehicle_speed_stats.csv"

#define the directory to save your output file(s), if any
results_dir = "C:\\Users\\shaw1\\Desktop\\heterogeneous-highd-master\\python\\src\\results/"

dataset_id = 1
if dataset_id < 10:
    dataset_id = "0" + str(dataset_id)
else:
    dataset_id = str(dataset_id)

print("Now comparing SUMO results with the dataset number ", dataset_id)

## Load the data into variables
recording_meta_path = data_dir + dataset_id + "_recordingMeta.csv"
track_meta_path = data_dir + dataset_id + "_tracksMeta.csv"
track_path = data_dir + dataset_id + "_tracks.csv"
recording_meta_data = read_meta_info(str(recording_meta_path))
track_meta_data = read_static_info(str(track_meta_path))
track_data = read_track_csv(str(track_path))

sumo_stats = pd.read_csv(sumo_results_dir + sumo_filename)
sumo_stats.columns = ['id','min','max','mean']
sumo_stats = sumo_stats.set_index('id')

error = []

for i in range(1, len(track_meta_data)+1):
    track_id = track_meta_data[i].get('id')
    track_min = track_meta_data[i].get('minXVelocity')
    track_max = track_meta_data[i].get('maxXVelocity')
    track_mean = track_meta_data[i].get('meanXVelocity')
    sumo_min = sumo_stats.loc[track_id]['min']
    sumo_max = sumo_stats.loc[track_id]['max']
    sumo_mean = sumo_stats.loc[track_id]['mean']
    error.append(
        {"id": track_id,
         "err_min": sumo_min - track_min,
         "err_max": sumo_max - track_max,
         "err_mean": sumo_mean - track_mean
         }
    )

pd.DataFrame(error).to_csv(
    results_dir + dataset_id + "_speed_error.csv",
    index=False)

total_min = 0
total_max = 0
total_mean = 0
errors = pd.DataFrame(error)

#for index in errors['err_min'].index:
#   total_min += np.square(errors['err_min'].get(index))
#rmse_min = np.sqrt(total_min / len(errors))
#print('RMSE for min ' + str(rmse_min))

#for index in errors['err_max'].index:
#    total_max += np.square(errors['err_max'].get(index))
#rmse_max = np.sqrt(total_max / len(errors))
#print('RMSE for max ' + str(rmse_max))

for index in errors['err_mean'].index:
    total_mean += np.square(errors['err_mean'].get(index))
rmse_mean = np.sqrt(total_mean / len(errors))
print('RMSE for mean ' + str(rmse_mean))
#pi = (rmse_mean + rmse_max + rmse_min) / 3
#print(pi)

#if plot is True:
    #errors = pd.DataFrame(error)
    #print(errors)
    #plt.figure(1)
    #plt.hist(errors['err_min'])
    #plt.title('errors in minimum value')

    #plt.figure(2)
    #plt.hist(errors['err_max'])
    #plt.title('errors in maximum value')

    #plt.figure(3)
    #plt.hist(errors['err_mean'])
    #plt.title('errors in mean value')
    #plt.show()
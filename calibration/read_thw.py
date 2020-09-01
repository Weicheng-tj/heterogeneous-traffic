# plot the distribution of minimum THW in highD
import statistics
import csv
import numpy as np
import matplotlib.pyplot as plt


data_id = []
for number in np.arange(60):
    data_id.append((str((number + 1)) if (number + 1) >= 10 else "0" + str(number + 1)))



car_thw = []
truck_thw = []

def read_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vId = row['id']
            vType = row['class']
            vTHW = round(float(row['minTHW']), 2)
            vTTC = float(row['minTTC'])
            vDHW = float(row['minDHW'])

            if vType == 'Car':
                if vTHW > 0:
                    car_thw.append(vTHW)
            else:
                if vTHW > 0:
                    truck_thw.append(vTHW)



for i in data_id:
    highd_filename = i + "_tracksMeta.csv"
    read_csv(highd_filename)

weights_car = np.ones_like(car_thw)/float(len(car_thw))
weights_truck = np.ones_like(truck_thw)/float(len(truck_thw))

print(np.median(car_thw))
print(np.mean(car_thw))
print(np.median(truck_thw))
print(np.mean(truck_thw))

plt.figure()
p1 = plt.hist(car_thw, bins=40, range=(0, 15), weights=weights_car)
p2 = plt.hist(truck_thw, bins=40, range=(0, 15), weights=weights_truck)
plt.title('Distribution of minimum THW in highD')
plt.legend( labels=['car', 'truck'])
plt.show()




# Part. 1
#=======================================
# Import module
# csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061155.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = data[:10]  # target_data={'C0A880':'PRES'...}
pres = 0
time = 0

# if ['PRES']=='-99.000' or data[i]['PRES']=='-999.000' remove data[i]
res = [i for i in data if not ((i['PRES'] == '-99.000')|(i['PRES'] == '-999.000'))]

# for i in range(len(data)):
# print(data[i]['station_id'])
target_data = []
target_C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', res))
target_C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', res))
target_C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', res))
target_C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', res))
target_C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', res))

for i in range(len(target_C0A880)):
    pres = pres + float(target_C0A880[i]['PRES'])   # calculate the sum of the PRES
    time = 1
target_data.append('C0A880')
if time == 1:
    target_data.append(pres/len(target_C0A880))     # find out the mean of the PRES
else:
    target_data.append('\'None\'')

time = 0
pres = 0

for i in range(len(target_C0F9A0)):
    pres = pres + float(target_C0F9A0[i]['PRES'])   # calculate the sum of the PRES
    time = 1
target_data.append('C0F9A0')
if time == 1:
    target_data.append(pres/len(target_C0F9A0))     # find out the mean of the PRES   
else:
    target_data.append('\'None\'')

time = 0
pres = 0

for i in range(len(target_C0G640)):
    pres = pres + float(target_C0G640[i]['PRES'])   # calculate the sum of the PRES
    time = 1
target_data.append('C0G640')
if time == 1:
    target_data.append(pres/len(target_C0G640))     # find out the mean of the PRES
else:
    target_data.append('\'None\'')

time = 0
pres = 0

for i in range(len(target_C0R190)):
    pres = pres + float(target_C0R190[i]['PRES'])   # calculate the sum of the PRES
    time = 1
target_data.append('C0R190')
if time == 1:
    target_data.append(pres/len(target_C0R190))     # find out the mean of the PRES
else:
    target_data.append('\'None\'')

time = 0
pres = 0

for i in range(len(target_C0X260)):
    pres = pres + float(target_C0X260[i]['PRES'])   # calculate the sum of the PRES
    time = 1
target_data.append('C0X260')
if time == 1:
    target_data.append(pres/len(target_C0X260))     # find out the mean of the PRES
else:
    target_data.append('\'None\'')

# Part. 4
#=======================================
# Print result
# target_data[1,3,5,7,9]store the mean of presure
# target_data[0,2,4,6,8]store the ID of station

print('[', end='')
print('[',end='')
print('\'',end='')
print('C0A880',end='')          # print [['C0A880', 1007.65],
print('\'',end='')
print(',',end='')
print(target_data[1],end='')
print('],',end='')

print('[',end='')
print('\'',end='')
print('C0F9A0',end='')          # print ['C0F9A0', 1010.65], 
print('\'',end='')
print(',',end='')
print(target_data[3],end='')
print('],',end='')

print('[',end='')
print('\'',end='')
print('C0G640',end='')          # print ['C0G640', 995.1], 
print('\'',end='')
print(',',end='')
print(target_data[5],end='')
print('],',end='')

print('[',end='')
print('\'',end='')
print('C0R190',end='')          # print ['C0R190', 1017.95], 
print('\'',end='')
print(',',end='')
print(target_data[7],end='')
print('],',end='')

print('[',end='')
print('\'',end='')
print('C0X260',end='')          # print ['C0X260', 'None']]
print('\'',end='')
print(',',end='')
print(target_data[9],end='')
print(']]')
#========================================

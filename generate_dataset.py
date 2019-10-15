import pandas as pd
import numpy as np
from random import randint
import datetime
from matplotlib import  pyplot as plt
import  matplotlib
matplotlib.use('TkAgg')


def main():
	timestamp_list, cpu_value_list, memory_value_list, network_value_list = prepareDataSets(10000)
	
	ds= dataset_compose(timestamp_list, cpu_value_list, memory_value_list, network_value_list)
	
	CheckCorrelation(ds)

	# if required to plot a chart with the metrics.
	#plotme(timestamp_list, cpu_value_list, memory_value_list)


def prepareDataSets(count):
	records_count = count
	time_now = datetime.datetime.now()
	id_list = list(i for i in range(1,records_count))
	timestamp_list = generate_timestamplist(time_now, records_count)
	cpu_value_list = list(randint(30,80) for i in range(1,records_count))
	memory_value_list = list(randint(20,90) for i in range(1,records_count))
	network_value_list = list(randint(20,70) for i in range(1,records_count))

	return timestamp_list, cpu_value_list, memory_value_list, network_value_list


def plotme(timestamp_list1, cpu_value_list1, memory_value_list1):
	try:
		plt.plot(timestamp_list1, cpu_value_list1, timestamp_list1, memory_value_list1)
		plt.ylabel('CPU Utilization %')
		plt.xlabel('Time')
		plt.show()	
		return True
	except:
		return False

def dataset_compose(timestamps, cpus, mems, net):
	#return zip(timestamps,cpus, mems)
	return zip(cpus, mems, net)

def generate_timestamplist(time_now, therangerecords):

	updatedtime = time_now
	timestamp_records = []
	for i in range(1, therangerecords):
		updatedtime = updatedtime + datetime.timedelta(0,120)
		timestamp_records.append(updatedtime)

	return timestamp_records


def CheckCorrelation(metricds):
	try:
		#data = pd.read_csv('https://www.dropbox.com/s/4jgheggd1dak5pw/data_visualization.csv?raw=1', index_col=0)
		data = pd.DataFrame(metricds)

		print(type(data))
		
		print(data)
		corr = data.corr()
		fig = plt.figure()
		ax = fig.add_subplot(111)
		cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
		fig.colorbar(cax)
		ticks = np.arange(0,len(data.columns),1)
		ax.set_xticks(ticks)
		plt.xticks(rotation=90)
		ax.set_yticks(ticks)
		ax.set_xticklabels(data.columns)
		ax.set_yticklabels(data.columns)
		plt.show()
		return True
	except:
		return False


main()
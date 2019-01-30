import pickle
import os
import matplotlib.pyplot as plt
import Filtering as fft


def plotData(data, filename):
	plt.close()
	plt.style.use('ggplot')
	plt.rcParams['axes.facecolor']='white'	
	plt.rcParams['grid.color']='gainsboro'
	plt.plot(data)
	plt.savefig(filename)

persons = os.listdir("./eeg_full")
persons.sort()
alcoholicData = {}
controlGroupData = {}
graphDir = "./Graphs"
alcoholDir = graphDir + "/Alcoholic"
controlDir = graphDir + "/Control"

if(not os.path.isdir(graphDir)):
	os.mkdir(graphDir)

if(not os.path.isdir(alcoholDir)):
	os.mkdir(alcoholDir)

if(not os.path.isdir(controlDir)):
	os.mkdir(controlDir)

for person in persons:
	print(person)
	if(person[3] == 'a'):
		alcoholicFlag = True
	else:
		alcoholicFlag = False

	files = os.listdir("./eeg_full/" + person)
	files.sort()
	for file in files:
		print(person, file)
		f = open("./eeg_full/" + person + "/" + file)
		file_data = f.readlines()
		try:
			typeOfTest = file_data[3].split()[1]
			typealcoholDir = alcoholDir + "/" + typeOfTest 
			typecontrolDir = controlDir + "/" + typeOfTest 
		except:
			continue
		if(not os.path.isdir(typealcoholDir)):
			os.mkdir(typealcoholDir)
		if(not os.path.isdir(typecontrolDir)):
			os.mkdir(typecontrolDir)
		channel = ''
		channel_data = []
		for i in range(4,len(file_data)):
			line_data = file_data[i].split()
			if(line_data[0] == '#'):
				if(channel != ''):
					channelalcoholDir = typealcoholDir + "/" + channel
					channelcontrolDir = typecontrolDir + "/" + channel

					if(not os.path.isdir(channelalcoholDir)):
						os.mkdir(channelalcoholDir)
					if(not os.path.isdir(channelcontrolDir)):
						os.mkdir(channelcontrolDir)
					if(alcoholicFlag):
						with open(channelalcoholDir + "/" + file + ".pickle", 'wb') as f:
							pickle.dump(channel_data, f)
					else:
						with open(channelcontrolDir + "/" + file + ".pickle", 'wb') as f:
							pickle.dump(channel_data, f)


				channel_data = []
				channel = line_data[1]
			else:
				channel_data.append(float(line_data[3]))

with open('./data.pickle', 'wb') as f:
	pickle.dump(alcoholicData, controlGroupData, f)

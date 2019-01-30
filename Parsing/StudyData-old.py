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
data = {}
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
	data[person] = {}
	if(person[3] == 'a'):
		data[person]["Alcoholic"] = True
		personDir = alcoholDir + "/" + person

	else:
		data[person]["Alcoholic"] = False
		personDir = controlDir + "/" + person
	data[person]["Number"] = person
	if(not os.path.isdir(personDir)):
		os.mkdir(personDir)
	files = os.listdir("./eeg_full/" + person)
	files.sort()
	data[person]["trials"] = []
	for file in files:
		print(person, file)
		trialData = {}
		f = open("./eeg_full/" + person + "/" + file)
		file_data = f.readlines()
		trialData["Type"] = file_data[3].split()[1]
		trialData["Trial_Number"] = file_data[3].split()[-1]
		trialDir = personDir + "/" + str(trialData["Trial_Number"])
		if(not os.path.isdir(trialDir)):
			os.mkdir(trialDir)
		trialData["Channels"] = {}
		channel = ''
		for i in range(4,len(file_data)):
			line_data = file_data[i].split()
			if(line_data[0] == '#'):
				# if(channel != ''):
				# 	plotData(trialData["Channels"][channel], trialDir + "/" + channel + ".png")
				trialData["Channels"][line_data[1]] = []
				channel = line_data[1]
			else:
				trialData["Channels"][channel].append(float(line_data[3]))
		data[person]["trials"].append(trialData)

with open('./data.pickle', 'wb') as f:
	pickle.dump(data, f)

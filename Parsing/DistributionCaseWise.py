import pickle
import os
import matplotlib.pyplot as plt
import Filtering as fft

def makeDir(name):
	if(not os.path.isdir(name)):
		os.mkdir(name)
	return name

def plotData(data, filename):
	plt.close()
	plt.style.use('ggplot')
	plt.rcParams['axes.facecolor']='white'	
	plt.rcParams['grid.color']='gainsboro'
	plt.plot(data)
	plt.savefig(filename)

persons = os.listdir("./eeg_full")
persons = persons[1:]
persons.sort()
alcoholicData = {}
controlGroupData = {}
graphDir = makeDir("./CaseWiseDistribution")
alcoholDir = makeDir(graphDir + "/Alcoholic")
controlDir = makeDir(graphDir + "/Control")
errCount = 1

for person in persons:
	print(person)
	if(person[3] == 'a'):
		alcoholicFlag = True
		groupDir = alcoholDir
	else:
		alcoholicFlag = False
		groupDir = controlDir

	files = os.listdir("./eeg_full/" + person)
	files = files[1:]
	files.sort()
	for file in files:
		print(person, file)
		f = open("./eeg_full/" + person + "/" + file)
		file_data = f.readlines()
		try:
			text = file_data[3]
			if(text.find("err") != -1):
				print("errorFile", errCount)
				errCount += 1
			elif(text.find("S1") != -1):
				typeOfTest = "S1"
			elif(text.find("S2 match") != -1):
				typeOfTest = "S2 match"
			elif(text.find("S2 nomatch") != -1):
				typeOfTest = "S2 nomatch"
			else:
				print("Here")
				continue
			typeDir = makeDir(groupDir + "/" + typeOfTest)
			personDir = makeDir(typeDir + "/" + person)
		except:
			continue

		try:
			trialNumber = text.split(' ')[-1][:-1]
		except:
			trialNumber = 'Unknown'
		trialDir = makeDir(personDir + "/" + str(trialNumber))
		channel = ''
		channel_data = []
		for i in range(4,len(file_data)):
			line_data = file_data[i].split()
			if(line_data[0] == '#'):
				if(channel != ''):
					with open(trialDir + "/" + channel + ".pickle", 'wb') as f:
						pickle.dump(channel_data, f)

				channel_data = []
				channel = line_data[1]
			else:
				channel_data.append(float(line_data[3]))
		if(channel != ''):
			with open(trialDir + "/" + channel + ".pickle", 'wb') as f:
				pickle.dump(channel_data, f)

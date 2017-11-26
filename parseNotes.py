def parseChords():
	fileIn = open('clairNotes.txt', 'r')
	line = fileIn.readline()
	chord = []
	adjacencyMatrix = {}
	
	#creates empty adjacency matrix
	#fills matrix with zeroes
	for i in range(27,98):
		adjacencyMatrix.update({i:{}})
		for j in range(27, 98):
			adjacencyMatrix[i].update({j:0})
	


	while line: #this is a string
		#this line should not contain time = 0
		note_starti = line.index("note=")+5
		time_starti = line.index("time=")+5

		noteStr = line[note_starti: note_starti+2] #cuts so only pitch remains
		note_int = int(noteStr)	 	
		time_str = line[time_starti:] 
		time_int = int(time_str)

		print(chord)
	
		#if time != 0 then reset chord list
		#need base case for first nonzero #
		#or just take an L on the 1st note

		if time_int == 0: 
			chord.append(note_int)
		elif chord != []:
			chord.sort()
			chord.reverse()
			key_int = chord[0] #the assumption that the upper note is melody
			chord.remove(key_int)
			#all other notes are harmony
		#	if not adjacenceyMatrix.has_key(key_int):
		#		adjacencyMatrix.update({key_int:{}})
				#AM's values are 
			for note in chord:
		#		if not adjacencyMatrix[key_int].has_key(note):
		#			adjacencyMatrix[key_int].update({note, 0})

				print(note)
		
				x = adjacencyMatrix[key_int][note] #x denotes occurrences
				x = x + 1
				adjacencyMatrix[key_int][note] = x
				#frequency of notes in chords is updated

			chord = []
		line = fileIn.readline()

	return adjacencyMatrix

	#when there are no more lines, all of the chord frequencies should be mapped
	#although.....this is a problem bc a lot of chords have the same top note, so i can't just pick random notes T_T i fucked up

def printMatrix(am): #am = adjacencyMatrix
	for i in range(27, 98):
		for j in range(27, 98):
			print am[i][j],

	
def makeProbMatrix(am): #am is adjacency matrix
	
	for i in range(27,98):

		#this gets sum of all counts in a row
		sum_ = 0
		myDict = am[i]
		for j in range(27,98):
			sum_ = sum_ + myDict[j]

		#this turns all sums into a probability
		for j in range(27,98):
			myDict[j] = myDict[j] / sum_


	return am
		


def parseMelody():
			
	fileIn = open("clairHigh.txt", "r")
	prev = fileIn.readline()
	starti = prev.index("note=")+5
	
	adjacencyMatrix = {}

	for i in range(27,98):
		adjacencyMatrix.update({i: {}})
		for j in range(27,98):
			adjacencyMatrix[i].update({j:0})


	
	prev_int = int(prev[starti : starti+2])
	
	line = fileIn.readline()	
	while line: #this is a string
		curr_int = int(line[starti : starti +2])
		x= adjacencyMatrix[prev_int][curr_int]
		x= x + 1
		adjacencyMatrix[prev_int][curr_int] = x
		
		prev_int = curr_int
		line = fileIn.readline()

	return adjacencyMatrix


if __name__ == "__main__":
	am = parseMelody()
	printMatrix(am)

def doAMarkovChain(am):
	vec initState = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
		
	

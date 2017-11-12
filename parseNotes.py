def parseChords():
	fileIn = open('clairNotes.txt', 'r')
	line = fileIn.readline()
	chord = []
	adjacencyMatrix = {}

	while line: #this is a string
		#this line should not contain time = 0
		note_starti = line.index("note=")
		time_starti = line.index("time=")

		note_str = line[note_starti: note_starti+2] #cuts so only pitch remains
		note_int = int(note_str)	 	
		time_str = line[time_starti:] 
		time_int = int(time_str)

	
	
		#if time != 0 then reset chord list
		#need base case for first nonzero #
		#or just take an L on the 1st note

		if time_int == 0: 
			chord.append(note_int)
		else:
			chord.sort()
			chord.reverse()
			key_int = chord[0] #the assumption that the upper note is melody
			chord.remove(key_int)
			#all other notes are harmony
			if not adjacenceyMatrix.has_key(key_int):
				adjacencyMatrix.update({key_int:{}})
				#AM's values are 
			for note in chord:
				if not adjacencyMatrix[key_int].has_key(note):
					adjacencyMatrix[key_int].update({note, 0})
		
				x = adjacencyMatrix[key_int][note] #x denotes occurrences
				x = x + 1
				adjacencyMatrix[key_int][note] = x
				#frequency of notes in chords is updated

		line = fileIn.readline()

	#when there are no more lines, all of the chord frequencies should be mapped
	#although.....this is a problem bc a lot of chords have the same top note, so i can't just pick random notes T_T i fucked up

"""
def parseMelody():
	fileIn = open("clairHigh.txt", "r")
	prev = fileIn.readLine()
	starti = prev.index("note=")
	
	adjacencyMatrix = {}
	
	prev_int = int(prev[starti : starti+2])
	
	line = fileIn.readLine()	
	while line: #this is a string
		curr_int = int(line[starti : starti +2])
		
		if not adjacencyMatrix.has_key(prev_int):
			adjacencyMatrix.update({prev_int, {}})
		
		if not adjacencyMatrix[prev_int].has_key(curr_int):
			adjacencyMatrix[prev_int].update({curr_int, 1})
		else:
			x = adjacencyMatrix[prev_int][curr_int]
			x= x + 1
			adjacencyMatrix[prev_int][curr_int] = x
		
		prev_int = curr_int
		line = fileIn.readLine()
	
"""

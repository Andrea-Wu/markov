from mido import MidiFile

myMid = MidiFile('deb_clai.mid')

for track in (myMid.tracks):
	for message in track:
		print(message)


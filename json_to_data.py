import os
import re
import csv
from pathlib import Path
import datetime

data = open("data.csv", "w")
data.truncate()
title = "child__hashed_id,condition,counterbalance,attn1,attn2,test,attn3,rachel_false_belief,diana_false_belief,allie_false_belief,num_speakers,coding_experience,smartphone_frequency,smart_speaker_frequency,voice_assistant_frequency,pass_attn1,pass_attn2,pass_attn3,pass_all_attn,chose_song_1\n"
data.write(title)
path = os.path.expanduser("~/Downloads/Guess-What-Happens-Next_framedata_per_session")
for file in os.listdir(path):
	if file.endswith(".csv"):
		with open(path + "/" + file) as csvfile:
			reader = csv.DictReader(csvfile)
			id = ""
			condition = ""
			counterbalance = 0
			attn1 = 0
			attn2 = 0
			test = 0
			attn3 = 0
			rachel_false_belief = 0
			diana_false_belief = 0
			allie_false_belief = 0
			num_speakers = ""
			coding_experience = ""
			smartphone_frequency = ""
			smart_speaker_frequency = ""
			voice_assistant_frequency = ""
			current_data = False
			for row in reader:
				id = row['child_hashed_id']
				if row['key'] == "timestamp":
					study_start = datetime.datetime.strptime('2023-11-22', "%Y-%m-%d")
					date = datetime.datetime.strptime(row["value"], "%Y-%m-%dT%H:%M:%S.%fZ")
					if date > study_start: 
						current_data = True
				if row['key'] == "videoShown" and row['frame_id'] == "11-alexa-protocol":
					video = row["value"]
					matches = re.search("([a-zA-Z]+)-CB([0-9])",video)
					condition = matches.group(1)
					counterbalance = int(matches.group(2))
				if row['key'] == "selectedImage":
					frame_id = row['frame_id']
					if frame_id == "12-alexa-protocol":
						value = row['value']
						if value == "left":
							attn1 = "wheels"
						elif value == "middle":
							attn1 = "twinkle"
						elif value == "right":
							attn1 = "spider"
					elif frame_id == "15-alexa-protocol":
						value = row['value']
						if value == "left":
							attn2 = "wheels"
						elif value == "middle":
							attn2 = "twinkle"
						elif value == "right":
							attn2 = "spider"
					elif frame_id == "18-alexa-protocol":
						value = row['value']
						if value == "left":
							test = "wheels"
						elif value == "right":
							test = "spider"
					elif frame_id == "22-null":
						selectedImage = row['value']
						if selectedImage == "left":
							attn3 = 1
					elif frame_id == "25-null":
						selectedImage = row['value']
						if selectedImage == "left":
							rachel_false_belief = 1
					elif frame_id == "28-null":
						selectedImage = row['value']
						if selectedImage == "left":
							diana_false_belief = 1
					elif frame_id == "31-null":
						selectedImage = row['value']
						if selectedImage == "middle":
							allie_false_belief = 1
				if row['frame_id'] == "34-parent-survey":
					if row['key'] == "formData.num_speakers":
						num_speakers = row['value']
					elif row['key'] == "formData.coding_experience":
						coding_experience = "\"" + row['value'] + "\""
					elif row['key'] == "formData.smartphone_frequency":
						smartphone_frequency = row['value']
					elif row['key'] == "formData.smart_speaker_frequency":
						smart_speaker_frequency = row['value']
					elif row['key'] == "formData.voice_assistant_frequency":
						voice_assistant_frequency = row['value']
			if not current_data:
				print("Ignoring data from earlier study version")
				continue
			pass_attn1 = 0
			pass_attn2 = 0
			pass_attn3 = 0
			pass_all_attn = 0
			if counterbalance is 1 or counterbalance == 3:
				correct_song_1 = "spider"
				correct_song_2 = "wheels"
			else:
				correct_song_1 = "wheels"
				correct_song_2 = "spider"
			if attn1 == correct_song_1:
				pass_attn1 = 1
			if attn2 == correct_song_2:
				pass_attn2 = 1
			pass_attn3 = attn3
			if pass_attn1 + pass_attn2 + pass_attn3 == 3:
				pass_all_attn = 1
			if test == correct_song_1:
				chose_song_1 = 1
			else:
				chose_song_1 = 0
			csv_str = str(id) + "," + condition + "," + str(counterbalance) + "," + str(attn1) + "," + str(attn2) + "," + str(test) + "," + str(attn3) + "," + str(rachel_false_belief) + "," + str(diana_false_belief) + "," + str(allie_false_belief) + "," + num_speakers + "," + coding_experience + "," + smartphone_frequency + "," + smart_speaker_frequency + "," + voice_assistant_frequency + "," + str(pass_attn1) + "," + str(pass_attn2) + "," + str(pass_attn3) + "," + str(pass_all_attn) + "," + str(chose_song_1) + "\n"
			data.write(csv_str)
data.close()











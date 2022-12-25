import os
import re
import csv
from pathlib import Path

data = open("data.csv", "w")
data.truncate()
title = "child__hashed_id,condition,counterbalance,attn1,attn2,test,diverse_desires,implicit_false_belief,diverse_beliefs,diana_false_belief_location,diana_false_belief_control,allie_false_belief_location,num_speakers,coding_experience,smartphone_frequency,smart_speaker_frequency,voice_assistant_frequency\n"
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
			diverse_desires_selected_snack = ""
			diverse_desires = 0
			implicit_false_belief = 0
			diverse_beliefs_selected_location = ""
			diverse_beliefs = 0 # not yet
			diana_false_belief_location = 0
			diana_false_belief_control = 0
			allie_false_belief_location = 0
			num_speakers = ""
			coding_experience = ""
			smartphone_frequency = ""
			smart_speaker_frequency = ""
			voice_assistant_frequency = ""
			for row in reader:
				id = row['child_hashed_id']
				if row['key'] == "videoShown" and row['frame_id'] == "11-alexa-protocol":
					video = row["value"]
					matches = re.search("([a-zA-Z]+)-CB([0-9])",video)
					condition = matches.group(1)
					counterbalance = matches.group(2)
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
					elif frame_id == "26-null":
						selectedImage = row['value']
						if selectedImage == "left":
							implicit_false_belief = 1
					elif frame_id == "34-null":
						selectedImage = row['value']
						if selectedImage == "left":
							diana_false_belief_location = 1
					elif frame_id == "36-null":
						selectedImage = row['value']
						if selectedImage == "right":
							diana_false_belief_control = 1
					elif frame_id == "38-null":
						selectedImage = row['value']
						if selectedImage == "middle":
							allie_false_belief_location = 1
					elif frame_id == "21-TOM-booklet-2-snack-select":
						diverse_desires_selected_snack = row['value']
					elif frame_id == "24-TOM-booklet-3-snack-response":
						diverse_desires_response_snack = row['value']
						if diverse_desires_selected_snack != diverse_desires_response_snack:
							diverse_desires = 1
					elif frame_id == "29-TOM-booklet-5-backpack-select":
						diverse_beliefs_selected_location = row['value']
					elif frame_id == "32-TOM-booklet-6-backpack-response":
						diverse_beliefs_response_location = row['value']
						if diverse_beliefs_selected_location != diverse_beliefs_response_location:
							diverse_beliefs = 1
				if row['frame_id'] == "46-parent-survey":
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
			if test == 0:
				print("Ignoring data from pilot 1...")
				continue
			csv_str = str(id) + "," + condition + "," + counterbalance + "," + str(attn1) + "," + str(attn2) + "," + str(test) + "," + str(diverse_desires) + "," + str(implicit_false_belief) + "," + str(diverse_beliefs) + "," + str(diana_false_belief_location) + "," + str(diana_false_belief_control) + "," + str(allie_false_belief_location) + "," + num_speakers + "," + coding_experience + "," + smartphone_frequency + "," + smart_speaker_frequency + "," + voice_assistant_frequency + "\n"
			data.write(csv_str)
data.close()











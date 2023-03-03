
import json
import pandas as pd
import sys
import os

dataset = pd.read_csv("../audiocaps/dataset/train.csv")

with open("../audiocaps_train/metadata.jsonl", 'w') as f:
    for _, row in dataset.iterrows():

        file_name = row['youtube_id'] + '.wav'
        full_path = "../audiocaps_train/" + file_name

        if not os.path.isfile(full_path):
            continue

        jsonline = {
            "file_name": file_name,
            "text": row['caption'],
        }

        f.write( json.dumps(jsonline) + "\n" )


# todo prepare spectrogram dataset
# ~/anaconda3_new/envs/riffusion/bin/python3.9 -m riffusion.cli audio-to-image --audio ../audiocaps_train/000AjsqXq54.wav --image ./000AjsqXq54.jpg

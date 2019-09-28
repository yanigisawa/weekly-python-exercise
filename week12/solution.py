import os
import json
import hashlib
from flask import Flask, escape, request
import pickle

app = Flask(__name__)

@app.route('/scan/{directory}')
def scan(directory):
    dir_files = []
    if not os.path.exists(directory):
        return f"Directory '{directory}' does not exist"
    for root, _, files in os.walk(directory, topdown=False):
        for name in files:
            full_path = os.path.join(root, name)
            sha_hash = hashlib.sha1(open(full_path, 'rb').read())

            file_info = {
                "fileName": name,
                "sha1": sha_hash.hexdigest()
            }
            dir_files.append(file_info)
    with open('files.bin', 'wb') as f:
        pickle.dump(dir_files, f)
    return dir_files


@app.route('/scan/{directory}')
def rescan(directory):
    dir_files = []
    if not os.path.exists(directory):
        return f"Directory '{directory}' does not exist"
    with open('files.bin', 'rb') as f:
        existing = pickle.load(f)
    for root, _, files in os.walk(directory, topdown=False):
        for name in files:
            full_path = os.path.join(root, name)
            curr_file = [f for f in existing if f['fileName'] == name]
            new_sha1 = hashlib.sha1(open(full_path, 'rb').read()).hexdigest()
            if len(curr_file) == 1 and curr_file[0]['sha1'] == new_sha1:
                continue
            # print(f"Name: {name} - sha1: {curr_file[0]['sha1']} - newSha: {new_sha1}")
            dir_files.append({
                "fileName": name,
                "sha1": new_sha1
            })
    return json.dumps(dir_files)

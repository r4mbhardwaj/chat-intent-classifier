import json
import os

folder = "convo/expressions/"

files = []
files.extend([os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(".txt")])

    
labels = []
sentences = []

for file_path in files:
    with open(file_path) as f:
        data = f.read()

    for line in data.split('\n'):
        if len(line.strip()) > 0:
            if line.startswith('\xa0'): # if the line starts with a space
                sentences.append({line[1:]:labels[-1]})
            elif line: # if the line starts with a letter
                try:
                    # labels.pop()
                    pass
                except:
                    pass
                if 'http' not in line:
                    labels.append(line)
                    print(labels[-1])

# print(sentences)

label_data = {}

for sentence in sentences:
    print(sentence)
    label = list(sentence.values())[0].replace(':', '')
    if label not in label_data:
        label_data[label] = []
    else:
        label_data[label].extend(list(sentence.keys()))
    print()

print(label_data)

for a in label_data:
    print(a, label_data[a])
    print()
    
with open('label_data.json', 'w') as f:
    json.dump(label_data, f)
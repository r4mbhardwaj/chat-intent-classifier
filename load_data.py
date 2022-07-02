import json

# read json file 
with open('label_data.json') as f:
    data = json.load(f)



training_sentences = []
training_labels = []

labels = []

for label in data:
    for sentence in data[label]:
        training_sentences.append(sentence)
        training_labels.append(label)
        if label not in labels:
            labels.append(label)


for index, a in enumerate(training_sentences):
    print(a, training_labels[index])

num_classes = len(labels)
print(f"num of classes: {num_classes}")

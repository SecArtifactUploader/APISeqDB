import pickle
import json

def load_data(file_path='./Mul_label.pk', json_path='./compactid2action.json', get_action=True, get_label=True):
    label_dict = ['', 'SMS-Related', 'Information Gathering', 'Rogue Behavior', 'Phone-Related', 'Re-Infection', 'System Corruption']
    with open(file_path,'rb') as f:
        data = pickle.load(f)
    with open(json_path,'r') as f:
        id2ac = json.load(f)
    
    # convert compactid to action format.
    seq = []
    if get_action:
        for i in data[0]:
            temp_list = []
            for j in i:
                temp_list.append(id2ac[str(j)])
            seq.append(temp_list)
    else:
        seq = data[0]
    
    # convert label to category.
    label = []
    if get_label:
        for i in data[1]:
            label.append(label_dict[i])
    else:
        label = data[1]
    
    # return two list: sequence and label. They have the same length.
    return [seq,label]

data = load_data()
print(data[0][1573])
print(data[1][1573])
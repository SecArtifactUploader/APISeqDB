import pickle
import json
from tqdm import tqdm

class Dataset:
    """
    Store the information of a dataset.
    """
    def __init__(self, data, s_label, label, pkg_names, time, source, family):
        #label:0/1 (0->mal 1->nor)
        self.SegmentsList = data #class 'numpy.ndarray' API Sequence
        self.SegmentsLabels = s_label #class 'numpy.ndarray' API Sequence Labels
        self.apkLabel = label #class 'numpy.float64' APP Label 
        self.pkgNames = pkg_names #class 'str' APP unique id
        self.pkgTime = time #class 'str' APP time xxxx(year)
        self.pkgSources = source #class 'str' APP source
        self.family = family #class 'str' APP family. Valid only when apkLabel == 0 

def load_data(file_path='./APISeqDB.pk', json_path='./compactid2action.json', get_action=True, get_label=False):
    '''
    return a list. Each item is a 'class Dataset',which contain an app info.
    '''
    with open(file_path,'rb') as f:
        data = pickle.load(f)

    # convert compactid to action format.
    if get_action:
        with open(json_path, 'r') as f:
            id2ac = json.load(f)
        for i in tqdm(data):
            new_list = []
            for j in i.SegmentsList:
                temp_list = []
                for k in range(256):
                    temp_list.append(id2ac[str(j[k])])
                new_list.append(temp_list)
            i.SegmentsList = new_list
    # convert 0/1 label to malicious/normal.
    if get_label:
        for i in data:
            if i.apkLabel==0:
                i.apkLabel = 'malicious'
            else:
                i.apkLabel = 'normal'
            new_label = []
            for j in range(len(i.SegmentsLabels)):
                temp_label = []
                if i.SegmentsLabels[j] == 0:
                    temp_label.append('malicious')
                else:
                    temp_label.append('normal')
                new_label.append(temp_label)
            i.SegmentsLabels = new_label
    return data

data = load_data(get_label=True)

print(data[203].SegmentsList[0])
print(data[203].SegmentsLabels[0])
print(data[203].apkLabel)
print(data[203].pkgNames)
print(data[203].pkgTime)
print(data[203].pkgSources)
print(data[203].family)

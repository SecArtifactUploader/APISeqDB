# Malware detection dataset

The datasets $Dc$ and $Df$ use the same app samples in MDT.pk.

`MDT.pk` has 20,000 apps for training set and 10,000 apps for testing set.

The sequence in $D_c$ is the original data in APISeqDB.

The sequence in $D_f$ is obtained by merging all the fine-grained sequences from the corresponding app in APISeqDB.


```python
class Dataset:
    """
    Store the information of a dataset.
    """
    def init(self, data, s_label, label, pkg_names, time, source, family):
        #label:0/1 (0->mal 1->nor)
        self.SegmentsList = data #class 'numpy.ndarray' API Sequence
        self.SegmentsLabels = s_label #class 'numpy.ndarray' API Sequence Labels
        self.apkLabel = label #class 'numpy.float64' APP Label
        self.pkgNames = pkg_names #class 'str' APP unique id
        self.pkgTime = time #class 'str' APP time xxxx(year)
        self.pkgSources = source #class 'str' APP source
        self.family = family #class 'str' APP family. Valid only when apkLabel == 0
```

When you want to load our data, please follow the guide of demo `MDT_load.py`

Here is an example script provided for loading the dataset, `MDT_load.py`. It calls the `load_data()` function to load the dataset. You can pass the `file_path` parameter to specify the dataset path and the `json_path` parameter to specify the mapping table for IDs and actions, which is `compactid2action.json`. Set `get_action=True` if you need to convert compact IDs to actions, and set `get_label=True` if you need to convert numeric labels to text categories. Please note that mapping compact IDs to actions might take a considerable amount of time, approximately 10 minutes.

## Case Study

In the given case, `MDT` stores two lists(training set and testing set) where each element is an instance of the `Dataset` class. Here is an example.

```shell
['bindService', 'bindService', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getLinkProperties', 'registerReceiver', 'registerReceiver', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getApplicationRestrictions', 'getLinkProperties', 'registerReceiver', 'registerReceiver', 'registerReceiver', 'registerReceiver', 'registerReceiver', 'registerReceiver', 'registerContentObserver', 'getNetworkInfo', 'getLinkProperties', 'addWindowHijack', 'registerReceiver', 'registerReceiver', 'addWindow', 'registerReceiver', 'registerReceiver', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getLinkProperties', 'unbindService', 'unbindService', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerContentObserver', 'registerReceiver', 'registerReceiver', 'unbindService', 'unbindService', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getNetworkInfo', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getNetworkInfo', 'getLinkProperties', 'getNetworkInfo', 'getNetworkInfo', 'getLinkProperties', 'setComponentHideIcon', 'addWindow', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
sequence's label: [0]
app's label: 0
app's md5: 1569bdb2177bc08cbebd6e0afa9ba265
app's birthday: 2018
app's source: VirusTotal
app's famliy: rotexy
```


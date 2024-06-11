# APISeqDB: A Semantic-preserving and Fine-grained Behavior Dataset for Facilitating Data-driven Android Malware Analysis

A Fine-grained and Semantic-perserving Android App Behavior Dataset.

## Background

Data-driven methods, especially those employing artificial intelligence (AI) techniques, have seen growing application in the field of malware detection and analysis. However, the absence of high-quality and large-scale datasets has limited the breadth and scope of their deployment in both academia and industry.

We presents *APISeqDB*, a large-scale yet semantic-preserving and fine-grained behavior dataset to facilitate advanced data-driven Android malware analysis. We build a dataset with more than 1.66 million action sequences from 218,332 real-world Android apps at a low cost. These data sets were created between 2018 and 2023. 5 years and above 10 experts are participating in this construction job.

We have release our datasets as open-source to foster research in the field of data-driven malware analysis at this page.

## Dataset

There are four sub-directories in our folder. They are `APISeqDB`, `MDT`, `Mul `and `LLM`.  The description of these folders are below.

| Directory Name | Major File Prefix | Detailed Information                                                                                                                                                                                                      |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /main          | APISeqDB.pk       | Whole dataset, A Fine-grained Behavior Dataset for Facilitating Data-Driven Android Malware Analysis.                                                                                                                     |
| /MDT           | MDT.pk         | Apps for the train and test set used in malware detection tasks. The dataset included in MDT directory is used to evaluate the performance of our dataset in classical machine learning android malware detection task. |
| /Mul           | Mul_lable.pk      | Sequences randomly selected from APISeqDB  and the multi labels along with them.                                                                                                                                          |
| /LLM           | LLM_*             | the train data used to fine-tune LLMs,  200 of them are for training and 50 for testing.                                                                                                                                  |

There are `readme.md` files in each folder. These readme files will be useful for users to know the detail about the dataset and make use of them quickly. The `APISeqDB `folder include `APISeqDB.pk` and `APISeqDB_load.py`. The first one is the main dataset we release, and the second one is a python format script for readers to quickly start. The `MDT` folder contains the whole file used in malware detection experiment. Mul directory contains the whole file used in muti-label experiment. `LLM_train ` and `test.json` files are included in the `LLM ` directory. With these two files, we can fine-tunning LLM to qualify the Android malicious behavior description. The following table shows the paths and explanations of the files in our open source dataset directory.

| Directory Name | File Name          | Detailed Information                                                       |
| -------------- | ------------------ | -------------------------------------------------------------------------- |
| /main          | APISeqDB.pk        | Whole dataset, for more info, please read the readme file in the directory |
| /main          | readme.md          | detailed user guideline for the usage of APISeqDB                          |
| /main          | APISeqDB_load.py   | demo script for load APISeqDB                                              |
| /MDT           | MDT.pk             | 20,000 apps for the training set and 10,000 apps for the testing set       |
| /MDT           | MDT_load.py        | demo script for load MDT                                                   |
| /MDT           | readme.md          | detailed user guideline for the usage of MDT.pk file                       |
| /Mul           | Mul_lable.pk       | 4,000 sequences and the multi labels along with them                       |
| /Mul           | readme.md          | detailed user guideline for the usage of Mul_lable.pk                      |
| /LLM           | LLM_train.json     | the train data used to fine-tune llms                                      |
| /LLM           | LLM_test.json      | the test data used to fine-tune llms                                       |
| /LLM           | readme.md          | detailed user guideline for the usage of LLM_* files.                      |

### MDT

The dataset included in MDT directory is used to evaluate the performance of our dataset in classical machine learning android malware detection task. Each model is trained on two datasets, one fine-grained dataset $D_f$ and one coarse-grained dataset $D_c$, and evaluated on the same test set.

| Dataset | Training Set(APPs)        | Training Set(Behaviors)    | Testing Set(Apps)       |
| ------- | ------------------------- | -------------------------- | ----------------------- |
| $D_c$ | 10k Benign, 10k Malicious | 10k Benign, 10k Malicious  | 9k Benign, 1k Malicious |
| $D_f$ | 10k Benign, 10k Malicious | 111k Benign, 52k Malicious | 9k Benign, 1k Malicious |

### MUL

The dataset $D_{category}$ included in MUL are our  randomly selected 4,000 action sequences from APISeqDB. We  manually label them into six categories. There categories distribution can be seen in table.

| Dataset          | SMS | Phone | Info  | Rog | Re-In | Sys | Sum   |
| ---------------- | --- | ----- | ----- | --- | ----- | --- | ----- |
| $D_{category}$ | 733 | 809   | 1,146 | 818 | 386   | 108 | 4,000 |

### LLM

$D_{description}$ is the data used to fine-tunning LLMs,  200 of them are for training and 50 for testing.

| Dataset             | Training Set | Testing Set |
| ------------------- | ------------ | ----------- |
| $D_{description}$ | 200          | 50          |

## Attention

- We released our extracted features of an unbiased sample of the 200K apps studied in our paper. Because `APISeqDB.pk`file is larger than 100M, we storage the files in the OneDrive ([APISeqDB](https://1drv.ms/f/s!AmEGIYMGBaTpap6pzfPNLWbMaIE?e=s1dCSB)).

      

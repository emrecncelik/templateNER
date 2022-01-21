# Template-Based NER
Source Code For
 [Template-Based Named Entity Recognition Using BART](https://aclanthology.org/2021.findings-acl.161.pdf)

# Training

## 1 Convert your BIO file to Template format 
```python FromBIO2Template.py MyBIOFile.csv> MyTempFile.csv```


## 2 Training
Change the necessary part in  ```Template NER Training.ipynb```
and train your model

## 3 Inference
Change accordingly and run Inference ```InferenceCode.ipynb```
You need to convert your test data in BIO format into JSONL format. Use FromBIO2JSONL.py for it!


# Corpus

ATIS (https://github.com/yvchen/JointSLU/tree/master/data)

MIT Restaurant Corpus (https://groups.csail.mit.edu/sls/downloads/) 

MIT Movie Corpus (https://groups.csail.mit.edu/sls/downloads/)

# Contact

If you have any questions, please feel free to contact Leyang Cui
(<cuileyang@westlake.edu.cn>).

# Citation

```
@inproceedings{cui-etal-2021-template,
    title = "Template-Based Named Entity Recognition Using {BART}",
    author = "Cui, Leyang  and
      Wu, Yu  and
      Liu, Jian  and
      Yang, Sen  and
      Zhang, Yue",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.161",
    doi = "10.18653/v1/2021.findings-acl.161",
    pages = "1835--1845",
}
```

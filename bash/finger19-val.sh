#!/bin/bash

# FILES_PATH=/media/deakin/00000354000386C6/work/dataset/casia-maxpy-clean/casia-maxpy-clean/CASIA-maxpy-clean
#FILES_PATH=/home/deakin/ml/data/data-hand-script/A
# OUTPUT_LIST_TXT=casia-maxpy-clean-train.txt

#FILES_PATH=/media/deakin/00000354000386C6/work/dataset/finger-vein/finger-17-50-clean00/train
#OUTPUT_LIST_TXT=finger-17-50-clean00-train.txt

# FILES_PATH=/media/deakin/00000354000386C6/work/dataset/finger-vein/finger-17-50/val
# OUTPUT_LIST_TXT=finger-17-50-val.txt

# FILES_PATH=/home/deakin/Desktop/newf
# OUTPUT_LIST_TXT=finger-17-50-val-new.txt

#FILES_PATH=/home/deakin/Desktop/test00-01
#OUTPUT_LIST_TXT=finger-00-01.txt

#FILES_PATH=/media/deakin/00000354000386C6/work/dataset/finger-vein/test/finger-19-classes-train
#OUTPUT_LIST_TXT=finger-19-classes-train.txt

FILES_PATH=/media/deakin/00000354000386C6/work/dataset/finger-vein/test/finger-19-classes-val
OUTPUT_LIST_TXT=finger-19-classes-val.txt

python ../classification.py   --files_path=$FILES_PATH   --saved_txt_name=$OUTPUT_LIST_TXT  --random_mix=true


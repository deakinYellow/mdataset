#!/bin/bash

FILES_PATH=/home/deakin/ml/data/vein/sdu-classes-close
OUTPUT_PATH=/home/deakin/ml/data/vein/sdu-classes-close-split


python  ../dataset_split.py  --files_path=$FILES_PATH  --out_path=$OUTPUT_PATH  --val_proprotion=0.4  --random_mix=true
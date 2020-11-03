#!/bin/bash



FILES_PATH=""
OUTPUT_LIST_TXT=""

if [ "$1" == "train" ]
then
    echo "生成训练文件."
    FILES_PATH=/home/deakin/ml/data/vein/sdu-classes-close-split/train
    OUTPUT_LIST_TXT=finger-sdu400-classes-train.txt
else
    echo "生成验证文件."
    FILES_PATH=/home/deakin/ml/data/vein/sdu-classes-close-split/val
    OUTPUT_LIST_TXT=finger-sdu400-classes-val.txt
fi

python ../classification.py   --files_path=$FILES_PATH   --saved_txt_name=$OUTPUT_LIST_TXT  --random_mix=true


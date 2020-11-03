#-*-coding: utf-8-*-
import  os 
import  shutil 
import argparse
import parser
import random

from get_file_paths import *


"""
读取当前目录下的文件夹，将每个文件夹中的文件分别进行划分
其中%n存入 val/class 1-n%存入train/class 路径
"""

# import cv2
# import numpy as np  
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files_path", type=str, default="images/", help="path for  images files")
    parser.add_argument("--out_path", type=str, default="images-out/", help="path for out  images files")
    parser.add_argument("--val_proprotion", type=float, default=0.2, help="验证数据占比" )
    parser.add_argument("--random_mix", type=bool, default=False, help="random mix images paths")

    #存参数操作对象
    params_opt = parser.parse_args()  

    ##创建out目录以及 train, val 目录
    if( not os.path.exists( params_opt.out_path ) ):
        os.mkdir(params_opt.out_path)
    if( not os.path.exists( params_opt.out_path + "/train" ) ):
        os.mkdir(params_opt.out_path+"/train")
    if( not os.path.exists( params_opt.out_path + "/val" ) ):
        os.mkdir(params_opt.out_path+"/val")
    ##获取文件列表
    all_dirs, all_paths , cnt =  get_paths_list(  params_opt.files_path  )
    print( all_dirs )
    #classes_id = 0

    ##先创建对应类文件夹
    for _, class_dir in enumerate( all_dirs ): 
        train_full_class_dir  =  params_opt.out_path + "/train/" + class_dir  
        if( not os.path.exists(  train_full_class_dir  )  ): 
            os.mkdir( train_full_class_dir )
        val_full_class_dir  =  params_opt.out_path + "/val/" + class_dir  
        if( not os.path.exists(  val_full_class_dir  )  ): 
            os.mkdir( val_full_class_dir )

    ##遍历文件夹
    for classes_id , paths in enumerate(  all_paths ):

        #源路径
        src_path = params_opt.files_path + "/" 
        train_dst_path  =  params_opt.out_path + "/train/"
        val_dst_path  =  params_opt.out_path + "/val/"

        #选择是否需要随机排列
        if( params_opt.random_mix ):
            random.shuffle( paths )
        ##遍历拷贝当前文件夹下文件到新文件夹
        for i  in  range( len( paths ) ):
            print("path: ", paths[ i ]  )
            ##拷贝到训练集
            if(  i  <=  ( 1 - params_opt.val_proprotion  ) * len(paths)  ):
                shutil.copy( src_path+paths[i], train_dst_path+paths[ i]  )
            ##拷贝到验证集
            else:
                shutil.copy( src_path+paths[i], val_dst_path+paths[ i]  )

    print("划分完成，其中验证集占比: {} % ".format(  100 * params_opt.val_proprotion  ) )

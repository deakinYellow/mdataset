#-*-coding: utf-8-*-
"""
为目标分类数据集，生成文件列表txt文件
"""
import  sys
import  os 
import  shutil 
import argparse
import parser
import random

from get_file_paths import *



# import cv2
# import numpy as np  

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files_path", type=str, default="images/", help="path for  images files")
    parser.add_argument("--saved_txt_name", type=str, default="images_path.txt", help="name for images paths txt file")
    parser.add_argument("--random_mix", type=bool, default=False, help="name for random mix images paths txt file")

    #存参数操作对象
    params_opt = parser.parse_args()  

    #生成TXT文件
    saved_txt_name = params_opt.saved_txt_name
    print("saved txt_file_name: {}".format( saved_txt_name   ) )

    ##打开文件
    fp = open( saved_txt_name , 'w+' )
    origin_lines = []

    ##获取文件列表
    all_paths , cnt =  get_paths_list(  params_opt.files_path  )
    classes_id = 0
    ##遍历文件路径
    for classes_id , paths in enumerate(  all_paths ):
        for i,  path  in  enumerate( paths ):
            print("path: ", path )
            origin_lines.append( path + " " + str( classes_id ) + "\n"  )
            #fp.write( path + " " +  str( classes_id  ) )
    # 写入完成
    fp.writelines( origin_lines  )
    fp.close()
    print("一共 {} 类,共写入 共 {} 条数据, 保存在文件{}".format(  classes_id + 1,  cnt ,  saved_txt_name  ) )

    ##选择是否随机混合
    if( params_opt.random_mix ):
        random.shuffle( origin_lines )
        random_saved_txt_name =   saved_txt_name[:-4]  + "-random" + saved_txt_name[-4:]
        with open( random_saved_txt_name , "w")  as fp_random:
            fp_random.writelines( origin_lines )
            fp_random.close()
            print("一共 {} 类,共写入 共 {} 条数据, 保存在文件{}".format(  classes_id + 1,  cnt ,  random_saved_txt_name  ) )


#-*-coding: utf-8-*-
import  sys
import  os 
import  shutil 
import argparse
import parser

# import cv2
# import numpy as np  

# img_dir="/media/deakin/00000354000386C6/work/finger-vein/finger-17-50/train/00000"
print("python version: ", sys.version  )

# class GetFilePaths( ):
    # def __init__( self, root_path  ):

###获取目标路径下的所有文件夹,以及所有文件的相对路径
###返回格式如下 ["dir000", "dir001", ...] ,  [ ['dir000/000.jpg','dir000/001.jpg'],['dir001/000.jpg','dir001/001.jpg'],...] ,  总文件数目
def get_paths_list( root_path  ):
    all_dirs = []
    all_paths = []
    count = 0
    # print("paths:", paths )
    ###遍历数据文件夹
    for parent ,dirs, file_names in os.walk( root_path , followlinks=True ):
        end_dir = parent[ len( root_path ) + 1 : ]
        # print("end_dir: {}".format( end_dir  ) )  ##最底层目录
        end_dir_paths = []
        # #遍历底层目录
        for file_name in file_names:
            file_path = os.path.join( end_dir ,  file_name )
            end_dir_paths.append( file_path  )              
            count = count + 1
        ##排除空目录
        if ( len(end_dir_paths ) != 0 ):
            # #保存底层目录
            all_dirs.append( end_dir )
            #先进行排序
            end_dir_paths.sort()
            all_paths.append( end_dir_paths )
        # print("end_dir_paths: ", end_dir_paths )
    # print("all_paths len: ", len( all_paths ) )
    all_dirs.sort()
    return all_dirs, all_paths , count



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files_path", type=str, default="images/", help="path for  images files")
    # parser.add_argument("--cut_files_path", type=str, default="cut_images/", help="path for  images  after cut")
    params_opt = parser.parse_args()
    all_paths , cnt = get_paths_list( params_opt.files_path    )
    print("all_paths len: ", len( all_paths ) )
    for paths in all_paths:
        print("paths:",  paths  )
        # print("len paths: ", len(  paths  ) )
        for path in paths:
            pass
            # print("path: {:s} ".format(  path  ) )
    # print("一共读取到{}个文件路径".format( cnt  ) )


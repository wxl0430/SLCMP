from file.json import *
from file.zip import *
from tool.database import *
from tool.doing import *
from tool.id import *
import os
import shutil

class SLCMProjectFileError(Exception):
    pass

def makeslcmprojectfile(output_file : str = "") -> None:
    try:
        if output_file == "":
            output_file = os.getcwd()+"/SLCM_Project.slcm"
        tmp_path = os.path.dirname(output_file)+"/"+new_id("SLCM_tmp_",remember=0)
        filename = os.path.basename(output_file)
        output_path = os.path.dirname(output_file)
        data_path = tmp_path+"/data/"
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)
        os.mkdir(tmp_path)
        os.mkdir(tmp_path+"/data/")
        save_json(data_path+"maindata.json",data_to_json_dict(),1)
        save_json(data_path+"idlist.json",{"idlist":get_id_list()},1)
        save_json(data_path+"main.json",{
            "screenx":getscreenpos()[0],
            "screeny":getscreenpos()[1],
            "scaling":getscaling()
        },1)
        packzip(tmp_path,output_file)
        shutil.rmtree(tmp_path)
        setsaved(True)
    except:
        raise SLCMProjectFileError("生成项目文件时出错")

def openslcmprojectfile(input_file : str) -> None:
    try:
        tmp_path = os.path.dirname(input_file)+"/"+new_id("SLCM_tmp_",remember=0)
        unpackzip(input_file,tmp_path)
        data_path = tmp_path+"/data/"
        maindata = read_json(data_path+"maindata.json",1)
        data_from_json_dict(maindata)
        idlist = read_json(data_path+"idlist.json",1)["idlist"]
        set_id_list(idlist)
        main = read_json(data_path+"main.json",1)
        setscreenpos((main["screenx"],main["screeny"]))
        setscaling(main["scaling"])
        shutil.rmtree(tmp_path)
        setsaved(True)
    except:
        raise SLCMProjectFileError("打开项目文件时出错")

def newslcmprojectfile() -> None:
    setdataall({"node":[],"line":[]})
    set_id_list([])
    setscreenpos((int(getwidth()/2),int(getheight()/2)))
    setscaling(100)
    setsaved(True)
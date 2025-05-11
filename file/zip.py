import zipfile
import os

class ZipFileError(Exception):
    pass

def packzip(file_path : str, output_path : str) -> None:
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipObj:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, file_path)
                    zipObj.write(absolute_path, relative_path)
    except:
        raise ZipFileError("打包zip文件时出错")

def unpackzip(zip_file : str, output_path : str) -> None:
    try:
        with zipfile.ZipFile(zip_file, 'r') as zipObj:
            output_path = output_path or os.path.dirname(zip_file)
            zipObj.extractall(output_path)
    except:
        raise ZipFileError("解压zip文件时出错")

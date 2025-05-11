import json
import os

class JsonFileError(Exception):
    pass

cwd = os.getcwd()+"/"

def read_json(file_path: str, hascwd: bool = False, encoding: str = 'utf-8') -> dict:
    if not hascwd:
        file_path = cwd + file_path
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise JsonFileError("JSON 解码失败") from e

def save_json(file_path: str, data: dict, hascwd: bool = False, encoding: str = 'utf-8') -> None:
    if not hascwd:
        file_path = cwd + file_path
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError as e:
        raise JsonFileError("JSON 编码失败") from e
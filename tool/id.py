import random

idlist = []

def new_id(strat_str: str = "", end_str: str = "", len: int = 16, chars: str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",remember : bool = True) -> str:
    now_id = strat_str + ''.join(random.choice(chars) for _ in range(len)) + end_str
    while now_id in idlist:
        now_id = strat_str + ''.join(random.choice(chars) for _ in range(len)) + end_str
    if remember:
        idlist.append(now_id)
    return now_id

def del_id(id_str: str) -> bool:
    if id_str in idlist:
        idlist.remove(id_str)
        return True
    else:    
        return False
    
def get_id_list() -> list:
    return idlist

def set_id_list(id_list: list) -> None:
    global idlist
    idlist = id_list

def check_id(id_str: str) -> bool:
    return id_str in idlist
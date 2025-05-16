class StringConverterError(Exception):
    pass

def stringsetlength(string : str, length : int, fillchar : str = " ", align : str = "left", delmore : bool = False, replacemore : bool = False, replacechar : str = "..."):
    """
    string : 要转换的字符串
    length : 目标长度
    fillchar : 填充字符，默认为空格
    align : 方向，可选：left、right，默认left
        left : 表示当不够长时，左边补fillchar，超出长度时，右边截取并添加replacechar
        right : 表示当不够长时，右边补fillchar，超出长度时，左边截取并添加replacechar
    delmore : 当字符串长度超过目标长度时，是否删除多余字符，默认False
    replacemore : 当字符串长度超过目标长度时，是否替换多余字符，默认False
    replacechar : 替换字符，默认省略号"..."
    """
    if len(string) > length:
        if delmore:
            string = string[:length]
            return string
        elif replacemore:
            try:
                string = string[:length-len(replacechar)]
            except:
                raise StringConverterError("替换字符过长，不得大于length")
            if align == "left":
                return string + replacechar
            elif align == "right":
                return replacechar + string
            else:
                raise StringConverterError("方向参数错误，可选：left、right")
        else:
            return string
    else:
        if align == "left":
            return fillchar * (length - len(string)) + string
        if align == "right":
            return string + fillchar * (length - len(string))


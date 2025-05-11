import tkinter
import tkinter.filedialog
import tkinter.messagebox

def init_filewindow():
    global root
    root = tkinter.Tk()
    root.withdraw()

def fileopenwindow(title : str = "打开项目文件", filetypes : list = [('All files', '*')], defaultextension= "", initialdir : str = '/'):
    r = tkinter.filedialog.askopenfilename(title=title,filetypes=filetypes,initialdir=initialdir,defaultextension=defaultextension)
    return r

def filesavewindow(title : str = "保存项目文件", filetypes : list = [('All files', '*')], defaultextension= "", initialdir : str = '/'):
    r = tkinter.filedialog.asksaveasfilename(title=title,filetypes=filetypes,initialdir=initialdir,defaultextension=defaultextension)
    return r

def messagebox(message :  str, title : str = "信息") -> str: 
	return tkinter.messagebox.showinfo(title=title,message=message)

def warningbox(message :  str, title : str = "警告") -> str: 
    return tkinter.messagebox.showwarning(title=title,message=message)

def errorbox(message :  str, title : str = "错误") -> str: 
    return tkinter.messagebox.showerror(title=title,message=message)
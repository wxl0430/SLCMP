import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.colorchooser
import tkinter.ttk

def init_tkwindow():
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

def questionbox(message :  str, title : str = "询问") -> str: 
    return tkinter.messagebox.askyesnocancel(title=title,message=message)

def getsettingwindow(title: str = "修改配置", normalx: int = 0, normaly: int = 0, normalcolor: str = "#000000", displaycolor: bool = False):
    print(normalx, normaly, normalcolor)
    if displaycolor:
        result = (normalx, normaly, normalcolor)
    else:
        result = (normalx, normaly)

    def confirm(event=None):
        nonlocal result
        x_value = entry_x.get()
        y_value = entry_y.get()
        if x_value == "-":
            x_value = "-0"
        if y_value == "-":
            y_value = "-0"
        if x_value == "":
            x_value = "0"
        if y_value == "":
            y_value = "0"
        
        if displaycolor:
            result = (x_value, y_value, color_var.get())
        else:
            result = (x_value, y_value)
        root.quit()

    def cancel(event=None):
        nonlocal result
        if displaycolor:
            result = (normalx, normaly, normalcolor)
        else:
            result = (normalx, normaly)
        root.quit()

    def on_closing():
        nonlocal result
        if displaycolor:
            result = (normalx, normaly, normalcolor)
        else:
            result = (normalx, normaly)
        root.quit()

    def select_color(event=None):
        color_code = tkinter.colorchooser.askcolor(title="选择颜色", initialcolor=color_var.get())
        if color_code[1]:
            color_var.set(color_code[1])
            color_label.config(bg=color_code[1])

    def validate_input(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if action == '0':
            return True
        if action == '1':
            if index == '0' and text == '-' and (value_if_allowed in ('', '-')):
                return True
            elif prior_value.startswith('-') and text.isdigit():
                return True
            elif text.isdigit():
                return True
            elif (text != "" and text[0] == "-" and text[1:].isdigit()):
                return True
            elif (text == "-" and index == "0" and (not "-" in prior_value)):
                return True
        return False

    root = tkinter.Tk()
    root.title(title)
    root.geometry("300x400")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.bind("<Return>", confirm)
    root.bind("<Escape>", cancel)

    validate_cmd = (root.register(validate_input), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

    frame = tkinter.Frame(root)
    frame.pack(pady=20)

    label_x = tkinter.ttk.Label(frame, text="x:", font=('Consolas', 15))
    label_x.grid(row=0, column=0, sticky='w', padx=(20, 0))
    entry_x = tkinter.ttk.Entry(frame, validate='key', validatecommand=validate_cmd, font=('Consolas', 15), width=10)
    entry_x.grid(row=0, column=1, sticky='w', padx=(10, 0))
    entry_x.insert(0, str(normalx))

    label_y = tkinter.ttk.Label(frame, text="y:", font=('Consolas', 15))
    label_y.grid(row=1, column=0, sticky='w', padx=(20, 0))
    entry_y = tkinter.ttk.Entry(frame, validate='key', validatecommand=validate_cmd, font=('Consolas', 15), width=10)
    entry_y.grid(row=1, column=1, sticky='w', padx=(10, 0))
    entry_y.insert(0, str(normaly))

    if displaycolor:
        color_label_text = tkinter.ttk.Label(frame, text="颜色：", font=('Consolas', 15))
        color_label_text.grid(row=2, column=0, sticky='w', padx=(20, 0))
        color_var = tkinter.StringVar(value=normalcolor)
        color_label = tkinter.Label(frame, text="", width=10, height=2, background=normalcolor, relief='solid', font=('Consolas', 15))
        color_label.grid(row=2, column=1, sticky='w', padx=(10, 0))
        color_label.bind("<Button-1>", select_color)

    style = tkinter.ttk.Style()
    style.configure('Big.TButton', font=('Consolas', 25), width=20, height=5)

    button_confirm = tkinter.ttk.Button(root, text="确认", command=confirm, style='Big.TButton')
    button_confirm.pack(pady=20)

    frame.grid_rowconfigure(0, pad=20)
    frame.grid_rowconfigure(1, pad=20)
    if displaycolor:
        frame.grid_rowconfigure(2, pad=20)

    root.mainloop()
    root.destroy()

    return result

import tkinter as tk
def haha():
    window = tk.Tk()
    window.geometry('500x100')

    name_input = tk.Text(window,width='40',height='3')		# width宽 height高
    name_input.pack()

    glo = '30'
    def print_name():
        global glo
        glo = name_input.get('1.0', '20.129312')
        # 可以用get()方法获取Text的文本内容
        window.destroy()
                                                                                                    # 其中第一个参数是起始位置，'1.1'就是从第一行第一列后，到第一行第五列后
    tk.Button(window,text='输出名字',command=print_name).pack()
    window.mainloop()
    print(glo)

haha()

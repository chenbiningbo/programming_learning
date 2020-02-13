import tkinter

window = tkinter.Tk()
window.title("计算器")

# 记录模式
expstr = ""

# 记录运算历史
history_label_obj_list = []

def onClick(key):
    """
    按钮点击事件
    """
    global expstr

    if key == "=":
        jieguo = round(eval(expstr), 2)
        result["text"] = jieguo

        frame_right.pack()

        t = tkinter.Label(frame_inner, text=expstr + "=" + str(jieguo),
                          background="seashell")
        t.pack()

        history_label_obj_list.append(t)

    elif key == "AC":
        result["text"] = ""
        expstr = ""
    else:
        expstr = expstr +str(key)
        result["text"] = expstr

frame_grap = tkinter.Frame(window)
frame_grap.pack(fill="y", side="left")

frame_left = tkinter.Frame(window)

result = tkinter.Label(frame_left, bg="seashell", text="0", height=2, font=("Arial", 34, "bold")) #定义标签
result.grid(row=0, column=0, columnspan=4, sticky=tkinter.E)

ac = tkinter.Button(frame_left, text="AC", width=12, height=2, command=lambda: onClick("AC"))
ac.grid(row=1, column=0)

negative = tkinter.Button(frame_left, text="+/-", width=12, height=2, command=lambda: onClick("-"))
negative.grid(row=1, column=1)

percent = tkinter.Button(frame_left, text="%", width=12, height=2, command=lambda: onClick("/100"))
percent.grid(row=1, column=2)

division = tkinter.Button(frame_left, text="/", width=12, height=2, command=lambda: onClick("/"))
division.grid(row=1, column=3)

num_seven = tkinter.Button(frame_left, text="7", width=12, height=4, command=lambda: onClick("7"))
num_seven.grid(row=2, column=0)

num_eight = tkinter.Button(frame_left, text="8", width=12, height=4, command=lambda: onClick("8"))
num_eight.grid(row=2, column=1)

num_nine = tkinter.Button(frame_left, text="9", width=12, height=4, command=lambda: onClick("9"))
num_nine.grid(row=2, column=2)

asterrisk = tkinter.Button(frame_left, text="*", width=12, height=4, command=lambda: onClick("*"))
asterrisk.grid(row=2, column=3)

num_four = tkinter.Button(frame_left, text="4", width=12, height=4, command=lambda: onClick("4"))
num_four.grid(row=3, column=0)

num_five = tkinter.Button(frame_left, text="5", width=12, height=4, command=lambda: onClick("5"))
num_five.grid(row=3, column=1)

num_six = tkinter.Button(frame_left, text="6", width=12, height=4, command=lambda: onClick("6"))
num_six.grid(row=3, column=2)

subtraction = tkinter.Button(frame_left, text="-", width=12, height=4, command=lambda: onClick("-"))
subtraction.grid(row=3, column=3)

num_one = tkinter.Button(frame_left, text="1", width=12, height=4, command=lambda: onClick("1"))
num_one.grid(row=4, column=0)

num_two = tkinter.Button(frame_left, text="2", width=12, height=4, command=lambda: onClick("2"))
num_two.grid(row=4, column=1)

num_three = tkinter.Button(frame_left, text="3", width=12, height=4, command=lambda: onClick("3"))
num_three.grid(row=4, column=2)

plus = tkinter.Button(frame_left, text="+", width=12, height=4, command=lambda: onClick("+"))
plus.grid(row=4, column=3)

num_zero = tkinter.Button(frame_left, text="0", width=26, height=4, command=lambda: onClick("0"))
num_zero.grid(row=5, column=0, columnspan=2)

point = tkinter.Button(frame_left, text=".", width=12, height=4, command=lambda: onClick("."))
point.grid(row=5, column=2)

equals = tkinter.Button(frame_left, text="=", width=12, height=4, command=lambda: onClick("="))
equals.grid(row=5, column=3)

frame_left.pack(fill="y", side="left")

frame_right = tkinter.Frame(window, width=400)
tkinter.Label(frame_right, text="运算历史", font=("Arial", 14, "underline bold")).pack()

frame_inner = tkinter.Frame(frame_right)
frame_inner.pack(fill="x", side="top")

def clean_history():
    """
    清除运算历史
    """
    for x in history_label_obj_list:
        print(x)
        x.destroy()


clean_button = tkinter.Button(frame_right, text="清空", command=lambda:clean_history())
clean_button.pack(fill="x", side="top")

window.mainloop()


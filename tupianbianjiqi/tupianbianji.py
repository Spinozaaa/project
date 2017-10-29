import tkinter as tk
from tkinter import *
'''
from tkinter import ttk  
from tkinter import scrolledtext  
from tkinter import Menu  
from tkinter import Spinbox  
from tkinter import messagebox as mBox
'''
from PIL import Image


def star():
	win = tk.Tk()     

	# Add a title         
	win.title("photo")  
	win.geometry("400x150")

	wel = Label(win,text="Welcome",bg="pink",font=("yellow",35))
#star = Label(win,text="\n 请输入图片所在路径及名称")
	wel.pack()
#star.pack()
	var = StringVar()
	e = Entry(win,textvariable=var,width=30)
	var.set("请在此处输入图片所在路径及名称")
	e.pack()

	def insert_end():
		global img
		img = Image.open(var.get())
		win.quit()
	

	b1=tk.Button(win,text="确定",width=15,height=2,font=(12),command=insert_end)
	b1.pack()
	#t.pack()
	win.mainloop()
	return img

im=star()
im.show()

def fuc():
	global im
	root = tk.Tk()
	root.title("photo")
	root.geometry("500x350")

	inf = Label(root,text="图像信息:",bg="pink")
	inf.pack()

	t=tk.Text(root,height=3)
	t.insert('1.0',"格式：")
	t.insert('end',im.format)
	t.insert('end',"\n大小：")
	t.insert('end',  im.size)
	t.insert('end',"\n模式：")
	t.insert('end',  im.mode)
	t.pack()

	f = Label(root,text="选择功能:",bg="pink",font=(35))
	f.pack()

	def jq():
		box=(100,100,300,300)

	cjtx=tk.Button(root,text="裁剪图像",width=15,height=2,font=(12),command=jq)
	jhbh=tk.Button(root,text="几何变换",width=15,height=2,font=(12),command=jq)
	yxms=tk.Button(root,text="颜色模式",width=15,height=2,font=(12),command=jq)
	txzq=tk.Button(root,text="图像增强",width=15,height=2,font=(12),command=jq)

	cjtx.pack()
	jhbh.pack()
	yxms.pack()
	txzq.pack()


	root.mainloop()
#infile, im.format, "%dx%d" % im.size, im.mode
fuc()


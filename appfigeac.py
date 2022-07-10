import tkinter as tk
from PIL import Image,ImageTk
from test import *
from tkinter.filedialog import askopenfile
from openpyxl import load_workbook
import time
from tkinter.ttk import *


root=tk.Tk()
canvas = tk.Canvas(root,width=600, height=300)
canvas.grid(columnspan=3 ,rowspan=3)
gpath=''
tb=tk.Entry(root, width=50)
#create the import dataset button
def open_file():
    global gpath
    file = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx *.xlsm *.sxc *.ods *.csv *.tsv')]) # To open the file that you want. 
    #' mode='r' ' is to tell the filedialog to read the file
    # 'filetypes=[()]' is to filter the files shown as only Excel files

    wb = load_workbook(filename = file.name) # Load into openpyxl
    wb2 = wb.active
    tb.insert(0,file.name)
    gpath=file.name
    if file is not None:
        pass
    #Whatever you want to do with the WorkSheet
    
    #wb2.sheetname

def uploadFiles():
    pb1 = Progressbar(
        root, 
        orient= 'horizontal', 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
#browse button
browse_text=tk.StringVar()

browse_btn=tk.Button(root,textvariable=browse_text,command=open_file,font="Raleway",bg="#20bebe",fg="white",height=2,width=15)
browse_text.set("import dataset")
browse_btn.grid(column=1,row=2)

label= tk.Label(root)
label.grid(column=1,row=4)

canvas = tk.Canvas(root,width=600, height=250)
canvas.grid(columnspan=3 )

#####################
adhar = Label(
    root, 
    text='Upload Government id in jpg format '
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    root, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)

upld = Button(
    root, 
    text='Upload File', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



root.mainloop()

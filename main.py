from tkinter import *
from tkinter import filedialog, font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
app_title = "Complete code"
app = Tk()
app.title(app_title)
app.geometry("700x650")
app.iconbitmap("logo.ico")
app.minsize(600, 600)
global open_status_name
open_status_name = False
global selected_text
selected_text = False
# The full dynamic width and height
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
# The main frame
main_frame = Frame(app)
main_frame.pack()
# Functions
def new_file():
    code_block.delete("1.0", END)
    app.title(f"{app_title}")
    global open_status_name
    open_status_name = False

def open_file():
    code_block.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="Downloads", title="Open file", filetype=(("Text file", "*.txt"), ("All files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    name.replace("Downloads", "")
    app.title(f"{app_title} - {name}")
    text_file = open(text_file, "r")
    stuff = text_file.read()
    code_block.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="Downloads", title="Save as", filetype=(("Text file", "*.txt"), ("All files", "*.*")))
    if text_file:
        name = text_file
        name = name.replace("Downloads", "")
        app.title(f"{app_title} - {name}")
        text_file = open(text_file, "w")
        text_file.write(code_block.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(code_block.get(1.0, END))
        text_file.close()
    else:
        save_as_file()

def cut_text(e):
    global selected_text
    if e:
        selected_text = app.clipboard_get()
    else:
        if code_block.selection_get():
            selected_text = code_block.selection_get()
            code_block.delete("sel.first", "sel.last")
            app.clipboard_clear()
            app.clipboard_append(selected_text)

def copy_text(e):
    global selected_text
    if e:
        selected_text = app.clipboard_get()
    if code_block.selection_get():
        selected_text = code_block.selection_get()
        app.clipboard_clear()
        app.clipboard_append(selected_text)

def paste_text(e):
    global selected_text
    if e:
        selected_text = app.clipboard_get()
    else:
        if selected_text:
            position = code_block.index(INSERT)
            code_block.insert(position, selected_text)

def light_mode():
    main_color = "#ffffff"
    first_color = "#f0f0f0"
    text_color = "#050505"
    app.config(bg=main_color)
    code_block.config(bg=first_color, fg=text_color, selectbackground="#c90a0a", selectforeground="white")
    file_menu.config(bg=first_color, fg=text_color)
    edit_menu.config(bg=first_color, fg=text_color)
    theme_menu.config(bg=first_color, fg=text_color)

def dark_mode():
    main_color = "#000000"
    first_color = "#141414"
    text_color = "#f5f5f5"
    app.config(bg=main_color)
    code_block.config(bg=first_color, fg=text_color, selectbackground=text_color, selectforeground=main_color)
    file_menu.config(bg=first_color, fg=text_color)
    edit_menu.config(bg=first_color, fg=text_color)
    theme_menu.config(bg=first_color, fg=text_color)

def default_mode():
    main_color = "SystemButtonFace"
    first_color = "SystemButtonFace"
    text_color = "Black"
    app.config(bg=main_color)
    code_block.config(bg=first_color, fg=text_color, selectbackground="#c90a0a", selectforeground="white")
    file_menu.config(bg=first_color, fg=text_color)
    edit_menu.config(bg=first_color, fg=text_color)
    theme_menu.config(bg=first_color, fg=text_color)

def select_all(e):
    code_block.tag_add("sel", "1.0", "end")

def clear_all():
    code_block.delete(1.0, END)
# This is were the things get defined
code_block_scroll = Scrollbar(app)
code_block_scroll.pack(side=RIGHT, fill=Y)
code_block_scrollhor = Scrollbar(app, orient="horizontal")
code_block_scrollhor.pack(side=BOTTOM, fill=X)
code_block = Text(app, height=app_height, width=app_width, font=("Courier", 11), selectbackground="#c90a0a", selectforeground="white", undo=True, yscrollcommand=code_block_scroll.set, wrap="none", xscrollcommand=code_block_scrollhor.set)
# Menus
menu_bar = Menu(app)
app.config(menu=menu_bar)
# Add stuffs in menu
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New file", command=new_file, accelerator="(CTRL + N)")
file_menu.add_command(label="Open File", command=open_file, accelerator="(CTRL + O)")
file_menu.add_command(label="Save as", command=save_as_file, accelerator="(CTRL + SHIFT + S)")
file_menu.add_command(label="Save", command=save_file, accelerator="(CTRL + S)")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(CTRL + X)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(CTRL + C)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(CTRL + V)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=code_block.edit_undo, accelerator="(CTRL + Z)")
edit_menu.add_command(label="Redo", command=code_block.edit_redo, accelerator="(CTRL + Y)")
theme_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Default mode", command=default_mode)
theme_menu.add_command(label="Dark mode", command=dark_mode, accelerator="(RECOMMENDED)")
theme_menu.add_command(label="Light mode", command=light_mode)
dev_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Dev tools", menu=dev_menu)
dev_menu.add_command(label="Clear all", command=clear_all)
dev_menu.add_command(label="Select all", command=lambda: select_all(True))
# This is were the things gets placed
code_block.pack()
#Config
code_block_scroll.config(command=code_block.yview)
code_block_scrollhor.config(command=code_block.xview)
#Bindings
app.bind("<Control-x>", cut_text)
app.bind("<Control-c>", copy_text)
app.bind("<Control-v>", paste_text)
app.bind("<Control-A>", select_all)
app.bind("<Control-a>", select_all)
app.mainloop()
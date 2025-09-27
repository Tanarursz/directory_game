import tkinter as tk
import os

# List of directories you want to include
DIRECTORIES = [
    r"src\dev\modules\map\fasz",
    r"src\dev\modules\map\kope"
]

current_file = None

def load_files():
    """Fill the listbox with files from all DIRECTORIES"""
    listbox.delete(0, tk.END)
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            continue
        for file in os.listdir(directory):
            if file.endswith(".map"):
                # show "dirname/filename" in listbox
                listbox.insert(tk.END, f"{os.path.basename(directory)}/{file}")

def open_selected_file(event=None):
    """Open the selected file from the listbox"""
    global current_file
    selection = listbox.curselection()
    if not selection:
        return

    entry = listbox.get(selection[0])
    dirname, filename = entry.split("/", 1)

    # find the full directory path
    directory = [d for d in DIRECTORIES if os.path.basename(d) == dirname][0]
    filepath = os.path.join(directory, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text.delete("1.0", tk.END)
        text.insert(tk.END, f.read())

    root.title(f"MapMaker - {filepath}")
    status_label.config(text=f"Megnyitva: {filepath}")
    current_file = filepath

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
        status_label.config(text=f"Mentve: {current_file}")
    else:
        status_label.config(text="Nincs fájl kiválasztva!")

# --- UI setup ---
root = tk.Tk()
root.title("MapMaker")
root.geometry("800x400")

# Left side: listbox with files
frame_left = tk.Frame(root)
frame_left.pack(side="left", fill="y")

listbox = tk.Listbox(frame_left, width=40)
listbox.pack(fill="y", expand=True)
listbox.bind("<<ListboxSelect>>", open_selected_file)

# Right side: text editor
text = tk.Text(root, wrap="word", font=("Consolas", 12))
text.pack(side="right", expand=1, fill="both")

# Status bar
status_label = tk.Label(root, text="Készen áll", anchor="w")
status_label.pack(side="bottom", fill="x")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fájl", menu=file_menu)
file_menu.add_command(label="Mentés", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Kilépés", command=root.quit)

# Load file list at startup
load_files()

root.mainloop()

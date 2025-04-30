import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder)

def select_target_folder():
    folder = filedialog.askdirectory()
    if folder:
        target_entry.delete(0, tk.END)
        target_entry.insert(0, folder)

def filter_and_copy_files():
    source_dir = source_entry.get()
    target_dir = target_entry.get()
    suffixes_input = suffixes_entry.get()

    if not os.path.exists(source_dir):
        messagebox.showerror("错误", "源文件夹路径不存在")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    suffix_list = [s.strip() for s in suffixes_input.split(",") if s.strip()]
    if not suffix_list:
        messagebox.showerror("错误", "请至少输入一个有效后缀")
        return

    copied_count = 0
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            if any(filename.endswith(suffix) for suffix in suffix_list):
                shutil.copy2(source_path, os.path.join(target_dir, filename))
                copied_count += 1

    messagebox.showinfo("完成", f"已复制 {copied_count} 个文件。")

# 创建主窗口
root = tk.Tk()
root.title("phm文件筛选复制工具")
root.geometry("600x250")

# 源文件夹
tk.Label(root, text="源文件夹:").pack(anchor="w", padx=10, pady=(10, 0))
source_frame = tk.Frame(root)
source_frame.pack(fill="x", padx=10)
source_entry = tk.Entry(source_frame)
source_entry.pack(side="left", fill="x", expand=True)
tk.Button(source_frame, text="浏览", command=select_source_folder).pack(side="left", padx=5)

# 目标文件夹
tk.Label(root, text="目标文件夹:").pack(anchor="w", padx=10, pady=(10, 0))
target_frame = tk.Frame(root)
target_frame.pack(fill="x", padx=10)
target_entry = tk.Entry(target_frame)
target_entry.pack(side="left", fill="x", expand=True)
tk.Button(target_frame, text="浏览", command=select_target_folder).pack(side="left", padx=5)

# 后缀输入
tk.Label(root, text="输入后缀（用英文逗号分隔，例如 .AD07.lz4,.AD08.lz4）:").pack(anchor="w", padx=10, pady=(10, 0))
suffixes_entry = tk.Entry(root)
suffixes_entry.pack(fill="x", padx=10)

# 执行按钮
tk.Button(root, text="开始筛选并复制", command=filter_and_copy_files, bg="lightblue").pack(pady=20)

root.mainloop()

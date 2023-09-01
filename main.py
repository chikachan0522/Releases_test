import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry("300x200")

tk.Label(root, text="Hello World").pack()

if __name__ == "__main__":
    root.mainloop()
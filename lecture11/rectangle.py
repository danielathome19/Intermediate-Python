import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Area and Perimeter Calculator")
        root.geometry("300x325")

        self.lbl_len = tk.Label(root, text="Length:")
        self.lbl_len.place(x=0, y=30, width=90, height=26)

        self.txt_len = tk.Entry(root)
        self.txt_len.place(x=120, y=30, width=150, height=28)

        self.lbl_wid = tk.Label(root, text="Width:")
        self.lbl_wid.place(x=0, y=90, width=90, height=26)

        self.txt_wid = tk.Entry(root)
        self.txt_wid.place(x=120, y=88, width=150, height=28)

        self.btn_calc = tk.Button(root, text="Calculate", command=self.on_btn_calc)
        self.btn_calc.place(x=10, y=150, width=280, height=30)

        self.label3 = tk.Label(root, text="Area:")
        self.label3.place(x=0, y=210, width=90, height=26)

        self.lbl_area = tk.Label(root, text="", bg="#ffffff")
        self.lbl_area.place(x=120, y=208, width=150, height=30)

        self.label5 = tk.Label(root, text="Perimeter:")
        self.label5.place(x=0, y=270, width=90, height=26)

        self.lbl_perim = tk.Label(root, text="", bg="#ffffff")
        self.lbl_perim.place(x=120, y=268, width=150, height=30)

    def on_btn_calc(self):
        length = int(self.txt_len.get())
        width = int(self.txt_wid.get())

        area = length * width
        perim = 2 * length + 2 * width

        self.lbl_area.config(text=str(area))
        self.lbl_perim.config(text=str(perim))
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

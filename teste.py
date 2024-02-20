import tkinter as tk
from tkinter import *
from tkcalendar import Calendar

fundo = "#131A21"
fonte1 = ("Arial", 20, "bold")
fonte2 = ("Arial Greek", 20, "italic")

def main():
    def destruir_mosts():
        lb_most.destroy()
        lb_most2.destroy()
        lb_most3.destroy()
        lb_most4.destroy()

    def click():
        destruir_mosts()

        lb_time1 = tk.Button(janela, text="Button 1", font=fonte1, command=click, bg="#1C2632", width=6, height=2)
        lb_time1.place(x=400, y=130)

        lb_time2 = tk.Button(janela, text="Button 2", font=fonte1, command=click, bg="#1C2632", width=6, height=2)
        lb_time2.place(x=550, y=130)

        
        
        frame_tabela1 = tk.Frame(janela, bg="#1C2632")
        frame_tabela1.place(x=350, y=300, width=400, height=200)

        class TabelaLabel1(tk.Label):
            def __init__(self, master, rows, columns, data, **kwargs):
                super().__init__(master, **kwargs)
                self.rows = rows
                self.columns = columns
                self.data = data
                self.create_table()

            def create_table(self):
                for i in range(self.rows):
                    for j in range(self.columns):
                        cell_value = str(self.data[i][j]) if i < len(self.data) else ""
                        fg_color = "#328F71" if j == 0 or j == 3 else "#7A84FF"
                        cell_label = tk.Label(self, text=cell_value, relief="solid", borderwidth=1, width=10, height=2, fg=fg_color, bg="#1C2632")
                        cell_label.grid(row=i, column=j, sticky="nsew")

                for i in range(self.rows):
                    self.grid_rowconfigure(i, weight=1)

                for j in range(self.columns):
                    self.grid_columnconfigure(j, weight=1)

        data1 = [
            ["G", 2, 1, "G"],
            ["D", 1, 2, "D"],
            ["C", 0, 1, "C"],
            ["F", 0, 3, "F"],
            ["L", 1, 0, "L"],
            ["E", 2, 2, "E"],
        ]

        tabela_label1 = TabelaLabel1(frame_tabela1, rows=len(data1), columns=len(data1[0]), data=data1, bg="#1C2632", fg="white")
        tabela_label1.pack(expand=True, fill="both")

        frame_tabela2 = tk.Frame(janela, bg="#1C2632")
        frame_tabela2.place(x=800, y=150, width=150, height=300)

        class TabelaLabel2(tk.Label):
            def __init__(self, master, rows, columns, data, **kwargs):
                super().__init__(master, **kwargs)
                self.rows = rows
                self.columns = columns
                self.data = data
                self.create_table()

            def create_table(self):
                for i in range(self.rows):
                    for j in range(self.columns):
                        cell_value = str(self.data[i][j]) if i < len(self.data) else ""
                        fg_color = "#328F71" if j == 0 or j == 3 else "#7A84FF"
                        cell_label = tk.Label(self, text=cell_value, relief="solid", borderwidth=1, width=10, height=2, fg=fg_color, bg="#1C2632")
                        cell_label.grid(row=i, column=j, sticky="nsew")

                for i in range(self.rows):
                    self.grid_rowconfigure(i, weight=1)

                for j in range(self.columns):
                    self.grid_columnconfigure(j, weight=1)

        data2 = [
            ["passes", 0],
            ["Finalizações", 0],
            ["Posse de bola", 0],
            ["Laterais", 0],
            ["Tiro de Meta", 0],
            ["Passes errados", 0],
        ]

        tabela_label2 = TabelaLabel2(frame_tabela2, rows=len(data2), columns=len(data2[0]), data=data2, bg="#1C2632", fg="white")
        tabela_label2.pack(expand=True, fill="both")

    def get_selected_date():
        date_label.config(text="Selected Date is: " + cal.get_date())

    def grad_date():
        date_label.config(text="Selected Date is: " + cal.get_date())

    janela = tk.Tk()
    janela.geometry("1018x558")
    janela.configure(bg=fundo)
    janela.resizable(width=False, height=False)

    lb_barra = tk.Button(janela, text="LionsBet", font=fonte1, command=main,fg="#328F71", bg="#2A3543", bd=1, justify=RIGHT,
                        width=60, height=2)
    lb_barra.place(x=1, y=1)
    lb_barra2 = tk.Label(janela, font=fonte1, bg="#4A535F", width=60, height=1)
    lb_barra2.place(x=1, y=60)

    lb_most = tk.Button(janela, text="Button 1", font=fonte1, command=click, bg="#1C2632", width=16, height=2)
    lb_most.place(x=300, y=130)

    lb_most2 = tk.Button(janela, text="Button 2", font=fonte1, command=click, bg="#1C2632", width=16, height=2)
    lb_most2.place(x=620, y=130)

    lb_most3 = tk.Button(janela, text="Button 3", font=fonte1, command=click, bg="#1C2632", width=16, height=2)
    lb_most3.place(x=300, y=230)

    lb_most4 = tk.Button(janela, text="Button 4", font=fonte1, command=click, bg="#1C2632", width=16, height=2)
    lb_most4.place(x=620, y=230)

    cal = Calendar(janela, background="#1C2632", disabledbackground="#1C2632", borderbackground="#1C2632",
                   headersbackground="#1C2632", normalbackground="#1C2632")
    cal.config(background="#1C2632")
    cal.place(x=10, y=130)

    janela.mainloop()

main()
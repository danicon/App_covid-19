from tkinter import *
from tkinter import ttk

###############  Cores Usadas ###############
co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

# criar janela
janela = Tk()

janela.resizable(width=FALSE, height=FALSE)
janela.geometry('835x360')
janela.title('')
janela.configure(bg=co6)

#  criando frames
app_nome_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

mostrar_frame_mortes = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

selecione_frame = Frame(janela, width=840, height=50, bg=co6, relief="flat")
selecione_frame.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)


# criando labels para app_nome_frame
app_nome = Label(app_nome_frame, text="COVID-19", width=20, height=1,
             pady=20, relief="flat", anchor=CENTER, font=("Helvetica 25 bold"), bg=co2, fg=co0)
app_nome.grid(row=0, column=0, pady=5)


# criando labels para mostrar_frame_infectados
label_infetados = Label(mostrar_frame_infectados, text="infectados", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_infetados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infetados = Label(mostrar_frame_infectados, text="42222", width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_infetados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Quarta-feira 22 /06/2020", width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Total casos ativos de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_azul = Label(mostrar_frame_infectados, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co3, fg=co0)
mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando labels para mostrar_frame_recuperados
label_recuperados = Label(mostrar_frame_recuperados, text="recuperados", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_recuperados = Label(mostrar_frame_recuperados, text="42222", width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_recuperados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text="Quarta-feira 22 /06/2020", width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text="Total casos recuperados de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_verde = Label(mostrar_frame_recuperados, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co5, fg=co0)
mostrar_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando labels para mostrar_frame_mortes
label_mortes = Label(mostrar_frame_mortes, text="mortes", width=20, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(mostrar_frame_mortes, text="42222", width=12, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Quarta-feira 22 /06/2020", width=25, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Total casos mortes de covid-19", width=33, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_vermelho = Label(mostrar_frame_mortes, text="", width=19, height=1,
             pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co1, fg=co0)
mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


# criando  caixa de seleção
label_pais = Label(selecione_frame, text="Selecione o pais", width=13, height=1,
             pady=7, padx=0, relief="flat", anchor=NW, font=("Ivy 12 bold"), bg=co6, fg=co0)
label_pais.grid(row=0, column=0, pady=1, padx=13)

combo = ttk.Combobox(selecione_frame, width=15, font=("Ivy 8 bold"))
combo.grid(row=0, column=1, padx=0, pady=13)







janela.mainloop()
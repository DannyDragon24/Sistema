from pathlib import WindowsPath
from tkinter import *
from PIL import Image, ImageTk
from db import database
global root
root = Tk()
root.geometry("500x500+400+100")
bd = database("data.db")
root.config(bg="white")
root.resizable(0,0)
root.title("BANCO SOFITASA")
usuario = StringVar()
password = StringVar()
imagen = ImageTk.PhotoImage(Image.open("sofitasa.jpg").resize((150,150)))
canvas = Canvas(root,width=600,height=500)
canvas.pack(fill=BOTH,expand=True)
canvas.create_image(180,30,image=imagen,anchor="nw",tags="imagen")
canvas.create_text(255,220,text="Usuario",font=("Arial",15),fill="black")
entrada_usuario = Entry(root,textvariable=usuario,font=("Arial",13))
canvas.create_window(170,250,anchor="nw",window=entrada_usuario)
canvas.create_text(255,300,text="Contraseña",font=("Arial",15),fill="black")
entrada_password = Entry(root,textvariable=password,font=("Arial",13),show="*")
canvas.create_window(170,330,anchor="nw",window=entrada_password)

def pantalla_sistema():
    root.destroy()
    #------variables------
    global window
    window = Tk()
    window.title("BANCO SOFITASA")
    window.geometry("650x380")
    nombre = StringVar()
    apellido = StringVar()
    edad = StringVar()
    pago = StringVar()
#---------------------LABELS Y ENTRADAS DE TEXTO-----------------------------------------------------------
    global nombre_entry
    global apellido_entry
    global fecha_entry
    global saldo_entry
    Label(window,text="NOMBRE:",font=("Keraleeyam",13)).grid(row=0,column=0,padx=15,pady=15,sticky=W)
    nombre_entry=Entry(window,textvariable=nombre)
    nombre_entry.grid(row=0,column=1,padx=15,pady=15)
    Label(window,text="APELLIDO:",font=("Keraleeyam",13)).grid(row=0,column=2,padx=15,pady=15,sticky=W)
    apellido_entry=Entry(window,textvariable=apellido)
    apellido_entry.grid(row=0,column=3,padx=15,pady=20)
    Label(window,text="FECHA ÚLTIMO MOV:",font=("Keraleeyam",13)).grid(row=1,column=0,padx=15,pady=20,sticky=W)
    fecha_entry=Entry(window,textvariable=edad)
    fecha_entry.grid(row=1,column=1,padx=10,pady=10)
    Label(window,text="SALDO:",font=("Keraleeyam",13)).grid(row=1,column=2,padx=15,pady=15,sticky=W)
    saldo_entry=Entry(window,textvariable=pago)
    saldo_entry.grid(row=1,column=3,padx=15,pady=15)

    def mostrar():
        datos = bd.fetch()
        for i in datos:
            listbox.insert(0,i)
    
    def activos():
        datos = bd.fetch()
        ventana_mas = Tk()
        ventana_mas.geometry("450x600")
        ventana_mas.title("BANCO SOFITASA")
        Label(ventana_mas,text="",font=("Arial",13)).pack()
        Label(ventana_mas,text="Clientes más activos:",font=("Arial",14),fg="green").pack()
        Label(ventana_mas,text="",font=("Arial",13)).pack()
        Label(ventana_mas,text="Nombre y apellido  |  Saldo  |  Fecha de último mov",font=("Arial",13)).pack()
        Label(ventana_mas,text="",font=("Arial",13)).pack()
        for i in datos:
            fechas = i[5].split("/")
            fechas_menos = fechas[1]
            if int(fechas_menos) == 8:
                Label(ventana_mas,text=f"{i[1]} "+f"  {i[2]}  |"+f"{i[3]}  |"+f"{i[5]}",font=("Arial",15)).pack()
            else:
                pass
        ventana_mas.mainloop()
    def menos_activos():
        datos = bd.fetch()
        ventana_menos = Tk()
        ventana_menos.geometry("450x600")
        ventana_menos.title("BANCO SOFITASA")
        Label(ventana_menos,text="",font=("Arial",13)).pack()
        Label(ventana_menos,text="Clientes menos activos:",font=("Arial",14),fg="red").pack()
        Label(ventana_menos,text="",font=("Arial",13)).pack()
        Label(ventana_menos,text="Nombre y apellido  |  Saldo  |  Fecha de último mov",font=("Arial",13)).pack()
        Label(ventana_menos,text="",font=("Arial",13)).pack()
        for i in datos:
            fechas = i[5].split("/")
            fechas_menos = fechas[1]
            if int(fechas_menos) < 8:
                Label(ventana_menos,text=f"{i[1]} "+f"  {i[2]}  |"+f"{i[3]}  |"+f"{i[5]}",font=("Arial",15)).pack()
            else:
                pass
        ventana_menos.mainloop()
    def limpiar():
        nombre_entry.delete(0,END)
        apellido_entry.delete(0,END)
        fecha_entry.delete(0,END)
        saldo_entry.delete(0,END)
#---------------------BOTONES--------------------------------------------------------------------------------_
    Button(window,text="MÁS ACTIVOS",font=("padmaa-Bold.1.1",10),command=activos).grid(row=2,column=0,padx=10,pady=10)
    Button(window,text="MENOS ACTIVOS",font=("padmaa-Bold.1.1",10),command=menos_activos).grid(row=2,column=1)
    Button(window,text="LIMPIAR CAMPOS",font=("padmaa-Bold.1.1",10),command=limpiar).grid(row=2,column=2)
#----------------------LABEL----------------------------------------------------------------------------------
    etiquetas = Label(window,text="Nombre: | Apellido: | Saldo actual: | Último movimiento: | Fecha último mov.")
    etiquetas.grid(row=3,column=0,columnspan=5)
#---------------------LISTBOX---------------------------------------------------------------------------------
    listbox = Listbox(window,height=10,width=80)
    listbox.grid(row=4,column=0,columnspan=4)
#-----------------------FUNCIONES-----------------------------------------------------------------------------
    def seleccionar(event):
            try:
		            global seleccionar
		            index = listbox.curselection()[0]
		            seleccionar = listbox.get(index)	
		            nombre_entry.delete(0,END)
		            nombre_entry.insert(END,seleccionar[1])
		            apellido_entry.delete(0,END)
		            apellido_entry.insert(END,seleccionar[2])
		            fecha_entry.delete(0,END)
		            fecha_entry.insert(END,seleccionar[5])
		            saldo_entry.delete(0,END)
		            saldo_entry.insert(END,seleccionar[3])
            except:
                   pass
        
#---------------------SELECCIONAR-LISTBOX---------------------------------
    listbox.bind("<<ListboxSelect>>",seleccionar)
    mostrar()
    window.mainloop()


boton_acceder = Button(root,text="Acceder",font=("Arial",15),bg="light gray",command=pantalla_sistema)
canvas.create_window(215,370,anchor="nw",window=boton_acceder)
root.mainloop()

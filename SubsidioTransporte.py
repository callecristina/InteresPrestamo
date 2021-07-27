#ByCrispyCalle
###Obtiene el valor de auxilio de transporte de un trabajador
#importar la librería para GUI
from tkinter import*
from tkinter import messagebox
v=Tk()#instancia la ventana #nombre=TK¿k
v.wm_title("Pago del subsidio de transporte")
#pone el título proncipal de la venta# ventana.vm.title("titulo")
v.minsize(width=150, height=150)
# define el tamaño mínimo #venta.minzise(ancho=x,alto=y)
Label(v, text="Salario del trabajador").grid(row=0)
#texto que campaña la caja de texto #Label(ventana, "txto").grid(columna en la que va)
txtSMT=Entry(v,width=10)#instancia la entrada de datos nombre=Entry(venta,ancho)
txtSMT.grid(row=0,column=1)#ubica la celda en la primera fila en la segunda col con metodo grid

Label(v, text="Salario mínimo").grid(row=2)
#texto que campaña la caja de texto #Label(ventana, "txto").grid(columna en la que va)
txtSML=Entry(v,width=15)#instancia la entrada de datos nombre=Entry(venta,ancho)
txtSML.grid(row=2,column=1)#ubica la celda en la segunda fila en la segunda col c

Label(v, text="Auxilio de transporte").grid(row=5)
txtATV = Entry(v, width=15)
txtATV.grid(row=5, column=1)

def calcular():
    SMT=float(txtSMT.get())
    SMLV=float(txtSML.get())
    ATV=float(txtATV.get())

    if SMT<=2*SMLV:
        messagebox.showinfo("Resultado", "El valor de subsidio es " +str(ATV))
    else:
        messagebox.showinfo("Resultado", "no tiene derecho")
        
Button(v, text="Pago Auxilio", width=10, command=calcular).grid(row=6, column=0)
        
        






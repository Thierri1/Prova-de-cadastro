from tkinter import *
from tkinter import ttk,messagebox,filedialog
import mysql.connector
from mysql.connector import Error



janela=Tk()
janela.geometry('450x500')
janela.title('Lista de Cadastros:')


nome_l=Label(janela,text='Nome:')
nome_l.place(relx=0.01,rely=0.01)

dataN_l=Label(janela,text='Data de N: ')
dataN_l.place(relx=0.3,rely=0.01)

sexo_l=Label(janela,text='sexo:')
sexo_l.place(relx=0.57,rely=0.01)

cidade_l=Label(janela,text='Cidade:')
cidade_l.place(relx=0.78,rely=0.01)

global nome_v
nome_v=Entry(janela,width=15)
nome_v.place(relx=0.1,rely=0.01)
global dataN_v
dataN_v=Entry(janela,width=10)
dataN_v.place(relx=0.43,rely=0.01)
global sexo_v
sexo_v=Entry(janela,width=10)
sexo_v.place(relx=0.64,rely=0.01)
global cidade_v
cidade_v=Entry(janela,width=15)
cidade_v.place(relx=0.88,rely=0.01)

tvw=ttk.Treeview(janela,columns=('id','Nome','data Nasc.','sexo','cidade'),show='headings')

tvw.column('id',minwidth=0,width=50)
tvw.column('Nome',minwidth=0,width=150)
tvw.column('data Nasc.',minwidth=0,width=80)
tvw.column('sexo',minwidth=0,width=80)
tvw.column('cidade',minwidth=0,width=150)

tvw.heading('id',text='id')
tvw.heading('Nome',text='Nome')
tvw.heading('data Nasc.',text='data Nasc.')
tvw.heading('sexo',text='sexo')
tvw.heading('cidade',text='cidade')

tvw.grid(column=3,row=5,columnspan=5,pady=30)

try:
    con=mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password='',
    )
    comando='SELECT * FROM cliente'
    cursor=con.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    for linha in linhas:
        tvw.insert('',END,values=(linha[0],linha[1],linha[2],linha[3],linha[4]))
       

except Error as erro:
    messagebox.showerror(title='Aviso', message='conexão não estabelecida')

finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        
def Recarregar():
    try:
        con=mysql.connector.connect(
            host='localhost',
            database='colegio',
            user='root',
            password='',
        )
        comando='SELECT * FROM cliente'
        cursor=con.cursor()
        cursor.execute(comando)
        linhas=cursor.fetchall()
        for i in tvw.get_children():
            tvw.delete(i)


        for linha in linhas:
            tvw.insert('',END,values=(linha[0],linha[1],linha[2],linha[3],linha[4]))
       

    except Error as erro:
            messagebox.showerror(title='Aviso', message='conexão não estabelecida')

    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()


def add():
    try:
        con=mysql.connector.connect(
            host='localhost',
            database='colegio',
            user='root',
            password='',
        )
        
        add=f'''INSERT INTO cliente 
        (nomeCliente,dataNascimentoCliente,idSexo,idCidade)
        VALUES 
        ('{nome_v.get()}','{dataN_v.get()}','{sexo_v.get()}','{cidade_v.get()}')'''
        cursor=con.cursor()
        if nome_v.get()=='' or dataN_v.get()=='' or sexo_v.get()=='' or cidade_v.get()=='':
            messagebox.showerror(title='Aviso', message='preencha todos os campos')
            return
        cursor.execute(add)
        con.commit()
        nome_v.delete(0,END)
        dataN_v.delete(0,END)
        sexo_v.delete(0)
        cidade_v.delete(0)

        
    except:
        messagebox.showerror(title='Aviso', message='Erro ao inserir Cliente')
    

    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

            
def remover():
    try:
        con=mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password='',
        )
        itemSelecionado = tvw.selection()[0]
        valores=tvw.item(itemSelecionado,'values')
        comando=f'DELETE FROM cliente WHERE idCliente={valores[0]}'
        cursor=con.cursor()
        cursor.execute(comando)
        con.commit()
        tvw.delete(itemSelecionado)

        cursor.close()
        con.close()

        
    except:
        messagebox.showerror(title='Erro', message='Selecione um item para poder deletar')


    
    



def atualizar():
    try:
        con=mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password='',
        )
        itemSelecionado = tvw.selection()[0]
        valores=tvw.item(itemSelecionado,'values')
        comando=f'UPDATE cliente SET nomeCliente="{nome_v.get()}",dataNascimentocliente="{dataN_v.get()}",idSexo="{sexo_v.get()}",idCidade="{cidade_v.get()}" WHERE idCliente={valores[0]}'
        cursor=con.cursor()
        if nome_v.get()=='' or dataN_v.get()=='' or sexo_v.get()=='' or cidade_v.get()=='':
            messagebox.showerror(title='Aviso', message='preencha todos os campos')
            return
        cursor.execute(comando)
        con.commit()
        nome_v.delete(0,END)
        dataN_v.delete(0,END)
        sexo_v.delete(0)
        cidade_v.delete(0)

        cursor.close()
        con.close()

    except:
        messagebox.showerror(title='Erro', message='Selecione um item para poder atualizar')
        


        


    



B_add=Button(janela,text='Adicionar',command=add)
B_add.place(relx=0.01,rely=0.55)

B_remover=Button(janela,text='Remover',command=remover)
B_remover.place(relx=0.2,rely=0.55)

B_at=Button(janela,text='Atualizar',command=atualizar)
B_at.place(relx=0.38,rely=0.55)

B_ref=Button(janela,text='Recarregar Página',command=Recarregar)
B_ref.place(relx=0.57,rely=0.55)








mainloop()
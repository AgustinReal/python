from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()
root.title("Mi pimera gui")

tree = Treeview(root)
tree['columns'] = ('Nombre', 'Email')
tree.column('#0', width=0, stretch=None)
tree.column('Nombre', text="Nombre")
tree.column('Email', text="Email")

tree.grid(row=0, column=0)

tree.insert('', '1', values=('cesar mayta', 'cmayta@ed.team'))

root.mainloop()
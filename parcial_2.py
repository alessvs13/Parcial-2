import tkinter as tk
from tkinter import messagebox, ttk
import firebase_admin
from firebase_admin import credentials, db
import uuid

# Inicializar Firebase
cred = credentials.Certificate("""C:\\Users\\ESTUDIANTES\\Desktop\\parcial-2-54b3c-firebase-adminsdk-fbsvc-dd6a70f9ad.json""")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://parcial-2-54b3c-default-rtdb.firebaseio.com/"
})
# Funciones funcionales puras
def crear_libro(titulo, autor, categoria):
    return {
        "id": str(uuid.uuid4()),
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponible": True
    }

def guardar_libro(libro):
    ref = db.reference('libros')
    ref.child(libro['id']).set(libro)

def consultar_libros():
    ref = db.reference('libros')
    data = ref.get()
    return list(data.values()) if data else []

def buscar_libros(filtro, valor):
    libros = consultar_libros()
    return list(filter(lambda l: l[filtro].lower() == valor.lower(), libros))

def actualizar_disponibilidad(libro_id, disponible):
    ref = db.reference(f'libros/{libro_id}')
    ref.update({"disponible": disponible})

# GUI con Tkinter
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        root.title("Sistema Biblioteca Funcional")
        root.geometry("700x500")

        self.categorias = ["Ciencia", "Literatura", "Ingeniería"]

        # Tabs
        tab_control = ttk.Notebook(root)
        self.tab_registro = ttk.Frame(tab_control)
        self.tab_consulta = ttk.Frame(tab_control)
        tab_control.add(self.tab_registro, text="Registrar")
        tab_control.add(self.tab_consulta, text="Consultar")
        tab_control.pack(expand=1, fill="both")

        self._crear_tab_registro()
        self._crear_tab_consulta()

    def _crear_tab_registro(self):
        tk.Label(self.tab_registro, text="Título").grid(row=0, column=0)
        tk.Label(self.tab_registro, text="Autor").grid(row=1, column=0)
        tk.Label(self.tab_registro, text="Categoría").grid(row=2, column=0)

        self.entry_titulo = tk.Entry(self.tab_registro)
        self.entry_autor = tk.Entry(self.tab_registro)
        self.combo_categoria = ttk.Combobox(self.tab_registro, values=self.categorias)
        self.combo_categoria.current(0)

        self.entry_titulo.grid(row=0, column=1)
        self.entry_autor.grid(row=1, column=1)
        self.combo_categoria.grid(row=2, column=1)

        tk.Button(self.tab_registro, text="Registrar Libro", command=self.registrar_libro).grid(row=3, column=1)

    def _crear_tab_consulta(self):
        tk.Label(self.tab_consulta, text="Buscar por:").grid(row=0, column=0)
        self.filtro_var = tk.StringVar(value="titulo")
        tk.Radiobutton(self.tab_consulta, text="Título", variable=self.filtro_var, value="titulo").grid(row=0, column=1)
        tk.Radiobutton(self.tab_consulta, text="Autor", variable=self.filtro_var, value="autor").grid(row=0, column=2)

        self.entry_busqueda = tk.Entry(self.tab_consulta)
        self.entry_busqueda.grid(row=1, column=0, columnspan=2)
        tk.Button(self.tab_consulta, text="Buscar", command=self.buscar).grid(row=1, column=2)

        self.tree = ttk.Treeview(self.tab_consulta, columns=("Titulo", "Autor", "Categoría", "Disponible", "ID"), show="headings")
        for col in ("Titulo", "Autor", "Categoría", "Disponible", "ID"):
            self.tree.heading(col, text=col)
        self.tree.grid(row=2, column=0, columnspan=3)

        tk.Button(self.tab_consulta, text="Marcar como Prestado", command=lambda: self.cambiar_estado(False)).grid(row=3, column=0)
        tk.Button(self.tab_consulta, text="Marcar como Devuelto", command=lambda: self.cambiar_estado(True)).grid(row=3, column=1)

    def registrar_libro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        categoria = self.combo_categoria.get()
        if not titulo or not autor:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        libro = crear_libro(titulo, autor, categoria)
        guardar_libro(libro)
        messagebox.showinfo("Éxito", "Libro registrado correctamente.")

    def buscar(self):
        filtro = self.filtro_var.get()
        valor = self.entry_busqueda.get()
        resultados = buscar_libros(filtro, valor)
        self._actualizar_tabla(resultados)

    def _actualizar_tabla(self, libros):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for libro in libros:
            self.tree.insert("", "end", values=(libro["titulo"], libro["autor"], libro["categoria"], "Sí" if libro["disponible"] else "No", libro["id"]))

    def cambiar_estado(self, disponible):
        item = self.tree.selection()
        if not item:
            messagebox.showerror("Error", "Selecciona un libro.")
            return
        libro_id = self.tree.item(item)["values"][4]
        actualizar_disponibilidad(libro_id, disponible)
        self.buscar()

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

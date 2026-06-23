import tkinter as tk

def calcular_media():
    prova1 = float(campo_p1.get())
    prova2 = float(campo_p2.get())
    trabalho = float(campo_t.get())
    licao = float(campo_l.get())
    comportamento = float(campo_c.get())

    media = (prova1 + prova2 + trabalho + licao + comportamento) / 5

    resultado_m.config(text=f"Resultado: {media:.2f}")
    
    if (media > 10):
        classific = "Erro"
        resultado_m.config(text="")
    elif (media >= 6):
        classific = "Passou na prova"
    else:
        classific = "Reprovou, voce e uma vergonha" 
        
    resultado_n.config(text=f"Resultado: {classific}")

root = tk.Tk()
root.title("calcular media")
root.geometry("800x650")

texto_p1 = tk.Label(root, text="digite a nota da prova1: ")
texto_p1.pack(pady=10)

campo_p1 = tk.Entry(root)
campo_p1.pack()

texto_p2 = tk.Label(root, text="digite a nota da prova2: ")
texto_p2.pack(pady=10)

campo_p2 = tk.Entry(root)
campo_p2.pack()

texto_t = tk.Label(root, text="digite a nota do trabalho: ")
texto_t.pack(pady=10)

campo_t = tk.Entry(root)
campo_t.pack()

texto_l = tk.Label(root, text="digite a nota da lição: ")
texto_l.pack(pady=10)

campo_l = tk.Entry(root)
campo_l.pack()

texto_c = tk.Label(root, text="digite a nota do seu comportamento em sala: ")
texto_c.pack(pady=10)

campo_c = tk.Entry(root)
campo_c.pack()

botao_calcular = tk.Button(root, text="confirmar", command= calcular_media)
botao_calcular.pack(pady=15)

resultado_m = tk.Label(root)
resultado_m.pack(pady=5)

resultado_n = tk.Label(root)
resultado_n.pack(pady=5)


root.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função para atualizar a imagem do boneco
def update_image():
    global errors
    if errors < len(images):
        img_tk = images[errors]
        image_label.config(image=img_tk)
        image_label.image = img_tk

# Função para adivinhar a letra
def guess_letter():
    global errors, guessed_letters
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    
    if letter in guessed_letters:
        messagebox.showwarning("Letra Repetida", f"A letra '{letter}' já foi tentada antes.")
        return
    
    guessed_letters.append(letter)
    guessed_label.config(text="Letras tentadas: " + " ".join(guessed_letters))
    
    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                word_display[idx] = letter
        word_label.config(text=" ".join(word_display))
    else:
        errors += 1
        update_image()

    if errors == len(images):
        messagebox.showinfo("Forca", "Você perdeu!")
    elif "_" not in word_display:
        messagebox.showinfo("Forca", "Você ganhou!")

# Função para reiniciar o jogo
def restart_game():
    global errors, word, word_display, guessed_letters

    # Resetar variáveis
    errors = 0
    word = "futebol"
    word_display = ["_" for _ in word]
    guessed_letters = []

    # Atualizar interface gráfica
    img_tk = images[0]
    image_label.config(image=img_tk)
    word_label.config(text=" ".join(word_display))
    guessed_label.config(text="Letras tentadas: ")

# Configuração inicial
errors = 0
word = "futebol"
word_display = ["_" for _ in word]
guessed_letters = []

# Configuração da janela
root = tk.Tk()
root.title("Jogo da Forca")

# Carregar as imagens
image_paths = [
    "erros/inicial.png",
    "erros/erro1.png",  
    "erros/erro2.png",          
    "erros/erro4.png",
    "erros/erro5.png",
    "erros/erro6.png",
    "erros/erro7.png",
    "erros/erro_final.png"
]

images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]

# Configuração da imagem inicial
img_tk = images[0]
image_label = tk.Label(root, image=img_tk)
image_label.pack()

# Configuração da palavra oculta
word_label = tk.Label(root, text=" ".join(word_display), font=("Helvetica", 24))
word_label.pack()

# Configuração para exibir letras tentadas
guessed_label = tk.Label(root, text="Letras tentadas: ")
guessed_label.pack()

# Entrada para adivinhar a letra
entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Adivinhar", command=guess_letter)
guess_button.pack()

restart_button = tk.Button(root, text="Reiniciar", command=restart_game)
restart_button.pack()

# Iniciar o loop principal do tkinter
root.mainloop()
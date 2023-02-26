import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex")
window.config(padx = 10, pady = 10)

title_label = tk.Label(window, text="Pokedex")
title_label.config(font = ("Arial", 32))
title_label.pack(padx = 10, pady = 10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx = 10, pady = 10)

pokemon_information = tk.Label(window)
pokemon_information.config(font = ("Arial", 20))
pokemon_information.pack(padx = 10, pady = 10)

pokemon_types = tk.Label(window)
pokemon_types.config(font = ("Arial", 20))
pokemon_types.pack(padx = 10, pady = 10)

#Function
def load_pokemon():
    pokemon = pypokedex.get(name = text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    res = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(res.data))
    
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image = img)
    pokemon_image.image = img
    
    pokemon_information.config(text = f'{pokemon.dex} - {pokemon.name}'.title())
    pokemon_types.config(text = ' & '.join([type for type in pokemon.types]).title())
    
    

label_id_name = tk.Label(window, text="ID or Name of Pokemon")
label_id_name.config(font = ("Arial", 20))
label_id_name.pack(padx = 10, pady = 10)

text_id_name = tk.Text(window, height = 1)
text_id_name.config(font = ("Arial", 20))
text_id_name.pack(padx = 10, pady = 10)

load_button = tk.Button(window, text = "Show Pokemon", command = load_pokemon)
load_button.config(font = ("Arial", 20))
load_button.pack(padx = 10, pady = 10)


window.mainloop()
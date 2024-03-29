# IMPORTS
from tkinter import filedialog
from tkinter import *

# TKINTER
TK_SILENCE_DEPRECATION = 1
root = Tk()
root.wm_withdraw()


class lfp_reader():
    # SELECCIONAR ARCHIVO
    def __init__(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("LFP", "*.lfp"), ("all files", "*.*")))

    # OBTENER
    def get_lines(self, dev_path='./menu.lfp'):
        # LEER LINEAS
        lfp_stream = open(self.filename, encoding='utf-8')
        lfp_lines = lfp_stream.read()

        # CERRAR STREAM
        lfp_stream.close()
        return lfp_lines

'''
Created 25 March 2022


'''

import tkinter as tk
from tkinter import ttk
from turtle import width

from click import command

class View(tk.Tk):
    '''
    classdocs
    '''


    PAD = 10

    MAX_BUTTON_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
        ]

    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
                
        self.title('PyCalc1.0')

        self.ControllerCalc = controller

        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._center_window()


    def main(self):
        self.mainloop() #once call infinite loop


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(
            self.main_frm, justify = 'right', 
            textvariable=self.value_var,
            state='disabled')
        ent.pack(fill='x')

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()

        buttons_in_row = 0

        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTON_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack()

                buttons_in_row = 0
            
            btn = ttk.Button(
                frm, text=caption,
            command = 
            (
                lambda button=caption: self.ControllerCalc.on_button_click(button)
                )
            )

            btn.pack(side='left')

            buttons_in_row += 1

    def _center_window(self):
        self.update()
        
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )
    
            

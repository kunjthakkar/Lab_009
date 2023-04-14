from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from poke_api import get_poke_info

#Creating the window

root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(False, False)

# adding frame to the window 
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(15,0))

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0,10))

# addding widgets to top frame

lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)

def get_pokeinfo_btn_click():
    #Find the name of teh Pokemon 
    poke_name =ent_name.get().strip()
    if poke_name == '':
        return
    
    
    #Find the Pokemon info from the PokeApi 
    poke_info = get_poke_info(poke_name)
    
    if poke_info is None:
       error_occured = f"Information about {poke_name} Pokemon is not available in the Pokeapi."
       messagebox.showinfo(title='Error', message=error_occured, icon='error')
       return

    poke_type = [type['type']['name'] for type in poke_info['types']]
    poke_type_input = ', '.join(poke_type).title()
    
    lbl_height_input['text'] = f"{poke_info['height']} dm"
    lbl_Weight_input['text'] = f"{poke_info['weight']} hg"
    lbl_type_input['text'] = poke_type_input
    
    prog_hp['value'] = poke_info['stats'][0]['base_stat']
    prog_attack['value'] = poke_info['stats'][1]['base_stat']
    prog_defense['value'] = poke_info['stats'][2]['base_stat']
    prog_special_attack['value'] = poke_info['stats'][3]['base_stat']
    prog_special_defense['value'] = poke_info['stats'][4]['base_stat']
    prog_speed['value'] = poke_info['stats'][5]['base_stat']
     
    return

btn_info = ttk.Button(frm_top, text='Get Info', command=get_pokeinfo_btn_click)
btn_info.grid(row=0, column=2)

# addding widgets to bottom left frame

lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, sticky=E)

lbl_height_input = ttk.Label(frm_btm_left, text='TBD')
lbl_height_input.grid(row=0, column=1)

lbl_Weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_Weight.grid(row=1, column=0)

lbl_Weight_input = ttk.Label(frm_btm_left, text='TBD')
lbl_Weight_input.grid(row=1, column=1)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, sticky=E)

lbl_type_input = ttk.Label(frm_btm_left, text='TBD')
lbl_type_input.grid(row=2, column=1) 
  
# addding widgets to bottom right frame

lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0,sticky=E)

prog_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_hp.grid(row=0, column=1)

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0,sticky=E)

prog_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_attack.grid(row=1, column=1,pady=5, padx=(0,5))

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0,sticky=E)

prog_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_defense.grid(row=2, column=1,pady=5, padx=(0,5))

lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0,sticky=E,)

prog_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_special_attack.grid(row=3, column=1, pady=5, padx=(0,5))

lbl_special_defense = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_special_defense.grid(row=4, column=0,sticky=E)

prog_special_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_special_defense.grid(row=4, column=1, pady=5, padx=(0,5))

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0,sticky=E)

prog_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200,maximum=255)
prog_speed.grid(row=5, column=1,padx=5,pady=5)

root.mainloop() 



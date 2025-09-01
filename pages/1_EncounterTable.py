import numpy as np
import pandas as pd
import streamlit as st
import os



#variables; saved between reruns. allows code to be written flexibly
col_labels = np.array(['Pokemon', 'Encounter Location', 'Ability', 'Nature', 'HP', 'ATK', 'DEF', 'SPATK', 'SPDEF', 'SPD'])
natures = np.array(['Hardy (Neutral)', 'Docile (Neutral)', 'Bashful (Neutral)', 'Quirky (Neutral)', 'Serious (Neutral)',
                     'Lonely (+Atk -Def)', 'Adamant (+Atk -SPAtk)', 'Naughty (+Atk -SPDef)', 'Brave (+Atk -Spd)',
                     'Bold (+Def -Atk)', 'Impish (+Def -SPAtk)', 'Lax (+Def -SPDef)', 'Relaxed (+Def -Spd)',
                     'Modest (+SPAtk -Atk)', 'Mild (+SPAtk -Def)', 'Rash (+SPAtk -SPDef)', 'Quiet (+SPAtk -Spd)',
                     'Calm (+SPDef -Atk)', 'Gentle (+SPDef -Def)', 'Careful (+SPDef -SPAtk)', 'Sassy (+SPDef -Spd)',
                     'Timid (+Spd -Atk)', 'Hasty (+Spd -Def)', 'Jolly (+Spd -SPAtk)', 'Naive (+Spd -SPDef)'])
try:
    #gets the contents of the included tables folder and filters to only show csv (table) files
    folder = os.listdir('tables')
    csvs = [file for file in folder if file.endswith('.csv')]
except OSError as e:
    print("Error:", e)

if 'file' not in st.session_state:
    st.session_state.file = None
if 'createFile' not in st.session_state:
    st.session_state.createFile = False
if 'e_table' not in st.session_state:
    st.session_state.e_table = pd.DataFrame(columns=col_labels)
if 'pokemon' not in st.session_state:
    st.session_state.pokemon = None
if 'location' not in st.session_state:
    st.session_state.location = None
if 'ability' not in st.session_state:
    st.session_state.ability = None
if 'nature' not in st.session_state:
    st.session_state.nature = None
if 'hp' not in st.session_state:
    st.session_state.hp = 0
if 'atk' not in st.session_state:
    st.session_state.atk = 0
if 'Def' not in st.session_state:
    st.session_state.Def = 0
if 'spatk' not in st.session_state:
    st.session_state.spatk = 0
if 'spdef' not in st.session_state:
    st.session_state.spdef = 0
if 'spd' not in st.session_state:
    st.session_state.spd = 0

# Callables
def addEntry() -> None:
    #puts info input into the text+number fields and formats them into an array object to be added to the dataframe
    #add error message if input fields lack a pokemon, location, and ability
    if st.session_state.pokemon == None or st.session_state.location == None or st.session_state.ability == None:
        st.warning("Required Field(s) still blank")
        return None
    st.session_state.e_table.loc[len(st.session_state.e_table)] = [st.session_state.pokemon, st.session_state.location, 
                                                                   st.session_state.ability, st.session_state.nature, 
                                                                   st.session_state.hp, st.session_state.atk, st.session_state.Def,
                                                                     st.session_state.spatk, st.session_state.spdef, st.session_state.spd]
    return None

def loadFile() -> bool: #returns bool to decide whether success message pops up
    filepath = r'tables\\' + st.session_state.file #file = None is handled in the save button
    try:
        st.session_state.e_table.read_csv(filepath)
    except IOError as e:
        print(f'Error loading the file: {e}')
    return True

def saveFile() -> bool: #returns bool to decide whether success message pops up
    filepath = r'tables\\' + st.session_state.file #file = None is handled in the save button
    try:
        st.session_state.e_table.to_csv(filepath, index=False)
    except IOError as e:
        print(f'Error saving the file: {e}')
    return True



#save/load through a file in the same folder so the local path is the same everywhere
#user chooses a file to load from a list of the files in the tables folder
file = st.container(horizontal=True, horizontal_alignment='center')
csvs = [None] + csvs #adds None as first option of selectbox
st.session_state.file = file.selectbox('Load File', csvs, format_func=lambda x: '--Select a file --' if x is None else x)
if file.button('Load'): #throws an error, needs fixed.
    if st.session_state.file is not None:
        loadFile()
if file.button('Save'):
    if st.session_state.file is None: #save as functionality 
        st.session_state.createFile = True
    else:
        saveFile()
if st.session_state.createFile: #shows inputs for creating new file
    filename = file.text_input('Enter filename')
    if file.button('Create'):
        st.session_state.file = filename + '.csv'
        saveFile()
        st.session_state.createFile = False #turns of save as inputs
        st.session_state.file = None

#Notes: Needs another input before the rerun after createFile flag is reset and new file is added to selectbox



#container and the elements it holds for user to add encounters to table. starts not expanded
with st.expander("Add Encounter"): 
    entry = st.container(horizontal=True, horizontal_alignment='center')
    #following input areas' values are updated when clicking out of area
    st.session_state.pokemon = entry.text_input('Pokemon')
    st.session_state.location = entry.text_input('Location')
    st.session_state.ability = entry.text_input('Ability')
    st.session_state.nature = entry.selectbox('Nature', natures)
    st.session_state.hp = entry.number_input('HP', 0, 31)
    st.session_state.atk = entry.number_input('ATK', 0, 31)
    st.session_state.Def = entry.number_input('DEF', 0, 31)
    st.session_state.spatk = entry.number_input('SPATK', 0, 31)
    st.session_state.spdef = entry.number_input('SPDEF', 0, 31)
    st.session_state.spd = entry.number_input('SPD', 0, 31)
    if entry.button('Enter'): #Button to run addEntry()
        addEntry()


st.dataframe(st.session_state.e_table)
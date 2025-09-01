''' Pokemon NUzlocke tracker that is flexible enough for any nuzlocke, base game or ROM
Features:
    Expandable talbe of enccounters showing: Pokemon, route, ability, nature, IVs and the ability to adjust typings for ROMS
    Overview Page showing: Attempt #, PB, Level Cap (enterable), evolution notifs for within the level cap, Graph of type distrobution of encounters
    Way to save, load, and delete multiple nuzlock games.
'''
# nuzlocke.py
#Landing page written by ChatGPT. Kinda upset I didnt think of doing this with the page first
import streamlit as st

st.set_page_config(
    page_title="Nuzlocke Tracker",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Nuzlocke Tracker")
st.write(
    """
    Welcome to your Pokémon Nuzlocke tracking tool!

    Use the sidebar to navigate:
    - **Encounter Table**: Log and manage your Pokémon encounters.
    - **Analysis**: Review stats and progress over time.
    """
)

# Optional: give quick links as buttons
st.subheader("Quick Navigation")
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/1_EncounterTable.py", label="📋 Encounter Table")
with col2:
    st.page_link("pages/2_Analytics.py", label="📊 Analytics")

st.divider()
st.caption("Data files are stored in the `tables/` folder.")

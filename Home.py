import streamlit as st
from config import pagesetup as ps, login as lg
from streamlit_lottie import st_lottie
import json
from PIL import Image
from streamlit_option_menu import option_menu


#0. Page Config
st.set_page_config("WrestleAI", initial_sidebar_state="collapsed", layout="wide")



#1. Login and Page Setup
if lg.check_authentication():
    ps.set_title("WrestleAI", "Home")
    #ps.set_page_overview("Overview", "**FEOC Assistant** provides a way to quickly ask about the FEOC")
    container1 = st.container()
    with container1:
        cc = st.columns(3)
        with cc[0]:
            ps.set_page_overview_no_div("Welcome to WrestleAI", "WrestleAI is cutting edge, one of a kind technology.")
            st.divider()
            st.markdown("**Purchasers**")
            st.markdown("""```
                    By choosing to back reduced emission products, you set a commendable standard. Every purchase you make takes us one step closer to a cleaner, better world.
                    """)
        with cc[1]:
            image = Image.open("./assets/logo.png")
            st.image(image)
        with cc[2]:
            ps.set_page_overview_no_div("Welcome to WrestleAI", "WrestleAI is cutting edge, one of a kind technology.")
            st.divider()
            st.markdown("**Purchasers**")
            st.markdown("""```
                    By choosing to back reduced emission products, you set a commendable standard. Every purchase you make takes us one step closer to a cleaner, better world.
                    """)

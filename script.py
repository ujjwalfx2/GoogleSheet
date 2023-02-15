import gspread
import pandas as pd
import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
#from gsheetsdb import connect
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder


sa = gspread.service_account(filename='gsheet-323820-f62dfdb6d200.json')
sh = sa.open('D_R')
wks = sh.worksheet('D_R')


#print ('Rows :', wks.row_count)
#i9=20
#wks.update('I9', 20)
# dataframe (create or import it)
# df = pd.DataFrame({'SlNo':[1,2], 'Facility Name':['X', 'Y']})
# df_values = df.values.tolist()
# sh.values_append('D_R', {'valueInputOption': 'RAW'}, {'values': df_values})
st.set_page_config(page_title="Google sheet streamlit app", page_icon=":hospital:", layout="centered")
st.title("Google sheet streamlit app :hospital:")

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Sheet", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)
if selected == "Data Sheet":
    st.header(f"Data Sheet")
    df = pd.DataFrame(data = wks.get_all_values())
    
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    st.dataframe(df)
    #st.markdown("---")
    
if selected == "Data Visualization":
    st.header(f"Data Visulization")
    #st.bar_chart(data=df)




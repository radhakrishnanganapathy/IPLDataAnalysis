from database import get_db
from models import IPL 
import streamlit as st
import pandas as pd
st.write("Cricket")

def main():
     # with get_db() as db:
     db = next(get_db())
     result = IPL.get_data()
     st.write(pd.DataFrame(result))

def head():
     result = IPL.head_to_head()
     st.write(pd.DataFrame(result))


if __name__ == "__main__":
     head()
     # main()

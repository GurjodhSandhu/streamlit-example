import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!yes

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
#create something
def login():
    username = input("Username: ")
    password = input("Password: ")

    # You can replace the condition with your own authentication logic
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Invalid credentials.")

login()

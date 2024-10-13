
import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'quotes' not in st.session_state:
    st.session_state.quotes = [
        "Life is what happens when you're busy making other plans. — John Lennon",
        "Get busy living or get busy dying. — Stephen King",
        "You only live once, but if you do it right, once is enough. — Mae West",
        "Many of life’s failures are people who did not realize how close they were to success when they gave up. — Thomas A. Edison",
        "If you want to live a happy life, tie it to a goal, not to people or things. — Albert Einstein"
    ]

def display_quote():
    quote = st.session_state.quotes[st.session_state.count]
    st.write(quote)

def next_quote():
    if st.session_state.count + 1 >= len(st.session_state.quotes):
        st.session_state.count = 0
    else:
        st.session_state.count += 1

def previous_quote():
    if st.session_state.count > 0:
        st.session_state.count -= 1

st.title("Inspirational Quotes")

display_quote()

col1, col2 = st.columns(2)

with col1:
    if st.button("⏮️ Previous", on_click=previous_quote):
        pass

with col2:
    if st.button("Next ⏭️", on_click=next_quote):
        pass

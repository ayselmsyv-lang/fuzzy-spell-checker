import streamlit as st
from spell_checker import load_words, get_suggestions

st.title("Smart Fuzzy Spell Checker")

word = st.text_input("Enter a word:")

max_distance = st.slider("Max edit distance:", 1, 5, 2)
top_n = st.slider("Number of suggestions:", 1, 10, 5)

dictionary = load_words("words.txt")

if st.button("Check"):
    suggestions = get_suggestions(word, dictionary, max_distance, top_n)

    if suggestions:
        st.success(f"Best suggestion: {suggestions[0][0]}")
        st.table(
            [{"Suggestion": w, "Edit distance": d} for w, d in suggestions]
        )
    else:
        st.warning("No close suggestion found.")
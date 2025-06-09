import streamlit as st


pg = st.navigation({
    "Français": [
        st.Page("conjugaison.py", title="Conjugaison de verbes", icon="📝", default=True)
        ],
    "Mathématiques": [
        st.Page("operation.py", title="Opérations sur nombres", icon="📐")
        ],
})

pg.run()
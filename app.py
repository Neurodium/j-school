import streamlit as st

pg = st.navigation({
        "Admin": [
            st.Page("db.py", title="Database", icon="📝")
            ],
        "Français": [
            st.Page("conjugaison.py", title="Conjugaison de verbes", icon="📝", default=True)
            ],
        "Mathématiques": [
            st.Page("operation.py", title="Opérations sur nombres", icon="📐")
            ],
    })

pg.run()




    
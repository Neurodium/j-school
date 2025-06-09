import streamlit as st
from spellchecker import SpellChecker
from mlconjug3 import Conjugator
from verbe import get_random_verb
from larousse_api import larousse


# initialize the conjugator
conjugator = Conjugator()

# Titre de l'application
st.title("Conjugaison de verbes français")

# Générateur de verbe aléatoire
init = get_random_verb()

# Initialisation du verbe
if 'verb' not in st.session_state:
    st.session_state.verb = init

# Bouton pour générer un verbe aléatoire
gen_verb = st.button("Générer un verbe aléatoire")
if gen_verb:
    st.session_state.verb = get_random_verb()

head1, head2, head3 = st.columns(3)
with head2:
    st.header(st.session_state.verb)

st.subheader("Définition du verbe")
st.subheader(larousse.get_definitions(st.session_state.verb)[0])

mode = st.radio("Choisissez le mode de conjugaison", ["Indicatif", "Subjonctif", "Conditionnel", "Impératif", "Participe"],
    horizontal=True)
if mode == "Indicatif":
    temps = st.radio("Choisissez le temps de conjugaison", ["Présent", "Imparfait", "Futur", "Passé Simple"],
        horizontal=True)
elif mode == "Subjonctif":
    temps = st.radio("Choisissez le temps de conjugaison", ["Présent", "Imparfait"],
        horizontal=True)
elif mode == "Conditionnel":
    temps = st.radio("Choisissez le temps de conjugaison", ["Présent"],
        horizontal=True)
elif mode == "Impératif":
    temps = st.radio("Choisissez le temps de conjugaison", ["Imperatif Présent"],
        horizontal=True)
elif mode == "Participe":
    temps = st.radio("Choisissez le temps de conjugaison", ["Participe Présent", "Participe Passé"],
        horizontal=True)

conj = conjugator.conjugate(st.session_state.verb)

st.header(f"Conjugaison du verbe {st.session_state.verb}")
st.subheader(f"{mode} {temps}")


je = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 1ère personne du singulier (je) :")
if je:
    if je == conj[mode][temps]["je"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['je']}")

tu = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 2ème personne du singulier (tu) :")
if tu:
    if tu == conj[mode][temps]["tu"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['tu']}")

il = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 3ème personne du singulier (il/elle/on) :")
if il:
    if il == conj[mode][temps]["il (elle, on)"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['il']}")

nous = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 1ère personne du pluriel (nous) :")
if nous:
    if nous == conj[mode][temps]["nous"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['nous']}")

vous = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 2ème personne du pluriel (vous) :")
if vous:
    if vous == conj[mode][temps]["vous"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['vous']}")

ils = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la 3ème personne du pluriel (ils/elles) :")
if ils:
    if ils == conj[mode][temps]["ils (elles)"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. La bonne réponse est : {conj[mode][temps]['ils']}")
import streamlit as st
from mlconjug3 import Conjugator
from verbe import get_random_verb
from larousse_api import larousse


@st.cache_resource
def get_conjugator():
    return Conjugator()

conjugator = get_conjugator()

@st.cache_data
def get_definition(verb):
    defs = larousse.get_definitions(verb)
    return defs[0] if defs else "Définition non trouvée."

# Titre de l'application
st.title("Conjugaison de verbes français")

# Initialisation du verbe
if 'verb' not in st.session_state:
    st.session_state.verb = get_random_verb()

# Bouton pour générer un verbe aléatoire
if st.button("🎲 Générer un verbe aléatoire", key="btn_gen_verb_main"):
    st.session_state.verb = get_random_verb()

head1, head2, head3 = st.columns(3)
with head2:
    st.header(st.session_state.verb)

st.subheader("Définition du verbe")
st.subheader(get_definition(st.session_state.verb))

# Choix du mode et du temps
mode = st.radio("Choisissez le mode de conjugaison", ["Indicatif", "Subjonctif", "Conditionnel", "Impératif", "Participe"],
                horizontal=True)

temps_disponibles = {
    "Indicatif": ["Présent", "Imparfait", "Futur", "Passé Simple"],
    "Subjonctif": ["Présent", "Imparfait"],
    "Conditionnel": ["Présent"],
    "Impératif": ["Imperatif Présent"],
    "Participe": ["Participe Présent", "Participe Passé"]
}
temps = st.radio("Choisissez le temps de conjugaison", temps_disponibles[mode], horizontal=True)

conj = conjugator.conjugate(st.session_state.verb)

st.header(f"Conjugaison du verbe {st.session_state.verb}")
st.subheader(f"{mode} {temps}")


pronoms = {
    "je": "1ère personne du singulier",
    "tu": "2ème personne du singulier",
    "il (elle, on)": "3ème personne du singulier",
    "nous": "1ère personne du pluriel",
    "vous": "2ème personne du pluriel",
    "ils (elles)": "3ème personne du pluriel"
}

for pronom, description in pronoms.items():
    saisie = st.text_input(f"Conjuge le verbe {st.session_state.verb} à la {description} ({pronom}) :", key=f"{pronom}_{mode}_{temps}")
    if saisie:
        bonne_reponse = conj[mode][temps].get(pronom) or conj[mode][temps].get(pronom.split(" ")[0])
        if saisie == bonne_reponse:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. La bonne réponse est : {bonne_reponse}")
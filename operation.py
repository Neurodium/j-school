import streamlit as st
import random

def reset_session_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def add(a, b):
    """Additionne deux nombres."""
    return a + b 

def substract(a, b): 
    """Soustrait le deuxième nombre du premier."""
    return a - b    

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b    

def divide(a, b):       
    """Divise le premier nombre par le deuxième."""
    if b == 0:
        return "Erreur: Division par zéro"
    return round(a / b,2)  # Arrondi à deux décimales

def random_unit_number():
    """Génère un nombre aléatoire entre 1 et 9."""
    return random.randint(1, 9)

def random_two_digit_number():
    """Génère un nombre aléatoire entre 10 et 99."""
    return random.randint(10, 99)

def random_three_digit_number():
    """Génère un nombre aléatoire entre 100 et 999."""
    return random.randint(100, 999)

def random_four_digit_number():
    """Génère un nombre aléatoire entre 1000 et 9999."""
    return random.randint(1000, 9999)

def assign_a_b_operations(ope):
    for i in range(st.session_state[ope]["nb"]):
        if ope in ["add", "multiply", "divide"]:
            # Pour les additions, on génère des nombres selon le nombre de chiffres spécifié
            if st.session_state[f"nb_a_{ope}"] == 1:
                a = random_unit_number()
            elif st.session_state[f"nb_a_{ope}"] == 2:
                a = random_two_digit_number()
            elif st.session_state[f"nb_a_{ope}"] == 3:
                a = random_three_digit_number()
            else:
                a = random_four_digit_number()

            if st.session_state[f"nb_b_{ope}"] == 1:
                b = random_unit_number()
            elif st.session_state[f"nb_b_{ope}"] == 2:
                b = random_two_digit_number()
            elif st.session_state[f"nb_b_{ope}"] == 3:
                b = random_three_digit_number()
            else:
                b = random_four_digit_number()
        elif ope == "substract":
            # Pour les soustractions, on s'assure que le premier nombre est plus grand que le second
            if st.session_state[f"nb_a_{ope}"] == 1:
                a = random.randint(2, 9)
            elif st.session_state[f"nb_a_{ope}"] == 2:
                a = random.randint(11, 99)
            elif st.session_state[f"nb_a_{ope}"] == 3:
                a = random.randint(101, 999)
            else:
                a = random.randint(1001, 9999)

            if st.session_state[f"nb_b_{ope}"] == 1:
                b = random.randint(1, a - 1)
            elif st.session_state[f"nb_b_{ope}"] == 2:
                b = random.randint(10, a - 1)
            elif st.session_state[f"nb_b_{ope}"] == 3:
                random.randint(100, a - 1)
            else:
                random.randint(1000, a - 1)
        st.session_state[ope]["a"].append(a)
        st.session_state[ope]["b"].append(b)
        
def calculate_operations(ope):
    """Calculates the results of the operations."""
    for i in range(st.session_state[ope]["nb"]):
        if ope == "add":
            st.session_state[ope]["result"].append(add(st.session_state[ope]["a"][i], st.session_state[ope]["b"][i]))
        elif ope == "substract":
            st.session_state[ope]["result"].append(substract(st.session_state[ope]["a"][i], st.session_state[ope]["b"][i]))
        elif ope == "multiply":
            st.session_state[ope]["result"].append(multiply(st.session_state[ope]["a"][i], st.session_state[ope]["b"][i]))
        elif ope == "divide":
            st.session_state[ope]["result"].append(divide(st.session_state[ope]["a"][i], st.session_state[ope]["b"][i]))     

def input_operations(ope):
    """Affiche les entrées utilisateur pour les opérations."""
    for i in range(st.session_state[ope]["nb"]):
        if len(st.session_state[ope]["user_input"]) == st.session_state[ope]["nb"]:
            if ope == "add":
                st.session_state[ope]["user_input"][i] = st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} + {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None)
            elif ope == "substract":
                st.session_state[ope]["user_input"][i] = st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} - {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None)
            elif ope == "multiply":
                st.session_state[ope]["user_input"][i] = st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} * {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None)
            elif ope == "divide":
                st.session_state[ope]["user_input"][i] = st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} / {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None)
        else:
            if ope == "add":
                st.session_state[ope]["user_input"].append(st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} + {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None))
            elif ope == "substract":
                st.session_state[ope]["user_input"].append(st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} - {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None))
            elif ope == "multiply":
                st.session_state[ope]["user_input"].append(st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} * {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None))
            elif ope == "divide":
                st.session_state[ope]["user_input"].append(st.number_input(f'Quel est le résultat de {st.session_state[ope]["a"][i]} / {st.session_state[ope]["b"][i]} ?', key=f'{ope}_{i}',value=None, step=None))
        if st.session_state[ope]["user_input"][i]:
            if st.session_state[ope]["user_input"][i] == st.session_state[ope]["result"][i]:
                st.success("✅ Correct!")
            else:
                st.error(f'❌ Incorrect. La bonne réponse est : {st.session_state[ope]["result"][i]}')


if "add" not in st.session_state:
    st.session_state.add = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}
if "substract" not in st.session_state:
    st.session_state.substract = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}    
if "multiply" not in st.session_state:
    st.session_state.multiply = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}
if "divide" not in st.session_state:
    st.session_state.divide = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}

add1, add2, add3 = st.columns([1.1, 1, 1])
with add1:
    add_op = st.number_input("Combien d'opérations d'addition souhaitez-vous générer ?", min_value=0, max_value=10, value=3, key="nb_add")
with add2:
    nb_a_add = st.number_input("Nombre de chiffres pour A (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_a_add")
with add3:
    nb_b_add = st.number_input("Nombre de chiffres pour B (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_b_add")
sub1, sub2, sub3 = st.columns([1.1, 1, 1])
with sub1:
    substract_op = st.number_input("Combien d'opérations de soustraction souhaitez-vous générer ?", min_value=0, max_value=10, value=3, key="nb_substract")
with sub2:
    nb_a_sub = st.number_input("Nombre de chiffres pour A (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_a_substract")
with sub3:
    nb_b_sub = st.number_input("Nombre de chiffres pour B (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_b_substract")
mult1, mult2, mult3 = st.columns([1.1, 1, 1])
with mult1:
    multiply_op = st.number_input("Combien d'opérations de multiplication souhaitez-vous générer ?", min_value=0, max_value=10, value=3, key="nb_multiply")
with mult2:
    nb_a_mult = st.number_input("Nombre de chiffres pour A (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_a_multiply")
with mult3:
    nb_b_mult = st.number_input("Nombre de chiffres pour B (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_b_multiply")
div1, div2, div3 = st.columns([1.1, 1, 1])
with div1:
    divide_op = st.number_input("Combien d'opérations de division souhaitez-vous générer ?", min_value=0, max_value=10, value=3, key="nb_divide")
with div2:
    nb_a_div = st.number_input("Nombre de chiffres pour A (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_a_divide")
with div3:
    nb_b_div = st.number_input("Nombre de chiffres pour B (1, 2, 3 ou 4 chiffres) :", min_value=1, max_value=4, value=1, key="nb_b_divide")

reset = st.button("Réinitialiser les opérations")
if reset:
    reset_session_state()
    st.session_state.add = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}
    st.session_state.substract = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []} 
    st.session_state.multiply = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []} 
    st.session_state.divide = {"nb": 0, "a": [], "b": [], "result": [], "user_input": []}

gen_operation = st.button("Générer les opérations")
if gen_operation:
    st.session_state.add = {"nb": add_op, "a": [], "b": [], "result": [], "user_input": []}
    st.session_state.substract = {"nb": substract_op, "a": [], "b": [], "result": [], "user_input": []} 
    if nb_b_sub != 1:
        for i in range(nb_b_sub):
            st.session_state.substract[f"result{i+1}"] = []
    st.session_state.multiply = {"nb": multiply_op, "a": [], "b": [], "result": [], "user_input": []} 
    st.session_state.divide = {"nb": divide_op, "a": [], "b": [], "result": [], "user_input": []}

    for ope in ["add", "substract", "multiply", "divide"]:
        assign_a_b_operations(ope)
        calculate_operations(ope)



for ope in ["add", "substract", "multiply", "divide"]:
    if ope == "add":
        st.header("Additions")
    elif ope == "substract":
        st.header("Soustractions")
    elif ope == "multiply":
        st.header("Multiplications")
    elif ope == "divide":
        st.header("Divisions")
    input_operations(ope)

st.write(st.session_state)

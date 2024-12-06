import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd
# Nos données utilisateurs doivent respecter ce format

utilisateurs = pd.read_csv("utilisateurs.csv", sep=';')

dico_utilisateur={}


lesDonneesDesComptes ={'usernames': {}}


for i in utilisateurs.index:
    # print(i)
    dico_utilisateur.update({utilisateurs.loc[i,'name']: {'name': utilisateurs.loc[i,'name'],
    'password': utilisateurs.loc[i,"password"],
    'email': utilisateurs.loc[i,'email'],
    'failed_login_attemps': utilisateurs.loc[i,'failed_login_attemps'], 
    'logged_in': utilisateurs.loc[i,'logged_in'], 
    'role': utilisateurs.loc[i,'role']}})
    # print(dico_utilisateur)
    lesDonneesDesComptes['usernames'].update(dico_utilisateur)




authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


def accueil():
    st.title("")

if st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
if st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')
if st.session_state["authentication_status"]:
    accueil()
    # Le bouton de déconnexion
    # authenticator.logout("Déconnexion")
    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    with st.sidebar:
                selection = option_menu(
                            menu_title='Menu',
                            options= ["Accueil", "Photos"]
                        )
                # Le bouton de déconnexion
                st.subheader(f"Bienvenue : {st.session_state['name']}")
                # st.session_state['name']
                authenticator.logout("Déconnexion")
            # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
                    st.title("Bienvenue sur la page d'accueil !")
                    st.image("D:\LOTUS\Documents\Formation_data_analyst\Cours\quetes\Streamlit\quete3\DSC_0051.JPG")

    elif selection == "Photos":
                    st.title("Bienvenue sur mon album photo")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.header("A cat")
                        st.image("https://static.streamlit.io/examples/cat.jpg")

                    with col2:
                        st.header("A dog")
                        st.image("https://static.streamlit.io/examples/dog.jpg")

                    with col3:
                        st.header("An owl")
                        st.image("https://static.streamlit.io/examples/owl.jpg")
                    # ... et ainsi de suite pour les autres pages


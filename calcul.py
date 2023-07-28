import streamlit as st
import pandas as pd
# from xlsxwriter import Workbook

image_path = './image.png'
st.image(image_path, use_column_width=True)

def calculate_debit_unitaire(q16, q24, t_peak, t_rain, num_filters):
    if num_filters != 0:
        debit_unitaire = q16 / num_filters
        return debit_unitaire
    else:
        return None

def calculate_Surface_unitaire(q16,num_filters,Vitesse_de_filtration):
    if Vitesse_de_filtration != 0:

        surface_unitaire = (q16 / num_filters) / Vitesse_de_filtration
        return surface_unitaire
    else:
        return None

def Vitesse_de_filtration_avec_n1_filtres(q16, num_filters, surface_unitaire):
    if surface_unitaire is not None and surface_unitaire != 0:
        vitesse_n1 = round(q16 / (num_filters - 1), 0) / surface_unitaire
        return vitesse_n1
    else:
        return None

def Vitesse_de_filtration_avec_n2_filtres(q16, num_filters, surface_unitaire):
    if surface_unitaire is not None and surface_unitaire != 0:
        vitesse_n2 = round(q16 / (num_filters - 2), 0) / surface_unitaire
        return vitesse_n2
    else:
        return None


def Vitesse_de_filtration_au_debit_de_pointe_temps_sec(t_peak, num_filters, surface_unitaire):
    if surface_unitaire is not None and surface_unitaire != 0:
        Vitesse_filtration_dp = round(t_peak / num_filters) / surface_unitaire
        return Vitesse_filtration_dp
    else:
        return None


def Vitesse_de_filtration_au_debit_de_pointe_temps_de_pluie(t_rain, num_filters, surface_unitaire):
    if surface_unitaire is not None and surface_unitaire != 0:
        Vitesse_filtration_dp_pluie = round(t_rain / num_filters / surface_unitaire, 1)
        return Vitesse_filtration_dp_pluie
    else:
        return None


def Vitesse_de_filtration_a_Q24(q24, num_filters, surface_unitaire):
    if surface_unitaire is not None and surface_unitaire != 0:
        Vitesse_de_filtration_a_Q24 = round((q24 / num_filters) / surface_unitaire, 2)
        return Vitesse_de_filtration_a_Q24
    else:
        return None

def Superficie_unitaire(long,larg):
    return long*larg

def Nombre_de_buslures_par_filtres_func(nmbre_brsl, surface_unitaire):
    if surface_unitaire is not None:
        return round(nmbre_brsl * surface_unitaire)
    else:
        return None

# Streamlit app
def main():
    st.title("Calcule")
    
    # Input fields
    q16 = st.number_input("Débit nominal Q16 (y compris retour) débit moyen EU")
    q24 = st.number_input("Débit nominal Q24 (y compris retour)")
    t_peak = st.number_input("Débit de pointe temps sec")
    t_rain = st.number_input("Débit de pointe temps de pluie")
    num_filters = st.number_input("Nombre de filtres")
    Vitesse_de_filtration = st.number_input("Vitesse de filtration") 


    
    # Calculate Débit unitaire
    debit_unitaire = calculate_debit_unitaire(q16, q24, t_peak, t_rain, num_filters)
    surface_unitaire=None
    surface_unitaire = calculate_Surface_unitaire(q16,num_filters,Vitesse_de_filtration)
    Vitesse_n1=None
    Vitesse_n1=Vitesse_de_filtration_avec_n1_filtres(q16,num_filters,surface_unitaire)
    Vitesse_n2=None
    Vitesse_n2=Vitesse_de_filtration_avec_n2_filtres(q16,num_filters,surface_unitaire)
    Vitesse_filtration_dp=None
    Vitesse_filtration_dp=Vitesse_de_filtration_au_debit_de_pointe_temps_sec(t_peak,num_filters,surface_unitaire)
    Vitesse_filtration_dp_pluie=None
    Vitesse_filtration_dp_pluie=Vitesse_de_filtration_au_debit_de_pointe_temps_de_pluie(t_rain,num_filters,surface_unitaire)
    Vitesse_de_filtration_Q24=None
    Vitesse_de_filtration_Q24=Vitesse_de_filtration_a_Q24(q24,num_filters,surface_unitaire)
    # Display result
    st.header("Résultat")
    if debit_unitaire is not None and surface_unitaire is not None and Vitesse_n1 is not None  and Vitesse_n2 is not None and Vitesse_filtration_dp is not None and Vitesse_filtration_dp_pluie is not None and Vitesse_de_filtration_Q24 is not None :
        st.write("Débit unitaire:", debit_unitaire)
        st.write("Surface unitaire:", round(surface_unitaire,1))
        st.write("Vitesse de filtration avec n-1 filtres :", round( Vitesse_n1,1))
        st.write("Vitesse de filtration avec n-2 filtres :",  round(Vitesse_n2,1))
        st.write("Vitesse_de_filtration_au_debit_de_pointe_temps_sec :",  round(Vitesse_filtration_dp,1))
        st.write("Vitesse_de_filtration_au_debit_de_pointe_temps_de_pluie :",  round(Vitesse_filtration_dp_pluie,1))
        st.write("Vitesse_de_filtration_a_Q24 :",  round(Vitesse_de_filtration_Q24,1))

    else:
        st.error("Entrer les valeur requis svp")
    #second input 
    long= st.number_input("Longueur d'une cellule")
    larg = st.number_input("Largeur d'une cellule ")

    #calcul 2
    Superficie_uni=None
    Superficie_uni=Superficie_unitaire(long,larg)

###############
   


    # Display result 2
    st.header("Résultat")
    if Superficie_uni is not None:
        st.write("Surface unitaire:", round(Superficie_uni,1))
        
    #third input 
    Nombre_buslures_m2= st.number_input("Nombre de buslures par m2")

    #calcul 3
    Nombre_de_buslures_par_filtres=None
    Nombre_de_buslures_par_filtres=Nombre_de_buslures_par_filtres_func(Nombre_buslures_m2,surface_unitaire)
    
    #calcul 4
    Nombre_de_buslures_total=None

    if surface_unitaire is not None:
        Nombre_de_buslures_total = Nombre_buslures_m2 * surface_unitaire * num_filters
    else:
        Nombre_de_buslures_total = None
   
 
    # Display result 3
    st.header("Résultat")
    if Nombre_de_buslures_par_filtres is not None and  Nombre_de_buslures_total is not None:
        st.write("Nombre de buslures par filtres:", Nombre_de_buslures_par_filtres)
        st.write("Nombre de buslures total :", Nombre_de_buslures_total)


    Vitesse_de_lavage_eau = st.number_input("Vitesse de lavage eau")
    Vitesse_de_lavage_air = st.number_input("Vitesse de lavage air")

    #calcul 5
    Debit_lavage_eau = Superficie_uni * Vitesse_de_lavage_eau
    Débit_lavage_air = Superficie_uni * Vitesse_de_lavage_air

    if Débit_lavage_air != 0:
        largeur_canal = Debit_lavage_eau / Débit_lavage_air
    else:
        largeur_canal = None

    st.header("Résultat")
    if None not in [Debit_lavage_eau, Superficie_uni, Vitesse_de_lavage_eau, Débit_lavage_air]:
        st.write("Débit de lavage eau:", Debit_lavage_eau)
        st.write("Débit de lavage air:", Débit_lavage_air)
        st.write("Largeur canal de reprise eau de lavage:", largeur_canal)

    if st.button("Export to XLSX"):
        # Create a dictionary with the results
        results = {
            "Débit unitaire": [debit_unitaire],
            "Surface unitaire": [round(surface_unitaire, 1)],
            "Vitesse de filtration avec n-1 filtres": [round(Vitesse_n1, 1)],
            "Vitesse de filtration avec n-2 filtres": [round(Vitesse_n2, 1)],
            # Include other results...
        }

        # Create a Pandas DataFrame from the results
        df = pd.DataFrame(results)
        writer = pd.ExcelWriter("results.xlsx", engine="xlsxwriter")

        # Export the DataFrame to XLSX
        df.to_excel(writer, sheet_name="Results", index=False)
        writer.save()
        st.success("Results exported to results.xlsx")

    st.download_button(
        label="Download Results (XLSX)",
        data="./results.xlsx",
        file_name="results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == "__main__":
    main()

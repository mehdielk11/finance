import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, OptionMenu, StringVar
from customtkinter import *

def calculate_present_value(v0_entry, t_entry, n_entry):
    try:
        v0 = float(v0_entry.get())
        t = float(t_entry.get())
        n = float(n_entry.get())

        if t == 0:
            messagebox.showerror("Error", "Le taux ne peut pas être nul.")
            return

        # Calculate present value (Va) Fin de période using the formula
        vaf = v0 * ((1 - (1 + t)**(-n)) / t)
        
        vad = v0 * (1+t) * ((1 - (1 + t)**(-n)) / t)
        # Display the calculated present value in a message box
        messagebox.showinfo("Calcul de la Valeur Actuelle", f"Valeur Actuelle en Fin de Période : {vaf:.2f}\n\nValeur Actuelle en Début de Période: {vad:.2f}")


    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")

def perform_discount(principal_entry, discount_rate_entry):
    principal = float(principal_entry.get())
    discount_rate = float(discount_rate_entry.get())

    # Example calculation (replace with your discount logic)
    discounted_amount = principal * (1 - (discount_rate / 100))

    messagebox.showinfo("Calcul de l'Escompte", f"Montant Escompté: {discounted_amount:.2f}")
      
def calculate_valeur_acquise(t_entry, periods_var, v0_entry, n_entry, custom_period_entry):
    try:
        t = float(t_entry.get())  # Annual tax rate
        v0 = float(v0_entry.get())  # Initial value
        n = float(n_entry.get())  # Number of periods

        # Parse the selected periods per year value
        selected_periods = periods_var.get()

        if selected_periods == "valeur personnalisée":
            # Custom periods per year value
            p = float(custom_period_entry.get())
        else:
            # Predefined periods per year value
            p = float(selected_periods.split(" (")[1].rstrip(")"))

        # Calculate Tax Per Period (tp)
        tp = ((1 + t) ** (1 / p)) - 1

        # Calculate Acquired Value (vA) Fin de période :
        vaf = v0 * (((1 + tp) ** n) - 1) / tp
        
        # Calculate Acquired Value (vA) Début de période :
        vad = v0 * (1 + tp) * (((1 + tp) ** n ) - 1) / tp
        
        # Display the calculated Acquired Value in a message box
        messagebox.showinfo("Calcul de la Valeur Acquise", f"Valeur Acquise en Fin de Période : {vaf:.2f}\n\nValeur Acquise en Début de Période : {vad:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")


def show_valeur_acquise_window():
    valeur_acquise_window = CTkToplevel(window)
    valeur_acquise_window.title("Calcul de la Valeur Acquise")
    valeur_acquise_window.geometry("350x430")
    valeur_acquise_window.grab_set()

    # Label and Entry for t (Annual Tax Rate)
    t_label = CTkLabel(valeur_acquise_window, text="Taux Annuel (t):", font=('Arial', 15))
    t_label.pack(pady=10)
    t_entry = CTkEntry(valeur_acquise_window, width=150)
    t_entry.pack()

    # Label and ComboBox for p (Periods per Year)
    p_label = CTkLabel(valeur_acquise_window, text="Périodes par an (p):", font=('Arial', 15))
    p_label.pack(pady=10)

    # Define predefined period options
    periods_options = [
        "mois (12)",
        "jour (365)",
        "semestre (2)",
        "trimestre (3)",
        "valeur personnalisée"
    ]

    periods_var = StringVar(valeur_acquise_window)
    periods_var.set(periods_options[0])  # Default value

    # Create a CTkComboBox for the dropdown
    periods_combobox = CTkComboBox(valeur_acquise_window, values=periods_options, width=150)
    periods_combobox.pack(pady=10)

    # Entry for custom periods per year (hidden by default)
    custom_period_entry = CTkEntry(valeur_acquise_window, width=150, placeholder_text='valeur personnalisée')
    custom_period_entry.pack(pady=5)
    custom_period_entry.configure(state="normal")  # Initially disabled

    # Function to enable/disable custom period entry based on selection
    def toggle_custom_period_entry(selected_option):
        if selected_option == "valeur personnalisée":
            custom_period_entry.configure(state="normal")
        else:
            custom_period_entry.configure(state="disabled")

    # Bind the toggle function to the combobox
    periods_combobox.bind("<<ComboboxSelected>>", lambda event: toggle_custom_period_entry(periods_combobox.get()))

    # Label and Entry for v0 (Initial Value)
    v0_label = CTkLabel(valeur_acquise_window, text="Valeur initiale (v0):")
    v0_label.pack(pady=10)
    v0_entry = CTkEntry(valeur_acquise_window, width=150)
    v0_entry.pack()

    # Label and Entry for n (Number of Periods)
    n_label = CTkLabel(valeur_acquise_window, text="Nombre de périodes (n):")
    n_label.pack(pady=10)
    n_entry = CTkEntry(valeur_acquise_window, width=150)
    n_entry.pack()

    # Button to calculate
    calculate_button = CTkButton(valeur_acquise_window, text="Calculer", command=lambda: calculate_valeur_acquise(t_entry, periods_combobox, v0_entry, n_entry, custom_period_entry))
    calculate_button.pack(pady=20)

def show_valeur_actuelle_window():
    form_window = CTkToplevel(window)
    form_window.title("Calcul de la Valeur Actuelle")
    form_window.geometry("350x300")
    form_window.grab_set()
    # Label and Entry for V0 (Valeur initiale)
    v0_label = CTkLabel(form_window, text="V0 (Valeur initiale):", font=('Arial', 15))
    v0_label.pack(pady=10)
    v0_entry = CTkEntry(form_window, width=150)
    v0_entry.pack()

    # Label and Entry for t (Taux)
    t_label = CTkLabel(form_window, text="t (Taux par Période):", font=('Arial', 15))
    t_label.pack(pady=10)
    t_entry = CTkEntry(form_window, width=150)
    t_entry.pack()

    # Label and Entry for n (Nombre de périodes)
    n_label = CTkLabel(form_window, text="n (Nombre de périodes):", font=('Arial', 15))
    n_label.pack(pady=10)
    n_entry = CTkEntry(form_window, width=150)
    n_entry.pack()

    # Button to calculate present value
    calculate_button = CTkButton(form_window, text="Calculer", command=lambda: calculate_present_value(v0_entry, t_entry, n_entry))
    calculate_button.pack(pady=20)

def show_annuities_window():
    annuities_window = CTkToplevel(window)
    annuities_window.title("Annuités Constantes")
    annuities_window.geometry("300x150")
    annuities_window.grab_set()
    # Label and Options for annuity type selection
    annuity_type_label = CTkLabel(annuities_window, text="Sélectionnez le type d'annuité:", font=('Arial', 15))
    annuity_type_label.pack(pady=10)

    annuity_type = StringVar(annuities_window)
    annuity_type.set("Valeur Acquise")  # Default value
    type_options = OptionMenu(annuities_window, annuity_type, "Valeur Acquise", "Valeur Actuelle", command=lambda value: handle_annuity_type(value))
    type_options.pack(pady=10)

    def handle_annuity_type(value):
        if value == "Valeur Acquise":
            show_valeur_acquise_window()
        elif value == "Valeur Actuelle":
            show_valeur_actuelle_window()

def calculate_simple_interest(principal_amount, period_value, period_category):
    try:
        principal = float(principal_amount)
        period_value = float(period_value)
        
        # Determine the 'categ' value based on the period category
        if period_category == "années":
            categ = 100
        elif period_category == "mois":
            categ = 1200
        elif period_category == "jours":
            categ = 36000
        else:
            messagebox.showerror("Error", "Période invalide.")
            return
        
        # Open the Simple Interest window
        show_simple_interest_window(principal, period_value, categ)
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")


def calculate_simple_interest_value(capital_amount, tax_rate, period_value, categ):
    try:
        capital = float(capital_amount)
        tax = float(tax_rate)
        
        # Calculate simple interest based on the provided parameters
        simple_interest = (capital * tax * period_value) / categ
        
        # Display the calculated simple interest value
        messagebox.showinfo("Intérêt Simple Calculé", f"Intérêt Simple: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")


def convert_to_years(period_category, period_value):
    if period_category == "jours":
        return period_value / 365  # Assuming 1 year = 365 days
    elif period_category == "mois":
        return period_value / 12  # 1 year = 12 months
    elif period_category == "années":
        return period_value  # Already in years
    else:
        return None

def show_simple_interest_window(principal, period_value, categ):
    simple_interest_window = CTkToplevel()
    simple_interest_window.title("Intérêt Simple")
    simple_interest_window.geometry("300x250")
    simple_interest_window.grab_set()
    # Label and Entry for capital amount (C)
    capital_label = CTkLabel(simple_interest_window, text="Montant du Capital (C) :", font=('Arial', 15))
    capital_label.pack(pady=10)
    capital_entry = CTkEntry(simple_interest_window, width=150)
    capital_entry.pack()

    # Label and Entry for tax rate (t)
    tax_label = CTkLabel(simple_interest_window, text="Taux d'Intérêt (t) :", font=('Arial', 15))
    tax_label.pack(pady=10)
    tax_entry = CTkEntry(simple_interest_window, width=150)
    tax_entry.pack()

    # Button to calculate simple interest value
    calculate_button = CTkButton(simple_interest_window, text="Calculer", font=('Arial', 15), 
                              command=lambda: calculate_simple_interest_value(capital_entry.get(), tax_entry.get(), period_value, categ))
    calculate_button.pack(pady=20)
    
def calculate_and_display_interest(C, t, principal, period_value, categ):
    try:
        C = float(C)
        t = float(t)
        # Calculate the simple interest
        interest = calculate_interest(C, t, period_value, categ)
        
        # Display the calculated simple interest
        result_label = CTkLabel(text=f"Intérêt Simple Calculé: {interest:.2f}")
        result_label.pack(padx=20, pady=20)
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")

def calculate_compound_interest(C, t, n):
    try:
        C = float(C)
        t = float(t)
        n = float(n)

        # Calculate compound interest (i)
        i = C * (((1 + t) ** n) - 1)

        # Calculate Valeur Acquise (VA)
        VA = C * ((1 + t) ** n)

        # Calculate Valeur Actuelle (C)
        if t != 0:
            Cv = VA * ((1 + t) ** (-n))

        return i, VA, Cv
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")

def show_compound_interest_window(principal, period_value):
    compound_interest_window = CTkToplevel()
    compound_interest_window.title("Intérêt Composé")
    compound_interest_window.geometry("350x300")
    compound_interest_window.grab_set()
    # Labels and Entries for input values
    C_label = CTkLabel(compound_interest_window, text="Capital Initial (C):", font=('Arial', 15))
    C_label.pack(pady=10)
    C_entry = CTkEntry(compound_interest_window, width=150)
    C_entry.pack()

    t_label = CTkLabel(compound_interest_window, text="Taux par Période (t):", font=('Arial', 15))
    t_label.pack(pady=10)
    t_entry = CTkEntry(compound_interest_window, width=150)
    t_entry.pack()

    n_label = CTkLabel(compound_interest_window, text="Nombre de Périodes (n):", font=('Arial', 15))
    n_label.pack(pady=10)
    n_entry = CTkEntry(compound_interest_window, width=150)
    n_entry.pack()

    # Button to calculate compound interest and display results
    def calculate_and_display():
        C = C_entry.get()
        t = t_entry.get()
        n = n_entry.get()

        # Calculate compound interest, Valeur Acquise, and Valeur Actuelle
        result = calculate_compound_interest(C, t, n)
        if result:
            i, VA, Cv = result
            messagebox.showinfo("Résultats : Intérêt Composé", f"Intérêt Composé (i): {i:.2f}\nValeur Acquise (VA): {VA:.2f}\nValeur Actuelle (C): {Cv:.2f}")

    calculate_button = CTkButton(compound_interest_window, text="Calculer", font=('Arial', 15), command=calculate_and_display)
    calculate_button.pack(pady=20)
    
    
def show_interest_window():
    interest_window = CTkToplevel(window)
    interest_window.title("Calcul d'Intérêt")
    interest_window.geometry("300x350")
    interest_window.grab_set()
    
    # Label and Entry for principal amount
    principal_label = CTkLabel(interest_window, text="Montant Principal :", font=('Arial', 15))
    principal_label.pack(pady=10)
    principal_entry = CTkEntry(interest_window, width=150)
    principal_entry.pack()

    # Label and ComboBox for period categories
    period_label = CTkLabel(interest_window, text="Période :", font=('Arial', 15))
    period_label.pack(pady=10)
    
    period_categories = ["années", "mois", "jours"]

    # Function to handle combobox selection
    def handle_combobox_selection(event):
        period_category = period_combobox.get()
        print("Selected period category:", period_category)

    period_combobox = CTkComboBox(interest_window, values=period_categories)
    period_combobox.pack(pady=10)
    period_combobox.configure(state="readonly")
    period_combobox.bind("<<ComboboxSelected>>", handle_combobox_selection)

    # Entry for the period value
    period_value_label = CTkLabel(interest_window, text="Valeur de la période :", font=('Arial', 15))
    period_value_label.pack(pady=10)
    period_value_entry = CTkEntry(interest_window, width=150, font=('Arial', 15))
    period_value_entry.pack()

    # Button to calculate interest
    def calculate_interest():
        principal = principal_entry.get()
        period_value = float(period_value_entry.get())
        period_category = period_combobox.get()
        
        # Convert period value to years
        period_in_years = convert_to_years(period_category, period_value)
        
        if period_in_years is None:
            CTkMessageBox.showerror("Error", "Période invalide.")
            return
        
        # Determine which interest calculation window to open
        if period_in_years <= 1:
            show_simple_interest_window(principal, period_value, 100)  # Using categ = 100 for years
        else:
            show_compound_interest_window(principal, period_value)

    calculate_button = CTkButton(interest_window, text="Continuer", font=('Arial', 15), command=calculate_interest)
    calculate_button.pack(pady=20)



def show_discount_window():
    discount_window = CTkToplevel(window)
    discount_window.title("Opérations d'Escompte")
    discount_window.geometry("300x200")
    discount_window.grab_set()
    # Label and Entry for principal amount
    principal_label = CTkLabel(discount_window, text="Montant Principal :")
    principal_label.pack(pady=10)
    principal_entry = CTkEntry(discount_window, width=150)
    principal_entry.pack()

    # Label and Entry for discount rate
    discount_rate_label = CTkLabel(discount_window, text="Taux d'Escompte (%):")
    discount_rate_label.pack(pady=10)
    discount_rate_entry = CTkEntry(discount_window, width=150)
    discount_rate_entry.pack()

    # Button to calculate discounted amount
    calculate_discount_button = CTkButton(discount_window, text="Calculer l'Escompte", command=lambda: perform_discount(principal_entry, discount_rate_entry))
    calculate_discount_button.pack(pady=20)





def calculate_valeur_actuelle_progressive(V0, q, n, t):
    try:
        V0 = float(V0)
        q = float(q)
        n = float(n)
        t = float(t)

        # Calculate Valeur Actuelle en Fin de Périodes
        Vaf = V0 * (((1 + t) ** -1) * ((q ** n) * ((1 + t) ** -n) - 1) / (q * ((1 + t) ** -1) - 1))

        # Calculate Valeur Actuelle en Début de Périodes
        Vad = V0 * (((q ** n) * ((1 + t) ** -n) - 1) / (q * ((1 + t) ** -1) - 1))

        return Vaf, Vad
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")


# Function to handle 'Valeur Actuelle' selection for progressive annuities
def show_valeur_actuelle_progressive_window():
    valeur_actuelle_window = CTkToplevel(window)
    valeur_actuelle_window.title("Valeur Actuelle en Annuités Progressives")
    valeur_actuelle_window.geometry("300x400")
    valeur_actuelle_window.grab_set()
    # Labels and Entries for input values
    v0_label = CTkLabel(valeur_actuelle_window, text="V0 (Versement):", font=('Arial', 15))
    v0_label.pack(pady=10)
    v0_entry = CTkEntry(valeur_actuelle_window, width=150)
    v0_entry.pack()

    q_label = CTkLabel(valeur_actuelle_window, text="q (Progression Géométrique):", font=('Arial', 15))
    q_label.pack(pady=10)
    q_entry = CTkEntry(valeur_actuelle_window, width=150)
    q_entry.pack()

    n_label = CTkLabel(valeur_actuelle_window, text="n (Nombre de périodes):", font=('Arial', 15))
    n_label.pack(pady=10)
    n_entry = CTkEntry(valeur_actuelle_window, width=150)
    n_entry.pack()

    t_label = CTkLabel(valeur_actuelle_window, text="t (Taux par Période):", font=('Arial', 15))
    t_label.pack(pady=10)
    t_entry = CTkEntry(valeur_actuelle_window, width=150)
    t_entry.pack()

    # Button to calculate and display results
    calculate_button = CTkButton(valeur_actuelle_window, text="Calculer", command=lambda: perform_valeur_actuelle_calculation(v0_entry.get(), q_entry.get(), n_entry.get(), t_entry.get()))
    calculate_button.pack(pady=20)

def perform_valeur_actuelle_calculation(V0, q, n, t):
    Vaf, Vad = calculate_valeur_actuelle_progressive(V0, q, n, t)
    if Vaf is not None and Vad is not None:
        result_window = CTkToplevel(window)
        result_window.title("Résultats : Valeur Actuelle en Annuités Progressives")
        result_window.geometry("400x150")
        result_window.grab_set()
        vaf_label = CTkLabel(result_window, text=f"Valeur Actuelle en Fin de Périodes : {Vaf:.2f}")
        vaf_label.pack(pady=10)

        vad_label = CTkLabel(result_window, text=f"Valeur Actuelle en Début de Périodes : {Vad:.2f}")
        vad_label.pack(pady=10)
    else:
        messagebox.showerror("Error", "Une erreur s'est produite lors du calcul.")

def calculate_valeur_acquise_progressive(V0, q, n, t):
    try:
        V0 = float(V0)
        q = float(q)
        n = float(n)
        t = float(t)

        # Calculate Valeur Aquise en Fin de Périodes 
        Vaf = V0 * ((1 + t) ** (n - 1)) * ((q ** n) * ((1 + t) ** -n) - 1) / (q * ((1 + t) ** -1) - 1)

        # Calculate Valeur Aquise en Début de Périodes
        Vad = V0 * ((1 + t) ** n) * ((q ** n) * ((1 + t) ** -n) - 1) / (q * ((1 + t) ** -1) - 1)

        return Vaf, Vad
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")

def show_valeur_acquise_progressive_window():
    valeur_acquise_window = CTkToplevel(window)
    valeur_acquise_window.title("Calcul : Valeur Aquise en Annuités Progressives")
    valeur_acquise_window.geometry("350x400")
    valeur_acquise_window.grab_set()
    # Labels and Entries for input values
    v0_label = CTkLabel(valeur_acquise_window, text="V0 (Versement):", font=('Arial', 15))
    v0_label.pack(pady=10)
    v0_entry = CTkEntry(valeur_acquise_window, width=150)
    v0_entry.pack()

    q_label = CTkLabel(valeur_acquise_window, text="q (Progression Géométrique):", font=('Arial', 15))
    q_label.pack(pady=10)
    q_entry = CTkEntry(valeur_acquise_window, width=150)
    q_entry.pack()

    n_label = CTkLabel(valeur_acquise_window, text="n (Nombre de Périodes):", font=('Arial', 15))
    n_label.pack(pady=10)
    n_entry = CTkEntry(valeur_acquise_window, width=150)
    n_entry.pack()

    t_label = CTkLabel(valeur_acquise_window, text="t (Tax par Période):", font=('Arial', 15))
    t_label.pack(pady=10)
    t_entry = CTkEntry(valeur_acquise_window, width=150)
    t_entry.pack()

    # Button to calculate and display results
    calculate_button = CTkButton(valeur_acquise_window, text="Calculer", command=lambda: perform_valeur_acquise_calculation(v0_entry.get(), q_entry.get(), n_entry.get(), t_entry.get()))
    calculate_button.pack(pady=20)

def perform_valeur_acquise_calculation(V0, q, n, t):
    Vaf, Vad = calculate_valeur_acquise_progressive(V0, q, n, t)
    if Vaf is not None and Vad is not None:
        result_window = CTkToplevel(window)
        result_window.title("Résultats : Valeur Aquise en Annuités Progressives")
        result_window.geometry("400x200")

        vaf_label = CTkLabel(result_window, text=f"Valeur Aquise en Fin de Périodes : {Vaf:.2f}")
        vaf_label.pack(pady=10)

        vad_label = CTkLabel(result_window, text=f"Valeur Aquise en Début de Périodes : {Vad:.2f}")
        vad_label.pack(pady=10)
    else:
        messagebox.showerror("Error", "Une erreur s'est produite lors du calcul.")

# Function to show options for progressive annuities
def show_progressive_annuities_window():
    progressive_annuities_window = CTkToplevel(window)
    progressive_annuities_window.title("Annuités en Progression")
    progressive_annuities_window.geometry("300x150")
    progressive_annuities_window.grab_set()
    # Label and Options for annuity type selection
    annuity_type_label = CTkLabel(progressive_annuities_window, text="Sélectionnez le type d'annuité:", font=('Arial', 15))
    annuity_type_label.pack(pady=10)

    annuity_type = StringVar(progressive_annuities_window)
    annuity_type.set("Valeur Actuelle")  # Default value
    type_options = OptionMenu(
        progressive_annuities_window, annuity_type, "Valeur Actuelle", "Valeur Acquise",
        command=lambda value: handle_progressive_annuity_type(value)
    )
    type_options.pack(pady=10)

    # Function to handle the selected annuity type
    def handle_progressive_annuity_type(value):
        if value == "Valeur Actuelle":
            show_valeur_actuelle_progressive_window()
        elif value == "Valeur Acquise":
            show_valeur_acquise_progressive_window()



# Create main window
window = CTk()

window.title("Gestion Financière")

# Create buttons for each operation

interest_button = CTkButton(window, text="Calcul d'Intérêt", command=show_interest_window, width=250, font=("Arial", 15))
interest_button.pack(pady=10)

discount_button = CTkButton(window, text="Opérations d'Escompte", command=show_discount_window, width=250, font=("Arial", 15))
discount_button.pack(pady=10)

annuities_button = CTkButton(window, text="Annuités Constantes", command=show_annuities_window, width=250, font=("Arial", 15))
annuities_button.pack(pady=10)

progressive_annuities_button = CTkButton(window, text="Annuités en Progression", command=show_progressive_annuities_window, width=250, font=("Arial", 15))
progressive_annuities_button.pack(pady=10)

# combobox = CTkComboBox(master=window, values= ["années", "mois", "jours"] )
# combobox.place(relx=0.5, rely=0.5, anchor='center')
# Set window size and position
window.geometry("300x200")
set_appearance_mode("dark")
window.resizable(True, True) 
# Start the main event loop
window.mainloop()
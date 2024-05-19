import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, OptionMenu, StringVar
from customtkinter import *
from CTkMessagebox import CTkMessagebox

MONTHS_IN_YEAR = 12
DAYS_IN_YEAR = 360 

# constant annuities section

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
        CTkMessagebox(title="Calcul de la Valeur Actuelle" ,message= f"Valeur Actuelle en Fin de Période : {vaf:.2f}\n\nValeur Actuelle en Début de Période: {vad:.2f}")


    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")
      
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
        CTkMessagebox(title="Calcul de la Valeur Acquise", message= f"Valeur Acquise en Fin de Période : {vaf:.2f}\n\nValeur Acquise en Début de Période : {vad:.2f}")
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
    periods_combobox.configure(state='readonly')
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
    type_options.configure(font=('Arial', 10))
    type_options.pack(pady=10)

    def handle_annuity_type(value):
        if value == "Valeur Acquise":
            show_valeur_acquise_window()
        elif value == "Valeur Actuelle":
            show_valeur_actuelle_window()


# interest section

def open_interest_window():
    # Create a new window for interest calculations
    interest_window = CTkToplevel()
    interest_window.title("Calcul d'Intérêt")
    interest_window.grab_set()
    interest_window.geometry('250x220')

    # Label for period category selection
    category_label = CTkLabel(interest_window, text="Sélectionnez la période :", font=('Arial', 15))
    category_label.pack(pady=5)

    
    category_options = [
        "years",
        "months",
        "days",
    ]
    category_var = StringVar(interest_window)
    category_var.set(category_options[0])
    category_combobox = CTkComboBox(master=interest_window, values=category_options, width=150, variable=category_var, font=('Arial', 14))
    category_combobox.configure(state='readonly')
    category_combobox.pack(pady=5)

    # Entry for period value
    value_label = CTkLabel(interest_window, text="Valeur de la période:", font=('Arial', 15))
    value_label.pack(pady=5)
    value_entry = CTkEntry(interest_window, width=150)
    value_entry.pack(pady=5)

    def continue_button_click():
        period_category = category_var.get()
        try:
            period_value = float(value_entry.get())

            if period_category == "years":
                period_in_years = period_value
            elif period_category == "months":
                period_in_years = period_value / MONTHS_IN_YEAR
            elif period_category == "days":
                period_in_years = period_value / DAYS_IN_YEAR
            else:
                period_in_years = 0

            if period_in_years <= 1:
                open_simple_interest_window(period_in_years)
            else:
                open_compound_interest_window(period_in_years)

        except ValueError:
            messagebox.showerror("Error", "Veuillez entrer une valeur numérique valide pour la période.")

    # Continue button to proceed based on the selected period
    continue_button = CTkButton(interest_window, text="Continuer", command=continue_button_click, font=('Arial', 15), width=150)
    continue_button.pack(pady=20)

def open_simple_interest_window(period_in_years):
    # Create a new window for simple interest calculation
    simple_interest_window = CTkToplevel()
    simple_interest_window.title("Intérêt Simple")
    simple_interest_window.grab_set()
    simple_interest_window.geometry("300x200")
    
    # Predefined interest rate options
    # predefined_rates = [5, 6, 7, 8, 9]  # Example predefined interest rates in percentage

    # Function to calculate simple interest
    def calculate_simple_interest(principal, rate, time):
        try:
            principal_value = float(principal.get())
            
            # Check if rate is a custom value or predefined
            if rate_var.get() == 'Custom':
                rate_value = float(custom_rate_entry.get())  # Custom rate entered by the user
            else:
                rate_value = float(rate_var.get())  # Predefined rate selected

            # Calculate the simple interest
            categ = 100  # Default category for 'years'
            if period_in_years <= 1:
                categ = 100
            elif period_in_years > 1 / MONTHS_IN_YEAR:
                categ = 1200
            elif period_in_years > 1 / DAYS_IN_YEAR:
                categ = 36000

            # Calculate the simple interest using the provided formula

            simple_interest = (principal_value * rate_value * period_in_years) / categ
            valeur_actuelle = principal_value - simple_interest
            CTkMessagebox(title="Intérêt Simple Calculé", message= f"Intérêt Simple: {simple_interest:.2f}\nValeur Actuelle: {valeur_actuelle:.2f}").geometry("300x200")
        except ValueError:
            messagebox.showerror("Error", "Veuillez entrer des valeurs numériques valides.")

    # Labels and entries for principal, rate, and time period
    principal_label = CTkLabel(simple_interest_window, text="Capital :", font=('Arial', 15))
    principal_label.pack(pady=5)
    principal_entry = CTkEntry(simple_interest_window)
    principal_entry.pack(pady=5)

    # OptionMenu for selecting interest rate
    rate_label = CTkLabel(simple_interest_window, text="Taux d'Intérêt (%):", font=('Arial', 15))
    rate_label.pack(pady=5)

    # Define rate selection variable
    predefined_rates = ['Custom', '5', '6', '7', '8', '9']
    # Define rate selection variable
    rate_var = StringVar(simple_interest_window)
    rate_var.set('5')  # Default selection
    rate_option_menu = CTkComboBox(master=simple_interest_window, values=predefined_rates, width=150, variable=rate_var)
    rate_option_menu.configure(state='readonly')
    # rate_option_menu.configure(font=('Arial', 10))
    rate_option_menu.pack(pady=5)

    # Entry field for custom interest rate
    custom_rate_label = CTkLabel(simple_interest_window, text="Taux d'Intérêt personnalisé (%):", font=('Arial', 15))
    custom_rate_entry = CTkEntry(simple_interest_window)

    # Function to show/hide custom rate entry based on selection
    def show_hide_custom_rate_entry(selected_value):
        if selected_value == 'Custom':
            custom_rate_label.pack(pady=5)
            custom_rate_entry.pack(pady=5)
            simple_interest_window.geometry("300x280")
        else:
            custom_rate_label.pack_forget()
            custom_rate_entry.pack_forget()
            simple_interest_window.geometry("300x200")

    # Update custom rate entry visibility when the OptionMenu selection changes
    rate_var.trace('w', lambda *args: show_hide_custom_rate_entry(rate_var.get()))

    # Calculate button for simple interest
    calculate_button = CTkButton(simple_interest_window, text="Calculer Intérêt Simple", font=('Arial', 15),
                                  command=lambda: calculate_simple_interest(principal_entry, rate_var, period_in_years))
    
    # Pack the button to always appear at the bottom
    calculate_button.pack(side='bottom', pady=10)

    # Initially hide the custom rate entry
    show_hide_custom_rate_entry(rate_var.get())

def open_compound_interest_window(period_in_years):
    # Create a new window for compound interest calculation
    compound_interest_window = CTkToplevel()
    compound_interest_window.title("Intérêt Composé")
    compound_interest_window.grab_set()
    compound_interest_window.geometry("300x330")

    # Predefined interest rates
    predefined_rates = [1, 2.5, 5, 10, "Custom"]

    # Function to calculate compound interest, future value, and present value
    def calculate_compound_interest(principal, rate, periods):
        try:
            principal_value = float(principal.get())
            rate_value = float(rate.get()) / 100  # Convert rate to decimal
            periods_value = float(periods.get())

            # Calculate compound interest
            compound_interest = principal_value * ((1 + rate_value) ** periods_value - 1)

            # Calculate future value (valeur acquise)
            future_value = principal_value * (1 + rate_value) ** periods_value

            # Calculate present value (valeur actuelle)
            present_value = future_value / ((1 + rate_value) ** periods_value)

            CTkMessagebox(title="Résultats de l'Intérêt Composé", message=
                                f"Montant d'Escompte: {compound_interest:.2f}\n\n"
                                f"Valeur Acquise: {future_value:.2f}\n\n"
                                f"Valeur Actuelle: {present_value:.2f}").geometry("350x250")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

    # Labels and entries for principal, rate, and periods
    principal_label = CTkLabel(compound_interest_window, text="Capital (C):", font=('Arial', 15))
    principal_label.pack(pady=10)
    principal_entry = CTkEntry(compound_interest_window)
    principal_entry.pack(pady=5)

    periods_label = CTkLabel(compound_interest_window, text="Nombre de Périodes (n):", font=('Arial', 15))
    periods_label.pack(pady=10)
    periods_entry = CTkEntry(compound_interest_window)
    periods_entry.pack(pady=5)
    
    # OptionMenu for interest rate selection
    rate_label = CTkLabel(compound_interest_window, text="Taux d'Intérêt par Période (%):", font=('Arial', 15))
    rate_label.pack(pady=10)

    predefined_rates = ['1', '2.5', '5', '10', "Custom"] # DROPDOWN MENU OPTIONS
    
    # Variable to store the selected rate
    selected_rate = StringVar(compound_interest_window)
    selected_rate.set(predefined_rates[0])  # Set initial value

    # Function to handle rate selection
    def handle_rate_selection(value):
        if value == "Custom":
            # Show custom rate entry
            rate_entry.pack(pady=0)
            compound_interest_window.geometry("300x360")
        else:
            # Hide custom rate entry
            rate_entry.pack_forget()
            compound_interest_window.geometry("300x330")

    # OptionMenu for rate selection
    rate_option_menu = CTkComboBox(master=compound_interest_window, variable=selected_rate, values=predefined_rates, command=handle_rate_selection)
    rate_option_menu.configure(font=('Arial', 13))
    rate_option_menu.configure(state='readonly')
    rate_option_menu.pack(pady=5)

    # Entry field for custom rate
    rate_entry = CTkEntry(compound_interest_window, placeholder_text='valeur personnalisée')

    # periods_label = CTkLabel(compound_interest_window, text="Nombre de Périodes (n):", font=('Arial', 15))
    # periods_label.pack(pady=10)
    # periods_entry = CTkEntry(compound_interest_window)
    # periods_entry.pack(pady=5)

    # Calculate button for compound interest
    calculate_button = CTkButton(compound_interest_window, text="Calculer Intérêt Composé", font=('Arial', 15),
                                  command=lambda: calculate_compound_interest(principal_entry, rate_entry if selected_rate.get() == "Custom" else selected_rate, periods_entry))
    calculate_button.pack(side='bottom', pady=20)


# escompte section

def show_discount_window():
    discount_window = CTkToplevel(window)
    discount_window.title("Opérations d'Escompte")
    discount_window.geometry("300x350")
    discount_window.grab_set()
    # Label and Entry for principal amount
    principal_label = CTkLabel(discount_window, text="Montant Principal :", font=('Arial', 15))
    principal_label.pack(pady=10)
    principal_entry = CTkEntry(discount_window, width=150)
    principal_entry.pack()

    # Label and Entry for discount rate
    discount_rate_label = CTkLabel(discount_window, text="Taux d'Escompte (%):", font=('Arial', 15))
    discount_rate_label.pack(pady=10)
    discount_rate_entry = CTkEntry(discount_window, width=150)
    discount_rate_entry.pack()

    period_label = CTkLabel(discount_window, text="Nombre de jours :", font=('Arial', 15))
    period_label.pack(pady=10)
    period_entry = CTkEntry(discount_window, width=150)
    period_entry.pack(pady=5)
    
    # Button to calculate discounted amount
    calculate_discount_button = CTkButton(discount_window, text="Calculer l'Escompte", command=lambda: perform_discount(principal_entry, discount_rate_entry, period_entry), font=('Arial', 15))
    calculate_discount_button.pack(pady=10)
    
    # calculate taux réel ( agios tva )
    calculate_real_rate = CTkButton(discount_window, text="Calculer le Taux Réel", command=lambda: show_real_rate_window(), font=('Arial', 15))
    calculate_real_rate.pack(pady=5)
 
def show_real_rate_window():
    real_rate_window = CTkToplevel(window)
    real_rate_window.title("Taux Réel d'Escompte")
    real_rate_window.geometry("300x400")
    real_rate_window.grab_set()
    # Label and Entry for principal amount
    principal_label = CTkLabel(real_rate_window, text="Montant Principal :", font=('Arial', 15))
    principal_label.pack(pady=5)
    principal_entry = CTkEntry(real_rate_window, width=150)
    principal_entry.pack()

    # Label and Entry for discount rate
    discount_rate_label = CTkLabel(real_rate_window, text="Taux d'Escompte (%) :", font=('Arial', 15))
    discount_rate_label.pack(pady=5)
    discount_rate_entry = CTkEntry(real_rate_window, width=150)
    discount_rate_entry.pack()

    period_label = CTkLabel(real_rate_window, text="Nombre de jours :", font=('Arial', 15))
    period_label.pack(pady=5)
    period_entry = CTkEntry(real_rate_window, width=150)
    period_entry.pack()
    
    tva_rate_label = CTkLabel(real_rate_window, text="Taux de TVA (%) :", font=('Arial', 15))
    tva_rate_label.pack(pady=5)
    tva_rate_entry = CTkEntry(real_rate_window, width=150)
    tva_rate_entry.pack()
    
    commissions_label = CTkLabel(real_rate_window, text="Total de commissions:", font=('Arial', 15))
    commissions_label.pack(pady=5)
    commissions_entry = CTkEntry(real_rate_window, width=150)
    commissions_entry.pack()
    
    
    # calculate taux réel ( agios tva )
    calculate_real_rate = CTkButton(real_rate_window, text="Calculer le Taux Réel", command=lambda: perform_real_rate(principal_entry, discount_rate_entry, period_entry, tva_rate_entry, commissions_entry), font=('Arial', 15))
    calculate_real_rate.pack(pady=20)
    
def perform_discount(principal_entry, discount_rate_entry, period_entry):
    principal = float(principal_entry.get())
    discount_rate = float(discount_rate_entry.get())
    period = int(period_entry.get())
    
    # Example calculation (replace with your discount logic)
    discounted_amount = (principal * discount_rate * period) / 36000

    # messagebox.showinfo("Calcul de l'Escompte", f"Montant Escompté: {discounted_amount:.2f}\n Valeur Actuelle: {principal - discounted_amount}")
    CTkMessagebox(title="Calcul de l'Escompte", message= f"Montant Escompté: {discounted_amount:.2f}\n Valeur Actuelle: {principal - discounted_amount}", font=('Arial', 13)).geometry("300x200")

def perform_real_rate(principal_entry, discount_rate_entry, period_entry, tva_rate_entry, commissions_entry):
    principal = float(principal_entry.get())
    discount_rate = float(discount_rate_entry.get())
    period = int(period_entry.get())
    tva_rate = float(tva_rate_entry.get())
    commissions = float(commissions_entry.get())
    
    # escompte
    discounted_amount = (principal * discount_rate * period) / 36000

    # calculate TVA
    TVA = (discounted_amount + commissions) * (tva_rate / 100)
    
    # calculate AGIOS
    AGIOS = discounted_amount + commissions + TVA
    
    # calculate real rate
    real_rate = (36000 * AGIOS) / (principal * period)

    CTkMessagebox(title="Taux Réel d'escompte", message= f"TVA : {TVA:.2f}\nAGIOS: {AGIOS:.2f}\nTaux Réel : {real_rate:.2f}%", font=('Arial', 13)).geometry("300x200")


# progressive annuities section

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
        result_window.geometry("350x150")
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
        result_window.grab_set()
        result_window.title("Résultats : Valeur Aquise en Annuités Progressives")
        result_window.geometry("350x150")

        vaf_label = CTkLabel(result_window, text=f"Valeur Aquise en Fin de Périodes : {Vaf:.2f}")
        vaf_label.pack(pady=10)

        vad_label = CTkLabel(result_window, text=f"Valeur Aquise en Début de Périodes : {Vad:.2f}")
        vad_label.pack(pady=10)
    else:
        messagebox.showerror("Error", "Une erreur s'est produite lors du calcul.")

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
    type_options.configure(font=('Arial', 10))
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
interest_menu = CTkButton(window,text="Calcul d'Intérêts", command=open_interest_window, width=250, font=("Arial", 15))
interest_menu.pack(pady=10)
# interest_button = CTkButton(window, text="Calcul d'Intérêt", command=show_interest_window, width=250, font=("Arial", 15))
# interest_button.pack(pady=10)

discount_button = CTkButton(window, text="Opérations d'Escompte", command=show_discount_window, width=250, font=("Arial", 15))
discount_button.pack(pady=10)

annuities_button = CTkButton(window, text="Annuités Constantes", command=show_annuities_window, width=250, font=("Arial", 15))
annuities_button.pack(pady=10)

progressive_annuities_button = CTkButton(window, text="Annuités en Progression", command=show_progressive_annuities_window, width=250, font=("Arial", 15))
progressive_annuities_button.pack(pady=10)

# combobox = CTkComboBox(master=window, values= ["années", "mois", "jours"] )
# combobox.pack(side="bottom")
# Set window size and position
window.geometry("300x200")
set_appearance_mode("dark")
window.resizable(True, True) 
# Start the main event loop
window.mainloop()
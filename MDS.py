import tkinter as tk
from tkinter import messagebox

# Updated facts without Bronchitis
facts = {
    "COVID-19": {"symptoms": ["fever", "cough", "breathlessness"], "type": "Viral Disease"},
    "Flu": {"symptoms": ["fever", "cough", "sore throat"], "type": "Viral Disease"},
    "Meningitis": {"symptoms": ["headache", "stiff neck", "nausea"], "type": "Bacterial Disease"},
    "Heart Disease": {"symptoms": ["chest pain", "shortness of breath"], "type": "Chronic Disease"},
    "Diabetes": {"symptoms": ["frequent urination", "increased thirst", "fatigue"], "type": "Chronic Disease"},
    "Tuberculosis": {"symptoms": ["persistent cough", "weight loss", "night sweats"], "type": "Bacterial Disease"},
    "Asthma": {"symptoms": ["wheezing", "shortness of breath", "chest tightness"], "type": "Chronic Disease"},
}

# Updated ISA hierarchy without Bronchitis
isa_hierarchy = {
    "Disease": ["Viral Disease", "Bacterial Disease", "Chronic Disease"],
    "Viral Disease": ["COVID-19", "Flu"],
    "Bacterial Disease": ["Meningitis", "Tuberculosis"],
    "Chronic Disease": ["Heart Disease", "Diabetes", "Asthma"]
}

# Predicate Logic - Check if a patient has a symptom
def has_symptom(disease, symptom):
    return symptom in facts[disease]["symptoms"]

# Predicate Logic - Check if a patient has a disease
def diagnose_disease(symptoms):
    possible_diseases = []
    for disease, info in facts.items():
        if all(symptom in symptoms for symptom in info["symptoms"]):
            return disease, []  
        if any(symptom in symptoms for symptom in info["symptoms"]):
            possible_diseases.append(disease)
    return None, possible_diseases 

# Predicate Logic - ISA relationship check
def isa(entity, category):
    return category in isa_hierarchy.get(entity, [])

# Function to assess the severity of the disease
def assess_severity(disease):
    if disease == "COVID-19":
        return "Severe. Immediate medical attention may be required."
    elif disease == "Flu":
        return "Mild. Usually treatable at home with rest."
    elif disease == "Meningitis":
        return "Severe. Emergency medical help needed."
    elif disease == "Heart Disease":
        return "Critical. Immediate medical intervention required."
    elif disease == "Diabetes":
        return "Chronic. Requires ongoing management."
    elif disease == "Tuberculosis":
        return "Serious. Medical treatment necessary."
    elif disease == "Asthma":
        return "Manageable. Requires regular treatment and monitoring."
    else:
        return "Unknown severity."

# User Interface for the Medical Diagnosis System
def run_diagnosis():
    symptoms = symptoms_entry.get().lower().split(", ")
    if not symptoms:
        messagebox.showwarning("Input Error", "Please enter your symptoms.")
        return
    
    disease, possible_diseases = diagnose_disease(symptoms)  
    
    if disease:
        result_text = f"Diagnosis: {disease}\n\nSeverity: {assess_severity(disease)}"
        result_label.config(text=result_text)
    elif possible_diseases:
        result_text = f"Possible diseases based on symptoms: {', '.join(possible_diseases)}"
        result_label.config(text=result_text)
    else:
        result_label.config(text="Unable to determine the condition. Please consult a doctor.")

# Function to clear input and output
def clear_input():
    symptoms_entry.delete(0, tk.END)
    result_label.config(text="")

# Building the UI using Tkinter
root = tk.Tk()
root.title("AI-Based Medical Diagnosis System")
root.geometry("700x500")
root.config(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="AI-Based Medical Diagnosis System", font=("Arial", 30), bg="#f0f8ff", fg="#00008b")
title_label.pack(pady=10)

# Instructions label
instructions_label = tk.Label(root, text="Enter your symptoms separated by commas (e.g., fever, cough):", font=("Arial", 14), bg="#f0f8ff")
instructions_label.pack()

# Entry field for symptoms
symptoms_entry = tk.Entry(root, width=50)
symptoms_entry.pack(pady=10)

# Button to run the diagnosis
diagnose_button = tk.Button(root, text="Diagnose", font=("Arial", 14), bg="#4682b4", fg="white", command=run_diagnosis)
diagnose_button.pack(pady=10)

# Button to clear input
clear_button = tk.Button(root, text="Clear", font=("Arial", 14), bg="#4682b4", fg="white", command=clear_input)
clear_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#00008b", justify=tk.LEFT, wraplength=500)
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

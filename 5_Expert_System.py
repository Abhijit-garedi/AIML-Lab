# Knowledge base: for each disease, list the symptoms associated with it
disease_rules = {
    "Flu": {"fever", "cough", "body ache", "fatigue"},
    "Common Cold": {"cough", "sneezing", "sore throat", "runny nose"},
    "COVID-19": {"fever", "cough", "loss of taste", "difficulty breathing", "fatigue"},
    "Malaria": {"fever", "chills", "sweating", "headache"},
    "Dengue": {"fever", "headache", "joint pain", "rash", "fatigue"},
    "Chickenpox": {"fever", "rash", "itching", "fatigue"},
    "Typhoid": {"fever", "headache", "abdominal pain", "diarrhoea"},
}



def diagnose(symptoms):
    """
    Given a set of input symptoms, compute a match score
    for each disease and return a ranked list.
    """


    scores = []



    for disease, rule_symptoms in disease_rules.items():

        matched = symptoms.intersection(rule_symptoms)

        score = (
            len(matched) / len(rule_symptoms)
            if rule_symptoms else 0.0
        )

        if score > 0:
            scores.append((disease, score, matched))



    scores.sort(key=lambda x: (-x[1], x[0]))
    return scores



def main():


    print("Welcome to the Expert System: Disease Diagnosis")
    print(
        "Enter symptoms separated by commas "
        "(e.g. fever, cough, headache). Type 'exit' to quit."
    )



    while True:

        user_input = input("\nEnter symptoms: ").strip().lower()



        if user_input == 'exit':
            print("Exiting the system. Take care!")
            break



        input_symptoms = {
            sym.strip()
            for sym in user_input.split(",")
            if sym.strip()
        }



        if not input_symptoms:
            print("Please enter at least one symptom.")
            continue



        results = diagnose(input_symptoms)



        if not results:
            print("No diseases matched your symptoms.")
        else:
            print("\nPossible diseases ranked by symptom match:")

            for disease, score, matched in results:
                percentage = score * 100
                matched_list = ", ".join(sorted(matched))

                print(
                    f"- {disease} ({percentage:.1f}% match). "
                    f"Symptoms matched: {matched_list}"
                )



if __name__ == "__main__":
    main()



"""
Output:

Welcome to the Expert System: Disease Diagnosis
Enter symptoms separated by commas (e.g. fever, cough, headache). Type 'exit' to quit.

Enter symptoms: fever,cough

Possible diseases ranked by symptom match:
- Flu (50.0% match). Symptoms matched: cough, fever
- COVID-19 (40.0% match). Symptoms matched: cough, fever
- Chickenpox (25.0% match). Symptoms matched: fever
- Common Cold (25.0% match). Symptoms matched: cough
- Malaria (25.0% match). Symptoms matched: fever
- Typhoid (25.0% match). Symptoms matched: fever
- Dengue (20.0% match). Symptoms matched: fever

Enter symptoms: exit
Exiting the system. Take care!
"""

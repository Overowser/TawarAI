import pandas as pd
from datetime import datetime
from groq import Groq
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def parse_patient_data(data):
    """
    Parse patient data from a dictionary into a human-readable report.

    Parameters
    ----------
    data : dict
        A dictionary containing the patient data.

    Returns
    -------
    str
        A human-readable report of the patient's vital signs and other information.
    """

    # Extract values
    patient_id = data.get("Patient ID")
    heart_rate = data.get("Heart Rate")
    respiratory_rate = data.get("Respiratory Rate")
    timestamp = data.get("Timestamp").split(".")[0]
    body_temp = data.get("Body Temperature")
    oxygen_saturation = data.get("Oxygen Saturation")
    systolic_bp = data.get("Systolic Blood Pressure")
    diastolic_bp = data.get("Diastolic Blood Pressure")
    age = data.get("Age")
    gender = data.get("Gender")
    weight = data.get("Weight (kg)")
    height = data.get("Height (m)")
    hrv = data.get("Derived_HRV")
    pulse_pressure = data.get("Derived_Pulse_Pressure")
    bmi = data.get("Derived_BMI")
    map_value = data.get("Derived_MAP")

    # Parse timestamp to readable format
    formatted_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

    # Generate report
    report = f"""
Rapport du Patient :
--------------------
ID du Patient : {patient_id}
Sexe : {gender}
Âge : {age} ans
Poids : {weight} kg
Taille : {height} m
IMC (Indice de Masse Corporelle) : {bmi}

Signes Vitaux :
- Fréquence Cardiaque : {heart_rate} bpm
- Fréquence Respiratoire : {respiratory_rate} respirations/min
- Température Corporelle : {body_temp} °C
- Saturation en Oxygène : {oxygen_saturation} %
- Pression Artérielle Systolique : {systolic_bp} mmHg
- Pression Artérielle Diastolique : {diastolic_bp} mmHg
- Pression Différentielle : {pulse_pressure} mmHg
- Pression Artérielle Moyenne (PAM) : {map_value} mmHg
- Variabilité de la Fréquence Cardiaque (VFC) : {hrv} ms

Date et Heure du Rapport : {formatted_timestamp.strftime('%d %b %Y, %I:%M %p')}
--------------------
    """
    return report.strip()


def generate_diagnosis(report):
    """
    Generate a diagnosis based on a patient report.

    Parameters:
        report (str): The patient report to base the diagnosis on.

    Returns:
        str: The generated diagnosis, including any additional tests or data that may be required.

    Notes:
        This function uses the Groq AI model to generate a diagnosis based on the provided patient report.
        The diagnosis will be returned in the format "Diagnostic : <diagnostic>\nTests ou Données Supplémentaires Requises : <tests ou données>".
    """
    client = Groq(api_key="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")
    # client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": f"""Vous êtes un assistant médical expert. Sur la base des données fournies sur le patient, analysez les informations et fournissez un diagnostic préliminaire ou identifiez d'éventuelles préoccupations. Prenez en compte les éléments suivants :

                            {report}

                            Soyez concis mais précis. S'il n'y a pas suffisamment d'informations pour établir un diagnostic concluant, suggérez des tests ou des données supplémentaires qui permettraient de clarifier l'état du patient. Ne faites aucune supposition sur la santé du patient.
                            Vous pouvez demander l'historique du patient si besoin.

                            Votre réponse doit être formatée comme suit :

                            Diagnostic : <diagnostic>
                            Tests ou Données Supplémentaires Requises : <tests ou données>

                            Réponse :""",
            }
        ],
        temperature=0.1,  # trying a more deterministic approach
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    diagnosis = ""

    for chunk in completion:
        diagnosis += chunk.choices[0].delta.content or ""

    return diagnosis


def generate_recommendations(report, diagnosis):
    """
    Generate recommendations based on patient report and diagnosis.

    Parameters
    ----------
    report : str
        The patient report.
    diagnosis : str
        The diagnosis of the patient.

    Returns
    -------
    str
        The recommendations for the patient, formatted as a string.

    Notes
    -----
    This function uses the Groq API to generate recommendations based on the patient report and diagnosis.
    The recommendations are generated using the LLaMA 3-70B-8192 model.
    The function returns a string containing the recommendations, formatted as follows:

        Recommandations : <recommandations>

    where <recommandations> is the generated recommendations.
    """
    client = Groq(api_key="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")
    # client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": f"""Vous êtes un assistant médical expert en soins aux patients. Ci-dessous se trouvent un rapport de patient, un diagnostic et un contexte médical pertinent. Sur la base de ces informations, fournissez des recommandations claires et actionnables, telles que des traitements ou des ajustements de style de vie.

                Rapport du Patient :
                {report}

                Diagnostic :
                {diagnosis}

                Sortie :
                Recommandations : Fournissez des étapes détaillées à suivre, incluant des traitements, des changements de mode de vie ou des tests, adaptés à l'état du patient et au contexte fourni.

                Concentrez-vous sur des recommandations spécifiques, actionnables et pertinentes pour les besoins du patient.

                Votre réponse doit être formatée comme suit, n'ajoute rien d'autre que les recommandations :

                Recommandations court terme : <recommandations court terme>
                Recommandations moyen terme : <recommandations moyen terme>
                Recommandations long terme : <recommandations long terme>

                Réponse :""",
            }
        ],
        temperature=0.1,  # trying a more deterministic approach
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    recommendations = ""
    for chunk in completion:
        recommendations += chunk.choices[0].delta.content or ""

    return recommendations


def generate_report(data):
    """
    Generate a comprehensive patient report including diagnosis and recommendations.

    Parameters
    ----------
    data : dict
        A dictionary containing patient vital signs and other relevant data.

    Returns
    -------
    str
        A formatted string containing the patient report, diagnosis, and recommendations.

    Notes
    -----
    This function consolidates the patient data into a report, generates a diagnosis based on the report,
    and provides recommendations. The final output is a comprehensive string combining all these elements.
    """
    report = parse_patient_data(data)
    diagnosis = generate_diagnosis(report)
    recommendations = generate_recommendations(report, diagnosis)

    report = report.strip() + "\n\n" + diagnosis.strip() + "\n\n" + recommendations

    return report


## for testing purposes
# patient_data = pd.read_csv("vital signs data.csv")
# vital_signs = patient_data.iloc[1].to_dict()
#print(generate_report(vital_signs))

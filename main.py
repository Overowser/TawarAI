import pandas as pd
from datetime import datetime

patient_data = pd.read_csv("vital signs data.csv")


def parse_patient_data(data):

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
    formatted_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

    # Generate report
    report = f"""
    Patient Report:
    ----------------
    Patient ID: {patient_id}
    Gender: {gender}
    Age: {age} years
    Weight: {weight} kg
    Height: {height} m
    BMI (Body Mass Index): {bmi}

    Vital Signs:
    - Heart Rate: {heart_rate} bpm
    - Respiratory Rate: {respiratory_rate} breaths/min
    - Body Temperature: {body_temp} °C
    - Oxygen Saturation: {oxygen_saturation} %
    - Systolic Blood Pressure: {systolic_bp} mmHg
    - Diastolic Blood Pressure: {diastolic_bp} mmHg
    - Pulse Pressure: {pulse_pressure} mmHg
    - Mean Arterial Pressure (MAP): {map_value} mmHg
    - Heart Rate Variability (HRV): {hrv} ms

    Report Timestamp: {formatted_timestamp.strftime('%d %b %Y, %I:%M %p')}
    ----------------
    """
    return report.strip()

    
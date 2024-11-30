from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from datetime import datetime
from io import BytesIO
import pdfkit  # For converting HTML to PDF

app = Flask(__name__)

# Read the CSV file into a global variable
patient_data = pd.read_csv("human_vital_signs_dataset_2024.csv")

def parse_patient_data(data):
    # Extract and format the patient data (same function as before)
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
    <h2>Patient Report</h2>
    <hr>
    <strong>Patient ID:</strong> {patient_id} <br>
    <strong>Gender:</strong> {gender} <br>
    <strong>Age:</strong> {age} years <br>
    <strong>Weight:</strong> {weight} kg <br>
    <strong>Height:</strong> {height} m <br>
    <strong>BMI:</strong> {bmi} <br><br>
    <h3>Vital Signs</h3>
    <ul>
        <li><strong>Heart Rate:</strong> {heart_rate} bpm</li>
        <li><strong>Respiratory Rate:</strong> {respiratory_rate} breaths/min</li>
        <li><strong>Body Temperature:</strong> {body_temp} °C</li>
        <li><strong>Oxygen Saturation:</strong> {oxygen_saturation} %</li>
        <li><strong>Systolic BP:</strong> {systolic_bp} mmHg</li>
        <li><strong>Diastolic BP:</strong> {diastolic_bp} mmHg</li>
        <li><strong>Pulse Pressure:</strong> {pulse_pressure} mmHg</li>
        <li><strong>MAP:</strong> {map_value} mmHg</li>
        <li><strong>HRV:</strong> {hrv} ms</li>
    </ul>
    <strong>Report Timestamp:</strong> {formatted_timestamp.strftime('%d %b %Y, %I:%M %p')} <br>
    <hr>
    """

    return report

@app.route('/')
def index():
    # Show the first patient report (or create a list to select a patient)
    first_patient = patient_data.iloc[0]  # for example, take the first row
    report = parse_patient_data(first_patient)
    return render_template('index.html', report=report)

@app.route('/generate_pdf')
def generate_pdf():
    first_patient = patient_data.iloc[0]  # for example, take the first row
    report = parse_patient_data(first_patient)
    
    # Path to wkhtmltopdf executable (adjust this path if necessary)
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    
    # Create a pdfkit configuration with the path to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    # Create PDF from the HTML content
    pdf = pdfkit.from_string(report, False, configuration=config)
    
    # Send the PDF as a downloadable file
    return send_file(BytesIO(pdf), download_name="patient_report.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from datetime import datetime
from io import BytesIO
import pdfkit  # For converting HTML to PDF

app = Flask(__name__, static_folder='assets')

# Read the CSV file and ensure 'Patient ID' is treated as a string
patient_data = pd.read_csv("human_vital_signs_dataset_2024.csv")
patient_data['Patient ID'] = patient_data['Patient ID'].astype(str)  # Ensuring all IDs are strings

# Number of patients per page
PATIENTS_PER_PAGE = 20

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
    # Get page number from query parameter, default to page 1 if not provided
    page = int(request.args.get('page', 1))
    
    # Calculate the start and end indices for slicing the patient data
    start = (page - 1) * PATIENTS_PER_PAGE
    end = start + PATIENTS_PER_PAGE
    patients_page = patient_data.iloc[start:end]

    # Get total number of patients to calculate the number of pages
    total_patients = len(patient_data)
    total_pages = (total_patients + PATIENTS_PER_PAGE - 1) // PATIENTS_PER_PAGE

    # Pass the flag to show patient list
    return render_template('index.html', patients=patients_page, page=page, total_pages=total_pages, show_patient_list=True)

@app.route('/patient/<patient_id>')
def patient_report(patient_id):
    # Ensure the patient_id is treated as a string for consistent comparison
    patient_id = str(patient_id)  # Convert patient_id to string
    
    # Check if patient_id exists in the DataFrame (which now has all Patient IDs as strings)
    if patient_id not in patient_data['Patient ID'].values:
        # Patient not found, return an error message or redirect to the home page
        error_message = f"Patient with ID {patient_id} not found."
        return render_template('index.html', error=error_message, show_patient_list=True, report=None)

    # Find the patient data based on the selected Patient ID
    patient = patient_data[patient_data['Patient ID'] == patient_id].iloc[0]
    report = parse_patient_data(patient)
    
    # Pass the report and hide the patient list
    return render_template('index.html', report=report, patient_id=patient_id, show_patient_list=False)

@app.route('/generate_pdf/<patient_id>')
def generate_pdf(patient_id):
    # Find the patient data based on the selected Patient ID
    patient = patient_data[patient_data['Patient ID'] == patient_id].iloc[0]
    report = parse_patient_data(patient)  # Generate the report for PDF
    
    # Path to wkhtmltopdf executable (adjust this path if necessary)
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    
    # Create a pdfkit configuration with the path to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    # Create PDF from the HTML content
    pdf = pdfkit.from_string(report, False, configuration=config)
    
    # Send the PDF as a downloadable file
    return send_file(BytesIO(pdf), download_name=f"patient_{patient_id}_report.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

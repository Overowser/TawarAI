# TawarAI - AI-Powered Emergency Healthcare Report Generation System
## Abstract
### Background and Problem Statement

In Morocco, emergency services play a critical role in the healthcare system, serving as the primary point of entry for many patients. However, there are significant inefficiencies within the system, particularly in terms of emergency response times and resource allocation. Vital emergency cases only make up around 10% of the total emergency room visits, with the remaining 50% being non-urgent consultations. Despite the high demand, the healthcare system suffers from a shortage of skilled personnel and limited resources, which can lead to delays in diagnosis and treatment.

TawarAI aims to address these challenges by providing an AI-powered solution to automate the creation of medical reports based on vital signs, enabling more efficient use of emergency services and improving overall care.

### Impact and Proposed Solution

TawarAI uses groqcloud API to call for llama 3.1 70b to assist healthcare professionals by analyzing real-time data from emergency patients, such as vital signs, and generating medical reports automatically. This technology streamlines the diagnosis process, ensuring quicker and more accurate treatment for patients in critical condition. The solution also helps optimize resource allocation, reduce the workload on medical staff, and minimize errors in documentation, ultimately improving the efficiency of emergency healthcare services.

By reducing manual report generation, TawarAI frees up medical professionals to focus on patient care, ultimately saving lives, improving decision-making, and reducing the burden on emergency departments. The solution also aims to assist in early anomaly detection, allowing healthcare professionals to intervene before a patient's condition worsens.

### Project Outcomes and Deliverables

* API: A fully functional REST API that takes vital sign data in CSV format, processes the information, and generates a medical report. The API will be designed to later integrate with IoT systems for real-time data collection.
* Web App: A user-friendly web application that allows users to upload CSV files with patient vital signs, view the AI-generated medical reports, and download the reports in PDF format.
* Report Generation: The AI system will analyze the uploaded data, process it, and generate detailed medical reports, offering diagnosis suggestions and recommendations.
* Proof of Concept: A working prototype that can be tested with Kaggle's patient vitals dataset, demonstrating the system's potential in a real-world scenario.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
  - [1. Get List of Patients](#1-get-list-of-patients)
  - [2. Generate Full Report for a Patient](#2-generate-full-report-for-a-patient)
  - [3. Download PDF Report for a Patient](#3-download-pdf-report-for-a-patient)
- [CSV File Format](#csv-file-format)
- [Error Handling](#error-handling)
- [Running the Application](#running-the-application)
- [Authors](#authors)
- [License](#license)

---

## Requirements

To run this project, you need the following dependencies:

- **Python 3.x** 
- **Flask**
- **pandas**
- **pdfkit** (for generating PDF files)
- **wkhtmltopdf** (required by pdfkit for rendering PDFs)

### Install Dependencies

Create a virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

requirements.txt
The following packages are required:

makefile
Copier le code
annotated-types==0.5.0
anyio==3.7.1
cached-property==1.5.2
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
distro==1.9.0
exceptiongroup==1.2.2
Flask==2.2.5
groq==0.11.0
h11==0.14.0
httpcore==0.17.3
httpx==0.24.1
idna==3.10
importlib-metadata==6.7.0
itsdangerous==2.1.2
Jinja2==3.1.4
MarkupSafe==2.1.5
numpy==1.21.6
pandas==1.1.5
pdfkit==1.0.0
pydantic==2.5.3
pydantic_core==2.14.6
python-dateutil==2.9.0.post0
pytz==2024.2
requests==2.31.0
six==1.16.0
sniffio==1.3.1
typing_extensions==4.7.1
urllib3==1.26.0
Werkzeug==2.2.3
zipp==3.15.0
Installation
Clone the repository to your local machine:

bash
Copier le code
git clone https://github.com/yourusername/patient-report-api.git
cd patient-report-api
Install the dependencies using pip:

bash
Copier le code
pip install -r requirements.txt
Install wkhtmltopdf to render PDF reports. Instructions are available on the wkhtmltopdf website.

Make sure wkhtmltopdf is available in your system's PATH or specify the full path in the generate_patient_pdf function.

Configuration
Ensure that the path to the wkhtmltopdf executable is correctly set in your generate_pdf function. For example:

python
Copier le code
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
For Linux or macOS users, you might have it installed as /usr/local/bin/wkhtmltopdf.

API Endpoints
1. Get List of Patients
Fetches a paginated list of patient IDs.

Request:
Method: GET
Query Parameters:
page: The page number (default is 1).
Response:
A JSON object containing:
patients: A list of patient IDs.
page: The current page number.
total_pages: The total number of pages.
curl Example:
bash
Copier le code
curl "http://127.0.0.1:5000/patients?page=1"
Example Response:
json
Copier le code
{
  "patients": ["12345", "67890", "11223", "44556", ...],
  "page": 1,
  "total_pages": 5
}
2. Generate Full Report for a Patient
Generates a full medical report for a specific patient based on their ID.

Request:
Method: GET
URL Parameter:
patient_id: The ID of the patient.
Response:
A JSON object containing the patient's report.
curl Example:
bash
Copier le code
curl "http://127.0.0.1:5000/patient_report/12345"
Example Response:
json
Copier le code
{
  "report": "Patient 12345: Full medical report content including diagnosis, vitals, and recommendations."
}
3. Download PDF Report for a Patient
Generates a downloadable PDF report for a specific patient.

Request:
Method: GET
URL Parameter:
patient_id: The ID of the patient.
Response:
A downloadable PDF file containing the full report for the patient.
curl Example (to download the PDF):
bash
Copier le code
curl -O "http://127.0.0.1:5000/generate_pdf/12345"
This will download the PDF file with the filename patient_12345_report.pdf.

CSV File Format
The API uses a CSV file (human_vital_signs_dataset_2024.csv) with the following structure:

Patient ID	Gender	Age	Weight (kg)	Height (m)	Heart Rate	Respiratory Rate	Body Temperature	Oxygen Saturation	Systolic BP	Diastolic BP	Derived BMI	Pulse Pressure	MAP	HRV
12345	Male	45	70	1.75	72	16	36.6	98	120	80	22.9	40	90	55
Columns Description:
Patient ID: Unique identifier for the patient.
Gender: Gender of the patient.
Age: Age of the patient.
Weight (kg): Weight of the patient in kilograms.
Height (m): Height of the patient in meters.
Heart Rate: Heart rate (beats per minute).
Respiratory Rate: Respiratory rate (breaths per minute).
Body Temperature: Body temperature (Celsius).
Oxygen Saturation: Oxygen saturation (%) in the blood.
Systolic BP: Systolic blood pressure (mmHg).
Diastolic BP: Diastolic blood pressure (mmHg).
Derived BMI: Body Mass Index.
Pulse Pressure: Pulse pressure (difference between systolic and diastolic).
MAP: Mean Arterial Pressure.
HRV: Heart Rate Variability.
Error Handling
404 Not Found: If the patient_id does not exist.

Example:

json
Copier le code
{
  "error": "Patient with ID 12345 not found."
}
500 Internal Server Error: If an internal error occurs (e.g., report generation failure).

Running the Application
To run the Flask app, execute the following command:

bash
Copier le code
python app.py
The app will start running on http://127.0.0.1:5000. You can test the API by sending requests to the endpoints mentioned above.

Authors
Developed by [Your Name]
License
This project is licensed under the MIT License - see the LICENSE file for details.

Additional curl Examples
1. Fetch Patient List for a Specific Page (Page 2)
bash
Copier le code
curl "http://127.0.0.1:5000/patients?page=2"
2. Generate Full Report for Patient ID 67890
bash
Copier le code
curl "http://127.0.0.1:5000/patient_report/67890"
3. Download PDF Report for Patient ID 44556
bash
Copier le code
curl -O "http://127.0.0.1:5000/generate_pdf/44556"
4. Handle Error for Non-Existent Patient ID
bash
Copier le code
curl "http://127.0.0.1:5000/patient_report/99999"
Expected Response:

json
Copier le code
{
  "error": "Patient with ID 99999 not found."
}

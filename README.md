# **TawarAI**  
## **AI-Powered Emergency Healthcare Report Generation System**

---

### **Abstract**

#### **Background and Problem Statement**  
In Morocco, emergency services are the primary entry point for many patients. Despite their importance, these services face inefficiencies in response times and resource allocation. Vital emergency cases account for only about 10% of visits, while non-urgent consultations make up 50%. This disparity, coupled with a shortage of skilled personnel and resources, delays diagnosis and treatment.  

TawarAI addresses these issues by automating medical report generation from vital signs, improving the efficiency of emergency services, and enhancing overall patient care.  

#### **Impact and Proposed Solution**  
TawarAI leverages the **groqcloud API** and **Llama 3.1 70b** model to analyze real-time patient data (e.g., vital signs) and generate medical reports. This process streamlines diagnosis, optimizes resource allocation, and minimizes documentation errors, ensuring more accurate and timely care for critical cases.  

By automating report generation, TawarAI frees medical professionals to focus on patient care, supports early anomaly detection, and improves emergency healthcare services' overall efficiency.  

---

### **Project Outcomes and Deliverables**

1. **API:**  
   A REST API that processes vital sign data in CSV format and generates AI-driven medical reports. Future iterations will integrate real-time IoT data collection.

2. **Web Application:**  
   A user-friendly web app for uploading CSV files, viewing AI-generated reports, and downloading them in PDF format.

3. **Report Generation:**  
   Detailed medical reports with diagnosis suggestions and actionable recommendations, analyzed from patient data.

4. **Proof of Concept:**  
   A working prototype tested on Kaggle's patient vitals dataset, showcasing real-world application potential.

---

## **Table of Contents**

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [API Endpoints](#api-endpoints)  
  - [Get List of Patients](#1-get-list-of-patients)  
  - [Generate Full Report](#2-generate-full-report-for-a-patient)  
  - [Download PDF Report](#3-download-pdf-report-for-a-patient)  
- [CSV File Format](#csv-file-format)  
- [Error Handling](#error-handling)  
- [Running the Application](#running-the-application)  
- [Authors](#authors)  
- [License](#license)  

---

## **Requirements**

- **Python 3.x**  
- **Flask**  
- **pandas**  
- **pdfkit**  
- **wkhtmltopdf**  

---

## **Installation**

### **Install Dependencies**
Create a virtual environment and install the required packages:  
```bash
pip install -r requirements.txt
Clone the Repository
```
```bash
git clone https://github.com/yourusername/patient-report-api.git  
cd patient-report-api
```
# Install wkhtmltopdf
Follow the installation guide on the official wkhtmltopdf website. Ensure the executable is accessible via the system's PATH.

**Configuration**
Ensure the path to wkhtmltopdf is correctly set in your generate_pdf function. For example:

```python
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
For Linux/macOS, the default path is typically /usr/local/bin/wkhtmltopdf.
```

#*API Endpoints*
1. Get List of Patients
Request:

**Method:** GET
**Query Parameters:**
```
page: Page number (default: 1)
```
Response:

```json
Copier le code
{
  "patients": ["12345", "67890", "11223"],
  "page": 1,
  "total_pages": 5
}
```

**Example:**

```bash
curl "http://127.0.0.1:5000/patients?page=1"
```

**2. Generate Full Report for a Patient
Request:**

**Method:** GET
**URL Parameter:** patient_id (Patient ID).
Response:
```json
{
  "report": "Patient 12345: Full medical report content."
}
```

Example:
```bash
curl "http://127.0.0.1:5000/patient_report/12345"
```

**3. Download PDF Report for a Patient
Request:**

**Method:** GET
**URL Parameter:** patient_id (Patient ID).
Response:
```
A downloadable PDF report.
```

Example:

```bash
curl -O "http://127.0.0.1:5000/generate_pdf/12345"
```
**CSV File Format**
The dataset (human_vital_signs_dataset_2024.csv) should have the following columns:
```
Patient ID	Gender	Age	Weight (kg)	Height (m)	Heart Rate	...	MAP	HRV
12345	Male	45	70	1.75	72	...	90	55
```

**Error Handling**
404 Not Found: If patient_id does not exist:
```json
{
  "error": "Patient with ID 12345 not found."
}
500 Internal Server Error: For unexpected failures.
```

**Running the Application**
To start the Flask application:

```bash
$python app.py
Access the app at http://127.0.0.1:5000.
```

###**Authors**
FullStack by [Aicha Lahnite]

###**License**
This project is licensed under the MIT License. See the LICENSE file for details.


# Patient Report API

This is a Flask-based API that allows the retrieval of patient information, generation of patient reports, and the creation of downloadable PDF reports. The API serves as an interface to interact with a dataset containing human vital signs, and provides various routes to fetch patient data, generate reports, and download them in PDF format.

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.x
- Flask
- pandas
- pdfkit (for PDF generation)
- wkhtmltopdf (for rendering PDFs)

### Install Dependencies

You can install all required dependencies using the `requirements.txt` file. To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This will install the necessary packages as specified in the `requirements.txt` file.

### `requirements.txt`

Here is the list of required packages:

```
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
```

Make sure `wkhtmltopdf` is installed separately. It is essential for generating PDF reports.

### Install `wkhtmltopdf`

`wkhtmltopdf` is a command-line tool used to convert HTML to PDF. The Flask API uses this tool to generate patient report PDFs. 

You can download and install `wkhtmltopdf` from [the official website](https://wkhtmltopdf.org/downloads.html).

For installation on various operating systems:

- **Windows**: Download the installer from the website and add `wkhtmltopdf` to your system PATH.
- **macOS**: You can use Homebrew:
  ```bash
  brew install wkhtmltopdf
  ```
- **Linux**: Use your package manager:
  ```bash
  sudo apt-get install wkhtmltopdf  # For Ubuntu/Debian
  sudo yum install wkhtmltopdf      # For CentOS/RHEL
  ```

### Configuring `wkhtmltopdf`

Ensure that the path to the `wkhtmltopdf` executable is correctly set in the `generate_pdf` function:

```python
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
```

For Linux or macOS, you can update the path accordingly (e.g., `/usr/local/bin/wkhtmltopdf`).

---

## Endpoints

### 1. **GET /patients**

Fetches a paginated list of patient IDs.

#### Request:
- **Method**: `GET`
- **Query Parameters**:
  - `page`: The page number (default is 1).

#### Response:
- A JSON object containing:
  - `patients`: A list of patient IDs.
  - `page`: The current page number.
  - `total_pages`: The total number of pages.

Example:
```json
{
  "patients": ["12345", "67890", "11223", ...],
  "page": 1,
  "total_pages": 5
}
```

### 2. **GET /patient_report/{patient_id}**

Generates a full report for a specific patient.

#### Request:
- **Method**: `GET`
- **URL Parameter**:
  - `patient_id`: The ID of the patient (string or integer).

#### Response:
- A JSON object containing the patient's report.

Example:
```json
{
  "report": "Full medical report content for the patient."
}
```

### 3. **GET /generate_pdf/{patient_id}**

Generates a downloadable PDF report for a specific patient.

#### Request:
- **Method**: `GET`
- **URL Parameter**:
  - `patient_id`: The ID of the patient (string or integer).

#### Response:
- A downloadable PDF file containing the full report for the specified patient.

---

## CSV File Format

The API assumes a CSV file (`human_vital_signs_dataset_2024.csv`) with the following structure:

| Patient ID | Gender | Age | Weight (kg) | Height (m) | Heart Rate | Respiratory Rate | Body Temperature | Oxygen Saturation | Systolic Blood Pressure | Diastolic Blood Pressure | Derived BMI | Derived Pulse Pressure | Derived MAP | Derived HRV |
|------------|--------|-----|-------------|------------|------------|------------------|------------------|-------------------|-------------------------|--------------------------|-------------|------------------------|-------------|-------------|
| 12345      | Male   | 45  | 70          | 1.75       | 72         | 16               | 36.6             | 98                | 120                     | 80                       | 22.9        | 40                     | 90          | 55          |

### Columns Description:

- **Patient ID**: Unique identifier for the patient.
- **Gender**: Gender of the patient.
- **Age**: Age of the patient.
- **Weight (kg)**: Weight of the patient in kilograms.
- **Height (m)**: Height of the patient in meters.
- **Heart Rate**: Heart rate of the patient in beats per minute.
- **Respiratory Rate**: Respiratory rate of the patient in breaths per minute.
- **Body Temperature**: Body temperature of the patient in Celsius.
- **Oxygen Saturation**: Oxygen saturation level of the patient in percentage.
- **Systolic Blood Pressure**: Systolic blood pressure value.
- **Diastolic Blood Pressure**: Diastolic blood pressure value.
- **Derived BMI**: Body Mass Index (BMI) derived from weight and height.
- **Derived Pulse Pressure**: Pulse pressure derived from systolic and diastolic blood pressure.
- **Derived MAP**: Mean Arterial Pressure (MAP).
- **Derived HRV**: Heart Rate Variability (HRV).

## PDF Generation

The PDF generation process uses the `wkhtmltopdf` tool to convert a report into a downloadable PDF. The `generate_patient_pdf` function formats patient data into a structured report, which is then rendered as a PDF.

---

## Error Handling

- If the `patient_id` provided does not exist in the dataset, a `404 Not Found` error is returned.
  Example:
  ```json
  {
    "error": "Patient with ID 12345 not found."
  }
  ```

- If the report generation fails, an internal server error (`500 Internal Server Error`) may occur.

## Running the Application

To run the Flask app, execute the following command:

```bash
python app.py
```

The app will start running on `http://127.0.0.1:5000`.

---

## Authors

- FullStack by Aicha LAhnite.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This is your complete `README.md` in Markdown format, which includes instructions for installation, dependencies, API usage, and how to run the application. Simply copy and paste this into your `README.md` file.

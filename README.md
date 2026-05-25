# Invoice Regression Framework

## Overview
The Invoice Regression Framework is designed to compare invoice extraction results between different releases of the system to identify validation differences, mismatches, and data quality issues.

This framework performs automated comparison of:
- Header fields
- Line item fields
- Validation status
- IPT processing results
- Before Release vs After Release outputs

The framework generates a detailed Excel comparison report for regression analysis and release validation.

---

# Features

- Automated invoice comparison
- Header validation comparison
- Line item validation comparison
- Match / Fail / Missed tracking
- Normalized data comparison
- Excel report generation
- Release validation support
- Scalable and reusable utility-based structure

---

# Project Structure

```text
invoice_regression_framework/
│
├── input/
│   ├── before_release/
│   └── after_release/
│
├── output/
│   └── Validation_PR_Report.xlsx
│
├── utils/
│   ├── header_compare.py
│   ├── lineitem_compare.py
│   ├── normalizer.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- OpenPyXL
- JSON Processing
- Excel Automation

---

# Framework Workflow

1. Read Before Release invoice data
2. Read After Release invoice data
3. Normalize extracted values
4. Compare Header fields
5. Compare Line Item fields
6. Generate validation status
7. Export final Excel report

---

# Validation Status Logic

| Status | Description |
|---|---|
| Matched | Values are identical |
| Failed | Values are different |
| Missed | Field missing in one release |

---

# How to Run

## Step 1: Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

## Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

## Step 3: Run Framework

```powershell
python main.py
```

---

# Output Report

Generated report:
```text
output/Validation_PR_Report.xlsx
```

The report contains:
- Invoice comparison summary
- Header validation details
- Line item validation details
- IPT status
- Match percentage
- Failed fields analysis

---

# Use Cases

- Release validation
- Regression testing
- Invoice extraction comparison
- OCR/IDP validation
- Production vs New Release analysis

---

# Future Enhancements

- HTML dashboard reporting
- Database integration
- API-based comparison
- Automated email report delivery
- Jenkins CI/CD integration
- Multi-format invoice support

---

# Author

Developed by Somyaranjan Sahoo

QA Automation Engineer  
Specialized in Automation Testing, API Testing, and Invoice Validation Frameworks
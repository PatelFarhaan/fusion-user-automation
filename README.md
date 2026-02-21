# Fusion Automation

Automated user provisioning and training access management system for Oracle Fusion and EBS training platforms. This Selenium-based bot automates Joomla CMS user group assignments, sends onboarding emails with training credentials, and tracks customer data via Google Sheets.

## Tech Stack

- **Language:** Python 3.6+
- **Automation:** Selenium WebDriver
- **Email:** SMTP (Gmail)
- **Data:** Google Sheets API (gspread), Pandas
- **CMS:** Joomla (automated via Selenium)

## Features

- Automated user registration and group assignment in Joomla CMS
- Training package and single-course provisioning for 90+ Oracle training modules
- Automated onboarding emails with training credentials and PDF attachments
- Google Sheets integration for customer tracking and record management
- Support for both new and existing user workflows
- Handles Oracle Fusion, EBS, and middleware training packages

## Prerequisites

- Python 3.6+
- Google Chrome browser
- ChromeDriver (matching Chrome version)
- Google Service Account JSON key file (for Sheets API access)
- Gmail account with App Password enabled

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/fusion-automation.git
cd fusion-automation

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your credentials
```

## Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Path to Google service account JSON key file |
| `SMTP_HOST` | SMTP server host (default: smtp.gmail.com) |
| `SMTP_PORT` | SMTP server port (default: 587) |
| `SMTP_USERNAME` | SMTP email address |
| `SMTP_PASSWORD` | SMTP email password or app password |
| `JOOMLA_ADMIN_URL` | Joomla admin panel URL |
| `JOOMLA_ADMIN_USERNAME` | Joomla admin panel username |
| `JOOMLA_ADMIN_PASSWORD` | Joomla admin panel password |
| `TRAINING_PASSWORDS_FILE` | Path to training passwords JSON config file |

## How to Run

```bash
# Activate virtual environment
source venv/bin/activate

# Copy and configure training passwords
cp training_passwords.json.example training_passwords.json
# Edit training_passwords.json with actual training passwords

# Load environment variables
source .env

# Run the automation script
python app.py
```

## Project Structure

```
fusion-automation/
├── app.py                              # Main automation script with training mappings
├── requirements.txt                    # Python dependencies
├── training_passwords.json.example     # Training password config template
├── .env.example                        # Environment variable template
├── google_sheet/
│   └── google.py           # Google Sheets API integration
├── mails/
│   ├── ebs_mail.py         # EBS training onboarding emails
│   ├── ebs_mail_existing.py # EBS emails for existing users
│   ├── fusion_mail.py      # Fusion training onboarding emails
│   ├── fusion_mail_existing.py # Fusion emails for existing users
│   └── images/             # Email attachments and PDF password lists
└── webdriver/
    └── chromedriver        # Chrome WebDriver binary (not tracked)
```

## License

MIT

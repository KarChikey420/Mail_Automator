# Mail Automator 📧

Automate your email-sending tasks with this simple and efficient Python-based tool. Perfect for sending bulk emails, scheduled notifications, or personalized messages without manual intervention.

## 📌 Features

- Send single or bulk emails via SMTP
- Supports HTML and plain-text email formats
- Personalize emails using templates (e.g., with names, dates, etc.)
- Configurable via `.env` file for secure credentials

## 🛠️ Requirements

- Python 3.7 or higher
- `smtplib`, `email`, `dotenv`, and other standard libraries

Install dependencies with:
```bash
pip install python-dotenv

## git clone 

git clone https://github.com/KarChikey420/Mail_Automator.git
cd Mail_Automator

## Set up your credentials
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password  
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

⚠️Note on Email Providers
For Gmail, you must enable 2-factor authentication and generate an App Password.
Other providers (Outlook, Yahoo, etc.) may require different SMTP settings—update them in .env.


📄 License
This project is open-source and available under the MIT License.

🤝 Contributing
Made with by KarChikey420


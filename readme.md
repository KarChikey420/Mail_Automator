# AI Email Assistant 📧

An intelligent email automation system that processes emails, detects spam, and generates automated replies using AI. Built with Python Flask and HTML interface.

## 🌟 Features

- **Smart Email Processing**: Automatically fetch and analyze unread emails
- **Spam Detection**: AI-powered spam classification with confidence scoring
- **Automated Replies**: Generate intelligent responses to legitimate emails
- **Modern UI**: Clean, responsive React interface with Tailwind CSS
- **Real-time Updates**: Live processing status and notifications
- **Email History**: View and search through processed emails

## 🛠️ Tech Stack

- **Python Flask** - Web framework
- **HTML/CSS** - Simple web interface
- **Gmail API** - Email integration
- **ChromaDB** - Vector database for RAG
- **AI/ML Libraries** - Spam detection and reply generation

## 📋 Prerequisites

- **Python** 3.7+
- **Gmail Account** with App Password enabled

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/KarChikey420/Mail_Automator.git
cd Mail_Automator
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

### 3. Configure Gmail Credentials
Edit `.env` file:
```env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### 4. Run the Application
```bash
python app/app.py
```

Visit `http://localhost:5000` to access the application.

## 📧 Gmail Setup Guide

### Enable 2-Factor Authentication
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification**
3. Follow the setup process

### Generate App Password
1. In **Security** settings, find **App passwords**
2. Select **Mail** and your device
3. Copy the generated 16-character password
4. Use this as `APP_PASSWORD` in your `.env` file

## 🎯 Usage

### Dashboard
- Click **"Process Unread Emails"** to analyze your inbox
- View spam detection results and generated replies
- Monitor processing status with real-time notifications

### Email History
- Switch to **"All Emails"** tab
- Search through processed emails
- View email details and AI-generated responses

## 📁 Project Structure

```
automate_email/
├── app/
│   ├── __init__.py         # Package initialization
│   ├── app.py              # Main Flask server
│   ├── chroma_db.py        # Vector database operations
│   ├── email_reader.py     # Email fetching logic
│   ├── emial_sender.py     # Email sending logic
│   ├── rag_engine.py       # RAG implementation
│   └── spam_or_not.py      # Spam detection
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── email.html             # Web interface
└── readme.md              # This file
```

## 🔧 Configuration

### Environment Variables
```env
# Gmail Configuration
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_char_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# API Configuration
FLASK_PORT=5000
FLASK_DEBUG=True

# AI Model Settings
SPAM_THRESHOLD=0.7
REPLY_MAX_LENGTH=200
```

### Customization
- Modify spam detection threshold in backend settings
- Customize email templates in `templates/` directory
- Adjust UI colors in `tailwind.config.js`

## 🚨 Troubleshooting

### Common Issues

**"Failed to connect to backend"**
- Ensure Flask server is running on port 5000
- Check firewall settings
- Verify CORS configuration

**"Authentication failed"**
- Confirm App Password is correct (16 characters, no spaces)
- Verify 2FA is enabled on Gmail account
- Check email address format

**"No emails found"**
- Ensure you have unread emails in your inbox
- Check Gmail API permissions
- Verify internet connection

### Debug Mode
```bash
# Run in debug mode
FLASK_DEBUG=True python app/app.py
```

## 🔒 Security Notes

- **Never commit** `.env` file to version control
- Use **App Passwords** instead of regular passwords
- Keep dependencies updated for security patches
- Review AI-generated replies before sending

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**KarChikey420**
- GitHub: [@KarChikey420](https://github.com/KarChikey420)
- Project: [Mail_Automator](https://github.com/KarChikey420/Mail_Automator)

## 🙏 Acknowledgments

- Gmail API for email integration
- ChromaDB for vector database
- Flask for web framework
- Python community for ML libraries

---

**⭐ Star this repo if you found it helpful!**
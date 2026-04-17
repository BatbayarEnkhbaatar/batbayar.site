# Batbayar's Portfolio Website

A full-stack Flask portfolio website featuring a voice-to-text API, multilingual support (English/Korean), and responsive mobile design.

**Live Site**: https://batbayar.site

## Features

- 🎙️ **Voice-to-Text API** - Real-time speech recognition using Web Speech API
- 🌍 **Multilingual Support** - English and Korean (한국어) with easy language switcher
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile phones
- 📄 **Professional Resume** - Comprehensive about page with university logos and experience
- 🎯 **Contact Page** - Contact form and social links
- ⚡ **Fast & Scalable** - Built with Flask and Gunicorn
- 🔒 **HTTPS Ready** - SSL/TLS configured with Let's Encrypt

## Project Structure

```
batbayar.site/
├── app.py                 # Flask application & routing
├── translations.py        # English & Korean translations
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── about.html        # Resume/About page
│   ├── projects.html     # Projects showcase
│   ├── contact.html      # Contact form
│   └── voice.html        # Voice-to-Text API demo
├── static/
│   └── photos/           # Images (profile, logos)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/BatbayarEnkhbaatar/batbayar.site.git
cd batbayar.site
```

### 2. Create a Virtual Environment

A **virtual environment** isolates project dependencies and keeps your system Python clean. This is the recommended approach for Python development.

#### What is a Virtual Environment?

A virtual environment is an isolated Python setup that allows you to:
- Install packages without affecting your system Python
- Use different versions of packages in different projects
- Avoid dependency conflicts

#### On Linux/macOS:

```bash
# Create virtual environment named .venv
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

Expected output:
```
(.venv) $ 
```

#### On Windows (Command Prompt):

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

#### On Windows (PowerShell):

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1
```

**Note**: Your terminal prompt will show `(.venv)` prefix when activated.

### 3. Install Dependencies

With the virtual environment **activated**, install required packages:

```bash
pip install -r requirements.txt
```

This will install:
- `Flask` - Web framework
- `Flask-CORS` - Cross-origin request handling
- `Gunicorn` - WSGI HTTP Server (production)

**Verify installation**:
```bash
pip list
```

### 4. Run the Application

#### Development Mode:

```bash
python app.py
```

The app will start at `http://localhost:5000`

#### Production Mode (using Gunicorn):

```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### 5. Visit the Website

Open your browser and go to:
- **Development**: http://localhost:5000
- **Production**: http://localhost:8080
- **Live**: https://batbayar.site

## Usage

### Language Switching

Click the **EN** or **KO** buttons in the top-right corner of the navigation bar to switch between English and Korean. Your preference is saved in your session.

### Voice-to-Text API

1. Navigate to `/voice-api` page
2. Click "🎤 Start Recording"
3. Speak clearly
4. Click "⏹️ Stop Recording"
5. Your speech will be transcribed to text

**Note**: Requires microphone permission in your browser.

## Virtual Environment Management

### Deactivating Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

Your terminal prompt will return to normal.

### Reactivating Later

Every time you open a new terminal session, reactivate the venv:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

## Development Workflow

### Making Changes

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # Linux/macOS
   # or
   .venv\Scripts\activate     # Windows
   ```

2. Make your changes to the code

3. Test locally:
   ```bash
   python app.py
   ```

4. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

### Adding New Dependencies

If you need to install a new package:

```bash
# Make sure venv is activated
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Commit the update
git add requirements.txt
git commit -m "Add new dependency"
git push
```

## Configuration

### Environment Variables

Create a `.env` file (optional):

```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
```

### Domain Configuration

The app is configured for `batbayar.site`. To run locally:

1. The `SERVER_NAME` config is commented out in `app.py` to allow localhost
2. Update if hosting on a different domain

## Troubleshooting

### Virtual Environment Not Activating

**Problem**: `source: command not found` or `.venv not recognized`

**Solution**: 
- Make sure you're in the project directory
- Use the correct command for your OS (see section 2 above)
- Check that `.venv` folder exists in your project

### Virtual Environment Already Activated in Another Terminal

**Problem**: Venv is active in another terminal/IDE

**Solution**: Use a separate terminal for each virtual environment

### Port Already in Use

**Problem**: `Address already in use` error

**Solution**: 
```bash
# Find and kill process using port 5000
lsof -i :5000
kill -9 <PID>

# or use a different port
python app.py --port 5001
```

### Missing Dependencies

**Problem**: `ModuleNotFoundError: No module named 'flask'`

**Solution**: Make sure virtual environment is activated and dependencies are installed:
```bash
source .venv/bin/activate  # Activate
pip install -r requirements.txt  # Install
```

### Wrong Python Version

**Problem**: `ModuleNotFoundError` or version conflicts

**Solution**: 
```bash
# Check Python version
python --version

# If wrong version, use python3 specifically
python3 -m venv .venv
source .venv/bin/activate
```

## Browser Support

- ✅ Chrome/Chromium (recommended for Voice API)
- ✅ Edge
- ✅ Safari
- ✅ Firefox
- ⚠️ Internet Explorer (legacy, not supported)

For **Voice API**, Chrome, Edge, or Safari are required as they support the Web Speech API.

## Deployment

### Using Gunicorn + Nginx

```bash
# Production with 4 workers
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### Using Systemd Service

```bash
sudo systemctl start gunicorn
sudo systemctl restart gunicorn
sudo systemctl status gunicorn
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Activate venv and install dependencies
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Contact

- **Email**: mr.btbmang@gmail.com
- **LinkedIn**: linkedin.com/in/batbayar-enkhbaatar
- **GitHub**: github.com/batbayar-e
- **Website**: https://batbayar.site

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Gunicorn Documentation](https://gunicorn.org/)

---

**Last Updated**: April 17, 2026

from flask import Flask, render_template, request, session, redirect, url_for
from translations import TRANSLATIONS

app = Flask(__name__)

# Domain configuration for batbayar.site
# Note: Comment out SERVER_NAME to allow localhost and other domains during development
# app.config['SERVER_NAME'] = 'batbayar.site'
app.config['PREFERRED_URL_SCHEME'] = 'https'
app.secret_key = 'your-secret-key-for-batbayar-site-2026'

# Try to enable CORS if available
try:
    from flask_cors import CORS
    CORS(app)
except ImportError:
    pass

@app.before_request
def set_language():
    """Set language from URL parameter or session"""
    lang = request.args.get('lang')
    if lang in ['en', 'ko']:
        session['language'] = lang
    elif 'language' not in session:
        session['language'] = 'en'

@app.context_processor
def inject_language():
    """Make language and translations available to all templates"""
    language = session.get('language', 'en')
    return dict(
        language=language,
        trans=TRANSLATIONS.get(language, TRANSLATIONS['en']),
        all_trans=TRANSLATIONS
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/voice-api')
def voice_api():
    return render_template('voice.html')

@app.route('/set-language/<lang>')
def set_language_route(lang):
    """Set language and redirect to referrer or home"""
    if lang in ['en', 'ko']:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    # For production, use a proper WSGI server like gunicorn
    # gunicorn -w 4 -b 0.0.0.0:80 app:app
    app.run(host='0.0.0.0', port=80, debug=False)

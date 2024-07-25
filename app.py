from flask import Flask, request, redirect, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dennisantwi064@gmail.com'
app.config['MAIL_PASSWORD'] = '3944google064'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        sender=email,
        recipients=['dennisantwi064@gmail.com'],  # Your email or a list of emails
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )
    mail.send(msg)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

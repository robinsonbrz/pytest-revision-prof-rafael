import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, smpt_port, from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smpt_port)
    server.starttls()
    server.login(from_addr, 'MyPassword')
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

if __name__ == '__main__':
    send_email('smtp.example.com', 587, 'me@example.com', 'you@example.com', 'Test', 'This is a test')
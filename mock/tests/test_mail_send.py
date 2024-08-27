import unittest
from unittest.mock import patch, ANY

from mail_send import send_email


class TestEmail(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        instance = mock_smtp.return_value
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        from_addr = 'sender@example.com'
        to_addr = 'recipient@example.com'
        subject = 'Test Email'
        body = 'This is a test email.'

        send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body)

        mock_smtp.assert_called_with(smtp_server, smtp_port)

        instance.starttls.assert_called_with()
        instance.login.assert_called_with(from_addr, "MyPassword")
        instance.sendmail.assert_called_with(from_addr, to_addr, ANY)
        instance.quit.assert_called_with()
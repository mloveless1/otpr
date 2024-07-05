import os
from flask import current_app
from flask_mail import Message


class EmailService:
    def __init__(self):
        self.mail = current_app.extensions.get('mail')

    # TODO separate the attachments part into another function
    def send_email(self, email_data, attachments):
        msg = Message(subject=email_data['subject'],
                      sender=email_data['sender'],
                      recipients=email_data['recipients'],
                      body=email_data['body'])

        if attachments is not None:
            for attachment in attachments:
                with open(attachment, 'rb') as file_to_attach:
                    msg.attach(filename=os.path.basename(attachment),
                               content_type='application/pdf',
                               data=file_to_attach.read())

        self.mail.send(msg)

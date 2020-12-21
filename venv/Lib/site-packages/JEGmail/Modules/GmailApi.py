import base64
import mimetypes
import os
import os.path
import pickle
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build


class GmailApi:

    def __init__(self, path):
        self.path = path

    def get_service(self):
        if self.path is None:
            raise Exception
        scopes = [
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/gmail.send',
        ]
        cred = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                cred = pickle.load(token)
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.getcwd() + self.path + '/client_secret.json', scopes)
                cred = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(cred, token)
        service = build('gmail', 'v1', credentials=cred)
        return service

    @staticmethod
    def want_send_message(service, sender, message):
        try:
            sent_message = (service.users().messages().send(userId=sender, body=message)
                            .execute())
            return sent_message
        except errors.HttpError as error:
            raise error

    @staticmethod
    def create_message(sender, to, subject, message_text, use_html=False):
        if use_html:
            message = MIMEText(message_text, 'html')
        else:
            message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        s = message.as_string()
        b = base64.urlsafe_b64encode(s.encode('utf-8'))
        return {'raw': b.decode('utf-8')}

    @staticmethod
    def create_message_with_attachment(sender, to, subject, message_text, file, use_html=False):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        if use_html:
            msg = MIMEText(message_text, 'html')
        else:
            msg = MIMEText(message_text)
        message.attach(msg)
        content_type, encoding = mimetypes.guess_type(file)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.add_header('Content-ID', '<%s>' % filename)
        message.attach(msg)

        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def send_mail_basic(self, email_form="Mail_Address", to="Mail_Address", subject="Test subject", body="Test body",
                        use_html=False):
        if email_form is None or to is None or subject is None or body is None:
            return "Value error"
        else:
            try:
                service = self.get_service()
                message = self.create_message(email_form, to, subject, body, use_html=use_html)
                self.want_send_message(service, email_form, message)
            except Exception as e:
                raise e

    def send_mail_attach(self, email_form="Mail_Address", to="Mail_Address", subject="Test subject", body="Test body",
                         attach_file='File_Path', use_html=False):
        if email_form is None or to is None or subject is None or body is None:
            return "Value error"
        else:
            try:
                service = self.get_service()
                message = self.create_message_with_attachment(email_form, to, subject, body, attach_file,
                                                              use_html=use_html)
                self.want_send_message(service, email_form, message)
            except Exception as e:
                raise e

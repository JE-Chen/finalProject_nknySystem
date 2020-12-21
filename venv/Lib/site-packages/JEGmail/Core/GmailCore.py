import datetime

from JEGmail.Modules.GmailApi import GmailApi
from JEGmail.Modules.SmtpGmail import SmtpGmail
from JEGmail.Token.GmailGetToken import GmailGetToken


class GmailCore:

    def __init__(self, path):
        try:
            self.Gmail_API = GmailApi(path)
            self.Gmail_Get_Token = GmailGetToken()
            self.Smtp_Gmail = SmtpGmail()
        except Exception as error:
            raise error
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')

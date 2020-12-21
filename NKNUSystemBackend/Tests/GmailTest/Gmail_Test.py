import os

import JEGmail

a = JEGmail.Core.GmailCore('/GmailTest')
with open(os.getcwd() + '/Templates/Email_Template1_Picture.html', 'r+') as File:
    content = (File.read())
a.Gmail_API.send_mail_attach("410877027@mail.nknu.edu.tw", "410877027@mail.nknu.edu.tw", "Hello",
                             content, attach_file=os.getcwd() + '/images/firefox_test.png', use_html=True)
File.close()

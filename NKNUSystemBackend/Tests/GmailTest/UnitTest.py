import os
import unittest

import JEGmail


class TestGmail(unittest.TestCase):

    def setUp(self) -> None:
        self.Gmail = JEGmail.Core.GmailCore()

    def test_log(self):
        with open(os.getcwd() + '/Test/Templates/Email_Template1_Picture.html', 'r+') as File:
            content = (File.read())
        self.Gmail.Gmail_API.send_mail_attach("410877027@mail.nknu.edu.tw", "410877027@mail.nknu.edu.tw", "Hello",
                                              content, attach_file=os.getcwd() + '/Test/images/firefox_test.png',
                                              use_html=True)
        File.close()


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestGmail))
    unittest.TextTestRunner(verbosity=2).run(suite)

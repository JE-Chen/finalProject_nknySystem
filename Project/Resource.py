import os

import JECryptography
import JEGmail
import JEVerificationCode
from JEDatabase.Core.SQLiteCore import SQLiteCore
from JELogSystem import LogSystem


class RestfulAPIResource:

    def __init__(self):
        self.SQL = SQLiteCore(db_name=os.getcwd() + '/NKNUSystemBackend/DATABASE/StudentSystemData.sqlite',
                              table_name='StudentSystem')
        self.VerificationCode = JEVerificationCode.GenerateVerificationCode()
        self.LogSystem = LogSystem()
        self.LogSystem.set_board_cast_lv(0)
        self.Hash = JECryptography.Hash()
        self.Gmail = JEGmail.Core.GmailCore('/NKNUSystemBackend/Gmail')


RestfulAPIResource = RestfulAPIResource()

import JEVerificationCode
from JEDatabase.Core.SQLiteCore import SQLiteCore


class RestfulAPIResource:

    def __init__(self):
        self.SQL = SQLiteCore(db_name=r'..\\NKNUSystemBackend/DATABASE/StudentSystemData.sqlite',
                              table_name='StudentSystem')
        self.VerificationCode = JEVerificationCode.GenerateVerificationCode()


RestfulAPIResource = RestfulAPIResource()

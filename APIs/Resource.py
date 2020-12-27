import JEVerificationCode
from JEDatabase.Core.SQLiteCore import SQLiteCore
from JELogSystem import LogSystem


class RestfulAPIResource:

    def __init__(self):
        self.SQL = SQLiteCore(db_name=r'..\\NKNUSystemBackend/DATABASE/StudentSystemData.sqlite',
                              table_name='StudentSystem')
        self.VerificationCode = JEVerificationCode.GenerateVerificationCode()
        self.LogSystem = LogSystem()
        self.LogSystem.set_board_cast_lv(0)


RestfulAPIResource = RestfulAPIResource()

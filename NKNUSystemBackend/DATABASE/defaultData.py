from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'StudentSystemData.sqlite', table_name='StudentSystem')

SQL.table_name = 'Manager'

SQL.insert_into_replace('410877027', 'test_password')

SQL.table_name = 'LessonContent'

SQL.insert_into_replace('A001', '測試課程', '課程內容\n測試課程內容', '109')

SQL.table_name = 'LessonDetail'

SQL.insert_into_replace('A001', '410877027', '課程內容\n測試課程內容', '109')

SQL.close()

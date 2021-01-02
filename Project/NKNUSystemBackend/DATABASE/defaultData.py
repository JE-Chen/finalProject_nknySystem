import JECryptography
from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'StudentSystemData.sqlite', table_name='StudentSystem')

Hash = JECryptography.Hash()

SQL.table_name = 'Account'

SQL.insert_into_replace('410877001', Hash.hash_sha512('test'))
SQL.insert_into_replace('410877002', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877003', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877004', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877005', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877006', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877007', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877008', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877009', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877010', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877011', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877012', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877013', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877014', Hash.hash_sha512('test'))
SQL.insert_into_replace('410877015', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877016', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877017', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877018', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877019', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877020', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877021', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877022', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877023', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877024', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877025', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877026', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877027', Hash.hash_sha512('test'))
SQL.insert_into_replace('410877028', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877029', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877030', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877031', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877032', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877033', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877034', Hash.hash_sha512('12345678'))
SQL.insert_into_replace('410877035', Hash.hash_sha512('12345678'))

SQL.table_name = 'LessonContent'

SQL.insert_into_replace('A001', '測試課程-體育-A', '體育', '109')
SQL.insert_into_replace('A002', '測試課程-英文-A', '英文', '109')
SQL.insert_into_replace('A003', '測試課程-數學-A', '數學', '109')
SQL.insert_into_replace('A004', '測試課程-國文-A', '國文', '109')

SQL.insert_into_replace('B001', '測試課程-體育-B', '體育', '108')
SQL.insert_into_replace('B002', '測試課程-英文-B', '英文', '108')
SQL.insert_into_replace('B003', '測試課程-數學-B', '數學', '108')
SQL.insert_into_replace('B004', '測試課程-國文-B', '國文', '108')

SQL.table_name = 'LessonDetail'

SQL.insert_into_replace('A001', '測試課程-體育-A', '1', 'HCP', '選修')
SQL.insert_into_replace('A002', '測試課程-英文-A', '2', 'HCP', '必修')
SQL.insert_into_replace('A003', '測試課程-數學-A', '3', 'HCP', '必修')
SQL.insert_into_replace('A004', '測試課程-國文-A', '2', 'HCP', '必修')

SQL.insert_into_replace('B001', '測試課程-體育-B', '1', 'HCP', '選修')
SQL.insert_into_replace('B002', '測試課程-英文-B', '2', 'HCP', '必修')
SQL.insert_into_replace('B003', '測試課程-數學-B', '3', 'HCP', '必修')
SQL.insert_into_replace('B004', '測試課程-國文-B', '2', 'HCP', '必修')

SQL.table_name = 'LessonGrade'

SQL.insert_into_replace('A001', '410877027', '60', '109', '老師1')
SQL.insert_into_replace('A002', '410877027', '60', '109', '老師2')
SQL.insert_into_replace('A003', '410877027', '60', '109', '老師3')
SQL.insert_into_replace('A004', '410877027', '60', '109', '老師4')

SQL.insert_into_replace('B001', '410877027', '60', '108', '老師1')
SQL.insert_into_replace('B002', '410877027', '60', '108', '老師2')
SQL.insert_into_replace('B003', '410877027', '60', '108', '老師3')
SQL.insert_into_replace('B004', '410877027', '60', '108', '老師4')

SQL.table_name = 'PersonnelAccess'

SQL.insert_into_replace('410877001', Hash.hash_sha512('Professor'))
SQL.insert_into_replace('410877002', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877003', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877004', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877005', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877006', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877007', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877008', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877009', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877010', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877011', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877012', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877013', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877014', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877015', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877016', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877017', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877018', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877019', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877020', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877021', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877022', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877023', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877024', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877025', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877026', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877027', Hash.hash_sha512('Super'))
SQL.insert_into_replace('410877028', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877029', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877030', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877031', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877032', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877033', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877034', Hash.hash_sha512('Normal'))
SQL.insert_into_replace('410877035', Hash.hash_sha512('Normal'))

SQL.table_name = 'PersonnelDetail'

SQL.insert_into_replace('410877001', '001', '107')
SQL.insert_into_replace('410877002', '002', '107')
SQL.insert_into_replace('410877003', '003', '107')
SQL.insert_into_replace('410877004', '004', '107')
SQL.insert_into_replace('410877005', '005', '107')
SQL.insert_into_replace('410877006', '006', '107')
SQL.insert_into_replace('410877007', '007', '107')
SQL.insert_into_replace('410877008', '008', '107')
SQL.insert_into_replace('410877009', '009', '107')
SQL.insert_into_replace('410877010', '010', '107')

SQL.insert_into_replace('410777011', '011', '106')
SQL.insert_into_replace('410777012', '012', '106')
SQL.insert_into_replace('410777013', '013', '106')
SQL.insert_into_replace('410777014', '014', '106')
SQL.insert_into_replace('410777015', '015', '106')

SQL.insert_into_replace('410877027', 'JE-Chen', '107')

SQL.table_name = 'SemesterLesson'

SQL.insert_into_replace('A001', '410877027', '109')
SQL.insert_into_replace('A002', '410877014', '109')
SQL.insert_into_replace('A003', '410877001', '109')
SQL.insert_into_replace('A004', '410777002', '108')

SQL.insert_into_replace('B001', '410877027', '109')
SQL.insert_into_replace('B002', '410877014', '109')
SQL.insert_into_replace('B003', '410877001', '109')
SQL.insert_into_replace('B004', '410777002', '108')

SQL.select_prefix = "*"

SQL.table_name = 'Account'

SQL.select_form()

SQL.select_where('Password', 'test_password')

Check = SQL.select_account('PersonnelNumber', 'Password', '410877027', Hash.hash_sha512('test'))

# SQL.update('password', 'password', 'test_password', 'new_password')

SQL.select_form()

SQL.table_name = 'LessonContent'

SQL.select_form()

SQL.table_name = 'LessonDetail'

SQL.select_form()

SQL.table_name = 'LessonGrade'

SQL.select_form()

SQL.table_name = 'PersonnelAccess'

SQL.select_form()

SQL.table_name = 'PersonnelDetail'

SQL.select_form()

SQL.table_name = 'SemesterLesson'

SQL.select_form()

SQL.close()

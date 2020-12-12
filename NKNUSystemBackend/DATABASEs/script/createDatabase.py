from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(r'../database/StudentSystemData.sqlite', table_name='StudentSystem')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Account('
    'PersonnelNumber VARCHAR(20) PRIMARY KEY ,'
    'Password VARCHAR(20))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelDetail('
    'PersonnelNumber VARCHAR(20) PRIMARY KEY ,'
    'PersonnelName VARCHAR(20),'
    'EnrollYear VARCHAR(10))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonDetail('
    'LessonCode VARCHAR (10) PRIMARY KEY ,'
    'LessonName VARCHAR (20),'
    'LessonCredit VARCHAR (5),'
    'LessonProfessor VARCHAR (20),'
    'LessonType VARCHAR (3),'
    'Semester VARCHAR (5))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonContent('
    'LessonCode VARCHAR(20) PRIMARY KEY ,'
    'LessonName VARCHAR(20),'
    'LessonContent VARCHAR(3000))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonGrade('
    'LessonCode VARCHAR(20) PRIMARY KEY ,'
    'LessonName VARCHAR(20),'
    'LessonContent VARCHAR(3000))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelAccess1('
    'IdNumber VARCHAR(20) PRIMARY KEY ,'
    'AccessLevelID VARCHAR(10))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelAccess2('
    'AccessLevelID VARCHAR(20) PRIMARY KEY ,'
    'AccessLevel VARCHAR(20))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelAccess3('
    'AccessLevel VARCHAR(20) PRIMARY KEY ,'
    'AccessID VARCHAR(20))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelAccess4('
    'AccessID VARCHAR(20) PRIMARY KEY ,'
    'Access VARCHAR(20))')

SQL.close()

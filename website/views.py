from sqlite3 import IntegrityError
from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from io import TextIOWrapper
from flask_sqlalchemy import SQLAlchemy
from .models import Student
import csv
import psycopg2
from psycopg2.errors import UniqueViolation

views = Blueprint('views', __name__)

conn = psycopg2.connect(database="d1aldo6rvck7l1", user='rpojgsgfhigprq', 
password='3e74d2ed51b8ad75dadd84b7404ac6761f19396439f75c48c4921cf97e4b2b88', host='ec2-52-70-107-254.compute-1.amazonaws.com', port='5432')

conn.autocommit = True
cursor = conn.cursor()

db = SQLAlchemy()

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method =='POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            student = Student(tnumber=row[0], firstname=row[1], middlename=row[2], lastname=row[3], 
            term=row[4], level=row[5], pprogram=row[6], 
            ppname=row[7], pcollege=row[8], 
            pdept=row[9], pdeptdesc=row[10], sprogram=row[11], spname=row[12], scollege=row[13], sdept=row[14], 
            sdeptdesc=row[15], decision=row[16], admit=row[17], saddress1=row[18], saddress2=row[19], city=row[20], state=row[21], 
            zip=row[22], phonearea=row[23], phonenum=row[24], phonenumex=row[25], email=row[26], ualremail=row[27], ethnicity=row[28], sex=row[29], admission=row[30], 
            studenttype=row[31])
            db.session.add(student)
            
            sql2 = '''COPY Student (tnumber, firstname, middlename, lastname, term, level, pprogram, ppname, pcollege, pdept, pdeptdesc, sprogram, spname, scollege, sdept,  sdeptdesc, decision, admit, saddress1, saddress2, city, state, zip, phonearea, phonenum, phonenumex, email, ualremail, ethnicity, sex, admission, studenttype)
                    FROM STDIN WITH
                    CSV HEADER
                    DELIMITER AS ',' '''
            with open ('C:\\Users\\CJ\\Desktop\\Test\\admitted_not_enrolled_test_set.csv', 'rb') as new_file:
                cursor.copy_expert(sql2, new_file, 8000)

        try:
            db.session.commit()

        except psycopg2.IntegrityError: psycopg2.UniqueViolation

        
        flash('File successfully uploaded!', category='success')

        return redirect(url_for('views.home'))
    return render_template("home.html", user=current_user)

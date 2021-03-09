''' This is a automated mail generator module '''
import os
import smtplib
import imghdr
from email.message import EmailMessage


def studentmail(name_of_student, mail_of_student, presursum, pretestsum, postsurtest, posttestsum):
    ''' This function is used to send mail to every students '''
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # contacts = ['YourAddress@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = 'Performance score of Python Advanced'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = mail_of_student

    msg.set_content(f'Dear {name_of_student},\nPlease find growth report Below\nYour Pre survey Score is : {presursum}\nYour Pre Assessment Score is : {pretestsum}\nYour Post Survey Score is : {postsurtest}\nYour Post Assessment Score is : {posttestsum}')
    # def
    with open('Presurvey.png', 'rb') as f:

        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)
    with open('Pretest.png', 'rb') as f:

        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)
    with open('Postsurvey.png', 'rb') as f:

        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)
    with open('Posttest.png', 'rb') as f:

        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('test.scored@gmail.com', 'testscored@123')
        smtp.send_message(msg)


def facultymail(str1, preavg, postavg, high, low, top5, bottom5):
    ''' this function is only used for class instructor'''
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

    msg = EmailMessage()
    msg['Subject'] = 'Report card of your Class'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = str1

    msg.set_content(
        f'Average Score of Pretest is : {preavg}\nAverage Score of posttest is : {postavg}\nHighest score from your class is : {high}\nLowest score from your class is : {low}\nTop 5 Scores fromm your class are : {top5}\nBottom 5 scores from your class are : {bottom5}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('test.scored@gmail.com', 'testscored@123')
        smtp.send_message(msg)

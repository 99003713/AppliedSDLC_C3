''' This is a automated mail generator module '''
import os
import smtplib
import imghdr
from email.message import EmailMessage


def mail1(str1, str2):
    ''' this function we will use for presurvey and postsurvey'''
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # contacts = ['YourAddress@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = f'Review Report of {str2}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = str1

    msg.set_content(f'''This report will show the comparison of pre review and post review
                        and in upcoming mail you can check your Assessment score''')

    with open('chart.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('helloankit13@gmail.com', 'Ankit@7065')
        smtp.send_message(msg)


def mail2(str1, str2, xvalue, yvalue, str3, top5, bottom5):
    ''' this function we will use for pretest and post test'''
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # contacts = ['YourAddress@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = f'Assessment score of {str2}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = str1

    msg.set_content(
        f'''This is your score card.\nYour Pre test score is : {xvalue}
            Your Post test scores is : {yvalue}\nand you are {str3} in Assessment.
            Numbers of bottom 5 students are : {bottom5}
            Numbers of top 5 students are : {top5}
            Please find the growth chart below.''')

    with open('chart.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('helloankit13@gmail.com', 'Ankit@7065')
        smtp.send_message(msg)


def mail3(str1, preavg, postavg, high, low):
    ''' this function is only used for class instructor'''
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # contacts = ['YourAddress@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = 'Report card of your Class'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = str1

    msg.set_content(
        f'''Average Score of Pretest is : {preavg}
        Average Score of posttest is : {postavg}
        Highest score from your class is : {high}
        Lowest score from your class is : {low} ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('helloankit13@gmail.com', 'Ankit@7065')
        smtp.send_message(msg)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

send_mail='shilpasudheer031@gmail.com'
receiver_mail='shilpasudheer2004@gmail.com'

msg=MIMEMultipart()
msg['From']=send_mail
msg['To']=receiver_mail
msg['subject']="subject of the mail:Image"

body='This is the body of the mail'
msg.attach(MIMEText(body,'plain'))
file_name='img.jpg'

attachment=open(file_name,'rb')
p=MIMEBase('application','octect-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('content-Disposition',f'attachment;filename={file_name}')
msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('shilpasudheer031@gmail.com',avtjcxunezffjqqg)
text=msg.as_string()

s.sendmail(send_mail,receiver_mail,text)

s.quit()
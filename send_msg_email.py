import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('shilpasudheer031@gmail.com','baolcxwtskjtiemm')
message='hello python....'
s.sendmail('shilpasudheer031@gmail.com','shilpasudheer2004@gmail.com',message)
s.quit()
li = [recipients_mail_ids]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender's_mail_id, sender's_password)
    message = "Model accuracy passed test"
    s.sendmail(sender's_mail_id, dest, message)
    s.quit()
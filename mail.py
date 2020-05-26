li = [recipients_mail_ids]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender's_mail_id, sender's_password)
    message = "Container successfully launched. Model training!!!"
    s.sendmail(sender's_mail_id, dest, message)
    s.quit()
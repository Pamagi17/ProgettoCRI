from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from importlib_metadata import files

def sendEmail(emailTo, name):
    
    email = 'matteo.albanese@lazio.cri.it'
    password = 'SoccAM1703!'

    sender = email

    msg = MIMEMultipart()
    msg['Subject'] = "Attestato Croce Rossa Italiana"
    msg['From'] = sender
    msg['To'] = emailTo

    html = f"""\
        <html>
            <head></head>
            <body>
                <p>Ciao {name},
                <br>
                <p>Grazie per aver donato, in allegato troverà un attestato di ringraziamento personalizzato.
                <br><br>
                Ci auguriamo di rivederla presto,
                <br>
                Comitato 13-14 di Roma
                </p>
            </body>
        </html>
    """

    message = MIMEText(html, 'html')
    msg.attach(message)

    # open the file to be sent 
    path = "PDF/"
    filename = "attestato.pdf"
    attachment = open(path + filename, "rb")
    
    # instance of MIMEBase and named as p
    att = MIMEBase('application', 'octet-stream')
    
    # To change the payload into encoded form
    att.set_payload((attachment).read())
    
    # encode into base64
    encoders.encode_base64(att)
    
    att.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    msg.attach(att)

    

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(email, password)
        smtpObj.sendmail(sender, emailTo, msg.as_string())
        smtpObj.quit()
        return True
    except Exception:
        return False
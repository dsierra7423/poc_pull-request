import smtplib, ssl
from email.message import EmailMessage


'''
Value Object Class to manage the data that are needed to Connect to Email SMTP.
'''
class Connection:
  def __init__(self, smtp_server, port,sender_email, receiver_email, password  ):
    self.smtp_server = smtp_server
    self.port = port
    self.sender_email = sender_email
    self.receiver_email = receiver_email
    self.password = password

'''
Value Object Class to manage the data that are needed to manage the message to be send .
'''
class Message:
  def __init__(self, subject, message ):
    self.subject = subject
    self.message = message


'''
Method to connect to SMTP Server and send email message.
'''
def send_email(conn, message):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(conn.smtp_server,conn.port)
        server.starttls(context=context) 
        server.login(conn.sender_email, conn.password )
        email = EmailMessage()
        email["From"] =conn.sender_email 
        email["To"] = conn.receiver_email 
        email["Subject"] = message.subject
        email.set_content(message.message, subtype="html")
        server.sendmail(conn.sender_email, conn.receiver_email ,  email.as_string())
        print("From: " + conn.sender_email )
        print("To: " + str(conn.receiver_email))
        print("Subject: " + message.subject)
        print("Body: " )
        print( message.message )
    except Exception as e:
        raise UserWarning("Could not send email.")
    finally:
        server.quit() 
        

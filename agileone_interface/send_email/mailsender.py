import smtplib

# 只有一个sendMail()方法，初始化的时候保存了发送的相关参数，之后就可以用该方法发送其参数msg了。
class MailSender:
    def __init__(self,smtpserver,smtpport,password,from_mail,to_mail,cc_mail=None):
        self.smtpserver = smtpserver
        self.smtpport = smtpport
        self.password = password
        self.from_mail = from_mail
        self.to_mail = to_mail
        self.cc_mail = cc_mail

    def sendMail(self,msg):
        try:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.smtpport)
            smtp.login(self.from_mail, self.password)
            if self.cc_mail == None:
                smtp.sendmail(self.from_mail, self.to_mail, msg.as_string())
            else:
                smtp.sendmail(self.from_mail, self.to_mail+self.cc_mail, msg.as_string())
            print("执行报告发送 successful")
        except(smtplib.SMTPRecipientsRefused):
            print("Recipient refused")
        except(smtplib.SMTPAuthenticationError):
            print("Auth error")
        except(smtplib.SMTPSenderRefused):
            print("Sender refused")
        except(smtplib.SMTPException) as e:
            print(e.message)
        finally:
            smtp.quit()

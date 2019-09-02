import datetime
from email.mime.multipart import MIMEMultipart

import os

from agileone_interface_test.send_email.mailassembler import MailAssembler
from agileone_interface_test.send_email.mailsender import MailSender



def send_email_qq_demo():
    """
    function:demo ，完整的例子，麻雀虽小，五脏俱全
    :return:
    """
    subject = "test report"#主题
    from_name = "agileone项目"#发件人
    from_mail = "578863544@qq.com"#发件人
    to_mail = ["647462724@qq.com","703520848@qq.com"]#收件人
    cc_mail = ["703520848@qq.com"]#抄送
    imgbody = '''
    <h3>hi, the attachment is the test report of this test, please check it in time.</h3>
    <img src="cid:image1"/>
    '''
    file1 = r"..\test\result.html"
    file2 = r"..\test\result.txt"
    imgfile = r"..\test\result.png"

    smtpserver = "smtp.qq.com"
    smtpport = 465
    password = "bamihpoyyumabeai"     # 授权码

    msg = MIMEMultipart()
    assembler = MailAssembler()
    sender = MailSender(smtpserver,smtpport,password,from_mail,to_mail,cc_mail)
    assembler.attachAttributes(msg,subject,from_name,from_mail,to_mail,cc_mail)
    assembler.attachBody(msg,imgbody,"html",imgfile)
    assembler.attachAttachment(msg,file1)
    assembler.attachAttachment(msg,file2)
    sender.sendMail(msg)

def send_email_qq():
    subject = "test report"#主题
    from_name = "agileone项目"#发件人
    from_mail = "578863544@qq.com"#发件人
    to_mail = ["647462724@qq.com","703520848@qq.com"]#收件人
    cc_mail = ["703520848@qq.com"]#抄送
    imgbody = '''
    <h3>anileone用例执行结果报告文件</h3>
    '''
    #获取最后一个文件，根据时间戳
    os.path.dirname(os.getcwd())
    file_dir =os.path.join(os.path.dirname(os.getcwd()),'reports')
    list=os.listdir(file_dir)
    list.sort(key=lambda fn: os.path.getmtime(file_dir+r'\\'+fn) if not os.path.isdir(file_dir+r'\\'+fn) else 0)
    #可以查看获取文件修改时间
    d=datetime.datetime.fromtimestamp(os.path.getmtime(file_dir+r'\\'+list[-1]))
    #待发送文件路径
    send_reports_file = file_dir+r'\\'+list[-1]

    smtpserver = "smtp.qq.com"
    smtpport = 465
    password = "bamihpoyyumabeai"     # 授权码

    msg = MIMEMultipart()
    assembler = MailAssembler()
    sender = MailSender(smtpserver,smtpport,password,from_mail,to_mail,cc_mail)
    assembler.attachAttributes(msg,subject,from_name,from_mail,to_mail,cc_mail)
    assembler.attachBody(msg,imgbody,"html")
    assembler.attachAttachment(msg,send_reports_file)
    sender.sendMail(msg)

if __name__ == "__main__":
    send_email_qq()
import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.qq.com"  # 这里以QQ邮箱为例
mail_port = 465
mail_user = "***********@qq.com"
mail_pass = "****************"  # SMTP授权码
sender = "***********@qq.com"  # 此处是发送者邮箱
receivers = ["***********@163.com", "***********@qq.com"]  # 此处接收者是列表形式，可以填写多个，用逗号分隔
message = MIMEText("此处是正文", "plain", "utf-8")  # 正文
message["From"] = sender
message["To"] = ";".join(receivers)
message["Subject"] = "此处是主题"  # 主题
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败，错误原因：{e}")

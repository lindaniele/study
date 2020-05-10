from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
to_addr = []
while True:
    addr = input('请输入收件人邮箱地址To: ')
    to_addr.append(addr)
    res = input("是否继续添加收件人（输入1继续，输入其它添加完毕）:")
    if res == '1':
        continue
    else:
        break
msg = MIMEText('hi,小课让学习更轻松，好好学习，天天向上，五一劳动节快乐', 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
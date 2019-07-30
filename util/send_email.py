import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    send_user = 'maybezhmn@163.com'
    global email_host
    email_host = 'smtp.163.com'
    global password
    password = 'Yy123456'

    def send_mail(self,user_list,sub,content):
        user = "maybezhmn"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['form'] = user
        message['To'] = ",".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.quit()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num
        #%.2f取小数点后两位
        pass_result = "%.2f%%"%(pass_num/count_num*100)
        fail_result = "%.2f%%"%(fail_num/count_num*100)
        user_list = ["915570474@qq.com","maybezmn@163.com"]
        sub = '接口自动化测试报告'
        content = "此次一共运行接口个数为%s个,通过个数为%s个，失败个数%s个，通过率为%s,失败率%s"%(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)


if __name__ == '__main__':
    sen =SendEmail()
    # user_list = ["915570474@qq.com"]
    # sub = '这个是测试邮件'
    # content = '这是第一份测试邮件'
    sen.send_main([1,2,3,4],[2,3,4,5,6])
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class NoticeUtil():
    
    def __init__(self):
        pass
    
    def send_email(self, data=None):
        title = '회원가입 승인 요청'
        email = 'djangotesthj123@gmail.com'
        message = '회원가입 승인 요청 메일입니다'
        email_content = render_to_string('signup_approve.html', {
            'title' : title,
            'email' : email,
            'message' : message   
        })
        email = EmailMessage(title, email_content, to=['djangotesthj123@gmail.com'])
        email.content_subtype = 'html'
        email.send()
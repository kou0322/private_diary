import os

from django import forms
from django.core.mail import EmailMessage


class BlogInquiryForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = '内容をここに入力してください。'

    def send_email(self):
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            title
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
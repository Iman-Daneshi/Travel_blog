from django.forms import ModelForm
from captcha.fields import CaptchaField
from blog.models import Comment


class CommentForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']
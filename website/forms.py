from captcha.fields import CaptchaField
from website.models import Contact, NewsLetter
from django.forms import ModelForm

class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = NewsLetter
        fields = '__all__'

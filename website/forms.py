from website.models import Contact, NewsLetter
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

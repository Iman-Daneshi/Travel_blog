from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from website.forms import ContactForm, NewsLetterForm

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def contact_view(request):
    if request.method != 'POST':
        form = ContactForm()
    else: 
        form = ContactForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket is submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket is not submitted successfully')
    context = {
        'form': form,
    }
    return render(request, 'website/contact.html', context)


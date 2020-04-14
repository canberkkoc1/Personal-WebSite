from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                form.save()
                messages.success(request, 'We have received your email successfully')
                return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})

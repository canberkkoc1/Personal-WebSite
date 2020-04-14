from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput( # BU BÖLÜMDE CONTACT HTML SAYFASINI HAREKETLİ HALE GETİRDİK CONTACT KISMINDA GÖRÜNECEK NAME VB GİBİ BÖLÜMLERİ OLUŞTURDUK...
                attrs={
                    'placeholder': 'Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Phone'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Message'
                }
            ),
        }

from django import forms
from .models import Portfolio
from .models import Contact

class ItemForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['item_name', 'item_description', 'item_image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']

from django import forms
from core.models.contact import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'telephone', 'message')

    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                                          'class': 'form-control'}))
    name = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={'placeholder': 'Full Name',
                                                                                       'class': 'form-control'}))
    telephone = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'placeholder': 'Phone '
                                                                                                            'Number',
                                                                                             'autocomplete': 'off',
                                                                                             'class': 'form-control'}))

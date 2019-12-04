from django import forms
from django.utils.safestring import mark_safe

class DefaultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(DefaultForm, self).__init__(*args, **kwargs)

class EmailForm(DefaultForm):
    user_email = forms.CharField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="", max_length=100)
    user_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}), label=mark_safe("<br>"), max_length=100)

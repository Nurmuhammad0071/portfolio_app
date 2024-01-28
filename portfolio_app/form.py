from django import forms
from portfolio_app.models import Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['your_name', 'your_email', 'subject', 'message']

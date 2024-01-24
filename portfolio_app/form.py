from django import forms
from portfolio_app.models import Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

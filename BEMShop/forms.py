from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    # name = forms.CharField(label='Your name', max_length=100)

    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})

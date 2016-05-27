from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class NotesForm(forms.Form):
    notes = forms.CharField(label='Any other notes', widget=forms.Textarea)
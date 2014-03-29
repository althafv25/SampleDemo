from django import forms

class DocumentForm(forms.Form):
    docfile=forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'

    )

class SearchForm(forms.Form):
    keyword=forms.CharField(max_length=100)
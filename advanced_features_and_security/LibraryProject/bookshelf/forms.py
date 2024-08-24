from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=600)

    def clean_name(self):
        data = self.cleaned_data['name']
        return data
    
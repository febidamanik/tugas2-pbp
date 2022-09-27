from django import forms

class TaskFrom(forms.Form):
    title = forms.CharField(label="Judul", max_length=150)
    description = forms.CharField(label="Deskripsi", widget=forms.Textarea)
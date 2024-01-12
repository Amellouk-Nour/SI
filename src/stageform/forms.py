from django import forms

class UploadFileForm(forms.Form):
    fileToUpload = forms.FileField()
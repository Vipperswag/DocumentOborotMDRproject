from django import forms

class DocumentUploadForm(forms.Form):
    excel_file = forms.FileField(
        label='Заполненный шаблон Excel',
        help_text='Загрузите заполненный файл по образцу',
        widget=forms.FileInput(attrs={
            'accept': '.xlsx,.xls',
            'class': 'form-control-file'
        })
    )
from django import forms
from django.forms import ModelForm
from .models import Document, Translation#, Task

class DocumentForm(ModelForm):
  class Meta:
    model = Document
    fields = ('dod', 'tod', 'dow', 'title', 'descriptor')
    labels = {
      'dod': 'Date Of Delivery',
      'tod': 'Time Of Day',
      'dow': 'Day Of Week',
      'title': 'Document Title',
      'descriptor': 'Descriptor',
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }
    widgets = {
      # 'dod': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date Of Delivery'}),
      # 'dod': forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
      # 'tod': forms.TextInput(attrs={'class':'form-control'}),
      # 'dow': forms.TextInput(attrs={'class':'form-control'}),
      'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
      'descriptor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descriptor'}),
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }

class TranslationForm(ModelForm):
  class Meta:
    model = Translation
    fields = ('lan', 'tran_title', 'eng_tran', 'descrip', 'blkc', 'subc', 'senc', 'xcrip', 'li', 'pubdate', 'version')
    labels = {
      'lan': 'Language',
      'tran_title': 'Translated Title',
      'eng_tran': 'English Translation',
      'descrip': 'Description',
      'blkc': 'Block Count',
      'subc': 'Sub-block Count',
      'senc': 'Sentence Count',
      'xcrip': 'Transcription',
      'li': 'Lookup Imported',
      'pubdate': 'Publication Date',
      'version': 'Version',
      # 'document': 'Document',
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }
    widgets = {
      'lan': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Language'}),
      'tran_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Translated Title'}),
      'descrip': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
      'blkc': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Block Count'}),
      'subc': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Sub-block Count'}),
      'senc': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Sentence Count'}),
      'xcrip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Transcription'}),
      # 'li': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'Language'}),
      'pubdate': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Publication Date'}),
      'version': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Version'}),
      # 'document': forms.ChoiceField(attrs={'class':'form-control', 'placeholder':'Document'}),
      # 'eng_tran': forms.ChoiceField(attrs={'class':'form-control', 'placeholder':'English Translasdfasdfasdfasdfasdfation'}),
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }

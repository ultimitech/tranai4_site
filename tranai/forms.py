from django import forms
from django.forms import ModelForm
from .models import Document, Translation, Task

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

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ('role', 'active', 'ci', 'place','translation', 'user', 'status', 'ccs', 'ccs_k', 'ccs_m', 'vcs', 'vcs_a', 'vcs_c', 'vcs_t', 'vcs_p', 'ct', 'vt', 'majtes', 'tietes', 'notes')
    labels = {
      'role': 'Role',
      'active': 'Active',
      'ci': 'Content imported',      
      'place': 'Place',
      'translation': 'Translation',
      'user': 'User',
      'status': 'Status',
      'ccs': 'Final Create additions',
      'ccs_k': '- by klearing',
      'ccs_m': '- by modding',
      'vcs': 'Final Vote additions',
      'vcs_a': '- by accepting',
      'vcs_c': '- by creating',
      'vcs_t': '- by topping',
      'vcs_p': '- by picking',
      'ct': 'Final Create time (s)',
      'vt': 'Final Vote time (s)',
      'majtes': 'Final Majority Top Changes',
      'tietes': 'Final Tie Top Changes',
      'notes': 'Notes',
    }
    widgets = {
      # 'role': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Role'}),
      # 'active': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Active'}),
      # 'ci': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Content imported'}),      
      'place': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Place'}),
      # 'translation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Translation'}),
      # 'user': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'User'}),
      # 'status': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Status'}),
      'ccs': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Create additions'}),
      'ccs_k': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by klearing'}),
      'ccs_m': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by modding'}),
      'vcs': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Vote additions'}),
      'vcs_a': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by accepting'}),
      'vcs_c': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by creating'}),
      'vcs_t': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by topping'}),
      'vcs_p': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '- by picking'}),
      'ct': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Create time (s)'}),
      'vt': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Vote time (s)'}),
      'majtes': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Majority Top Changes'}),
      'tietes': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Final Tie Top Changes'}),
      'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Notes'}),
    }

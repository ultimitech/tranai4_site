from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Document, Translation
from .forms import DocumentForm#, TranslationForm, TaskForm

# def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
def home(request):
  name = 'John'
#   month = month.capitalize()
  # conver month from naem to number
#   month_number = list(calendar.month_name).index(month)
#   month_number = int(month_number)
  # 
#   cal = HTMLCalendar().formatmonth(year, month_number)
  # get current year
#   now = datetime.now()
#   current_year = now.year

  return render(request, 'tranai/home.html', {
    'name': name,
    # 'year': year,
    # 'month': month,
    # 'month_number': month_number,
    # 'cal': cal,
    # 'current_year': current_year,
  })

###############################################################################
# Document
###############################################################################

def index_documents(request):
  document_list = Document.objects.all().order_by('title')#sort by date instead of title
  return render(request, 'tranai/index_documents.html', {'document_list': document_list})

def show_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  translations = document.translations
  return render(request, 'tranai/show_document.html', {'document': document, 'translations': translations})
  # return render(request, 'tranai/show_document.html', {'document': document})

def create_document(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST)
    if form.is_valid():
      try:
        document = form.save()
        model = form.instance
        # return redirect('index-documents')
        return redirect(f'/documents/{document.id}/')
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = DocumentForm()
    # print('get')
    return render(request, 'tranai/create_document.html', {'form': form})

###############################################################################
# Translation
###############################################################################

def show_document_translation(request, document_id, translation_id):
  # return redirect('/')
  # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  # return redirect('show')
  document = Document.objects.get(pk=document_id)
  translation = Translation.objects.get(pk=translation_id)
  return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation})
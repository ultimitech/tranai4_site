from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Document, Translation
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

from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Document, Translation, Task, Sentence
from .forms import DocumentForm, TranslationForm, TaskForm, SentenceForm

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  return render(request, 'tranai/home.html', {})

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

def update_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  form = DocumentForm(initial={'dod': document.dod, 'tod': document.tod, 'dow': document.dow, 'title': document.title, 'descriptor': document.descriptor})
  if request.method == 'POST':
    form = DocumentForm(request.POST, instance=document)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Document id=' + document_id + ' updated successfully')
        return redirect(f'/documents/{document_id}/')
      except Exception as e:
        print('Document update failure: ' + e)
        pass
    else:
      print('form is not valid')
  elif request.method == 'GET':
    form = DocumentForm(initial={'dod': document.dod, 'tod': document.tod, 'dow': document.dow, 'descriptor': document.descriptor, 'title': document.title })
    return render(request, 'tranai/update_document.html', {'document': document, 'form': form})

def delete_document(request, document_id):
  document = Document.objects.get(pk=document_id)
  try:
    document.delete()
    print('Document delete success')
  except Exception as e:
    print('Document delete failure: ' + e)
    pass
  return redirect('index-documents')
  # return redirect(f'/documents/')

###############################################################################
# Translation
###############################################################################

def index_all_translations(request):
  translation_list = Translation.objects.all()
  return render(request, 'tranai/index_all_translations.html', {'translation_list': translation_list})

def index_document_translations(request, document_id):
  document = Document.objects.get(pk=document_id)
  translations = document.translations.all
  # return redirect('/')
  return render(request, 'tranai/show_document.html', {'document': document, 'translations': translations})

def show_document_translation(request, document_id, translation_id):
  # return redirect('/')
  # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  # return redirect('show')
  document = Document.objects.get(pk=document_id)
  translation = Translation.objects.get(pk=translation_id)
  tasks = translation.tasks.all
  sentences = translation.sentences.all
  return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation, 'tasks': tasks, 'sentences': sentences})

def create_document_translation(request, document_id):
  if request.method == 'POST':
    form = TranslationForm(request.POST)
    if form.is_valid():
      try:
        # form.save()
        translation = form.save()
        document = Document.objects.get(pk=document_id)
        # translation = Translation.objects.get(pk=translation_id)
        translation = Translation.objects.get(pk=translation.id)
        translation.document_id = document_id
        translation.save()
        # model = form.instance
        # return redirect('index-translations')
        # document
        return render(request, 'tranai/show_document.html', {'document': document})
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = TranslationForm()
    # print('get')
    return render(request, 'tranai/create_document_translation.html', {'form': form})

def update_document_translation(request, document_id, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  document = Document.objects.get(pk=document_id)
  form = TranslationForm(initial={'lan': translation.lan, 'tran_title': translation.tran_title, 'eng_tran': translation.eng_tran, 'descrip': translation.descrip, 'blkc': translation.blkc, 'subc': translation.subc, 'senc': translation.senc, 'xcrip': translation.xcrip, 'li': translation.li, 'pubdate': translation.pubdate, 'version': translation.version })
  if request.method == 'POST':
    form = TranslationForm(request.POST, instance=translation)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Translation id=' + translation_id + ' updated successfully')
        # return redirect(f'/documents/{document_id}/translations/{translation_id}/')
        return redirect(f'/documents/{document_id}/')
        # return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation})
        # return redirect('index-translations')
      except Exception as e:
        # print('Translation update failure: ' + e)
        pass
    else:
      print('form is not valid')  
  elif request.method == 'GET':
    form = TranslationForm(initial={'lan': translation.lan, 'tran_title': translation.tran_title, 'eng_tran': translation.eng_tran, 'descrip': translation.descrip, 'blkc': translation.blkc, 'subc': translation.subc, 'senc': translation.senc, 'xcrip': translation.xcrip, 'li': translation.li, 'pubdate': translation.pubdate, 'version': translation.version })
    return render(request, 'tranai/update_document_translation.html', {'document': document, 'translation': translation, 'form': form})

def delete_document_translation(request, document_id, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  document = Document.objects.get(pk=document_id)
  try:
    translation.delete()
    print('Translation delete success')
  except Exception as e:
    print('Translation delete failure: ' + e)
  # return redirect(f'/documents/{document_id}/translations/')
  return redirect(f'/documents/{document_id}/')

###############################################################################
# Sentence
###############################################################################

# def index_translation_sentences(request, translation_id):
#   translation = Translation.objects.get(pk=translation_id)
#   sentences = translation.sentences.all
#   # return redirect('/')
#   return render(request, 'tranai/show_document_translation.html', {'translation': translation, 'sentences': sentences})

def show_translation_sentence(request, translation_id, sentence_id):
  translation = Translation.objects.get(pk=translation_id)
  sentence = translation.sentences.get(pk=sentence_id)
  return render(request, 'tranai/show_translation_sentence.html', {'translation': translation, 'sentence': sentence})

def create_translation_sentence(request, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  if request.method == 'POST':
    form = SentenceForm(request.POST)
    if form.is_valid():
      try:
        # form.save()
        sentence = form.save()
        # translation = Translation.objects.get(pk=translation_id)
        sentence = Sentence.objects.get(pk=sentence.id)
        sentence.translation_id = translation_id
        sentence.save()
        return render(request, 'tranai/show_document_translation.html', {'translation': translation})
      except:
        pass
  elif request.method == 'GET':
    form = SentenceForm()
    return render(request, 'tranai/create_translation_sentence.html', {'translation': translation, 'form': form})

def update_translation_sentence(request, translation_id, sentence_id):
  sentence = Sentence.objects.get(pk=sentence_id)
  translation = Sentence.objects.get(pk=sentence_id)
  form = SentenceForm(initial={'blk': sentence.blk, 'sub': sentence.sub, 'rsub': sentence.rsub, 'sen': sentence.sen, 'rsen': sentence.rsen, 'typ': sentence.typ, 'tie': sentence.tie })
  if request.method == 'POST':
    form = SentenceForm(request.POST, instance=sentence)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Sentence id=' + sentence_id + ' updated successfully')
        return redirect(f'/translations/{translation_id}/sentences/{sentence_id}')
      except Exception as e:
        # print('Sentence update failure: ' + e)
        pass
    else:
      print('form is not valid')  
  elif request.method == 'GET':
    form = SentenceForm(initial={'blk': sentence.blk, 'sub': sentence.sub, 'rsub': sentence.rsub, 'sen': sentence.sen, 'rsen': sentence.rsen, 'typ': sentence.typ, 'tie': sentence.tie })
    return render(request, 'tranai/update_translation_sentence.html', {'translation': translation, 'sentence': sentence, 'form': form})

def delete_translation_sentence(request, translation_id, sentence_id):
  sentence = Sentence.objects.get(pk=sentence_id)
  translation = Translation.objects.get(pk=translation_id)
  try:
    sentence.delete()
    print('Sentence delete success')
  except Exception as e:
    print('Sentence delete failure: ' + e)
  return redirect(f'/documents/{translation.document.id}/translations/{translation_id}')

###############################################################################
# Task
###############################################################################

def index_tasks(request):
  task_list = Task.objects.all()
  return render(request, 'tranai/index_tasks.html', {'task_list': task_list})

def show_task(request, task_id):
  task = Task.objects.get(pk=task_id)
  return render(request, 'tranai/show_task.html', {'task': task})

def create_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      try:
        task = form.save()
        model = form.instance
        # return redirect('index-documents')
        return redirect(f'/tasks/{task.id}/')
      except:
        pass
    # print('post')
    # return HttpResponse("<a class='dropdown-item' href='#'>Translations</a>")
  elif request.method == 'GET':
    form = TaskForm()
    # print('get')
    return render(request, 'tranai/create_task.html', {'form': form})

def update_task(request, task_id):
  task = Task.objects.get(pk=task_id)
  form = TaskForm(initial={'role': task.role, 'active': task.active, 'ci': task.ci, 'place': task.place, 'translation': task.translation, 'user': task.user, 'status': task.status, 'ccs': task.ccs, 'ccs_k': task.ccs_k, 'ccs_m': task.ccs_m, 'vcs': task.vcs, 'vcs_a': task.vcs_a, 'vcs_c': task.vcs_c, 'vcs_t': task.vcs_t, 'vcs_p': task.vcs_p, 'ct': task.ct, 'vt': task.vt, 'majtes': task.majtes, 'tietes': task.tietes, 'notes': task.notes})
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      try:
        form.save()
        model = form.instance
        print('Task id=' + task_id + ' updated successfully')
        return redirect(f'/tasks/{task_id}/')
      except Exception as e:
        print('Task update failure: ' + e)
        pass
    else:
      print('form is not valid')
  elif request.method == 'GET':
    form = TaskForm(initial={'role': task.role, 'active': task.active, 'ci': task.ci, 'place': task.place, 'translation': task.translation, 'user': task.user, 'status': task.status, 'ccs': task.ccs, 'ccs_k': task.ccs_k, 'ccs_m': task.ccs_m, 'vcs': task.vcs, 'vcs_a': task.vcs_a, 'vcs_c': task.vcs_c, 'vcs_t': task.vcs_t, 'vcs_p': task.vcs_p, 'ct': task.ct, 'vt': task.vt, 'majtes': task.majtes, 'tietes': task.tietes, 'notes': task.notes})
    return render(request, 'tranai/update_task.html', {'task': task, 'form': form})

def delete_task(request, task_id):
  task = Task.objects.get(pk=task_id)
  try:
    task.delete()
    print('Task delete success')
  except Exception as e:
    print('Task delete failure: ' + e)
    pass
  return redirect('index-tasks')
  # return redirect(f'/tasks/')

###############################################################################
# User
###############################################################################
from django.contrib.auth import get_user_model

def index_users(request):
  User = get_user_model()
  users = User.objects.all()
  return render(request, 'tranai/index_users.html', {'users': users})

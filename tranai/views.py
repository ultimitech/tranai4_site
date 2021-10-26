# from django.http import request
from django.http import request
from tranai4_site.settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Addition, Change, Document, Lookup, Translation, Task, Sentence
from .forms import DocumentForm, TranslationForm, TaskForm, SentenceForm
from django.contrib import messages
import re
import json

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  return render(request, 'tranai/home.html', {})

###############################################################################
# Document
###############################################################################

def report_documents_by_dod(request):
  document_list = Document.objects.all().order_by('dod')#sort by date instead of title??
  return render(request, 'tranai/report_documents.html', {'document_list': document_list})

def report_documents_by_title(request):
  document_list = Document.objects.all().order_by('title')#sort by date instead of title??
  return render(request, 'tranai/report_documents.html', {'document_list': document_list})  

def index_documents(request):
  document_list = Document.objects.all().order_by('id')#sort by date instead of title??//was title??
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

def search_documents(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    # documents = Document.objects.filter(title__contains=searched).filter(descriptor__contains=searched)
    documents = Document.objects.filter(title__contains=searched)
    # documents = Document.objects.filter(descriptor__contains=searched)

    return render(request, 'tranai/search_documents.html', {'searched':searched,'documents':documents})
  else:
    return render(request, 'tranai/search_documents.html', {})    

def search_documents2():
  if request.method == 'POST':
    dod = models.DateField('Date Of Delivery')
    tod = models.CharField('Time Of Day', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=TimeOfDay.choices, default=TimeOfDay.NO_TOD, blank=False,)
    dow = models.CharField('Day Of Week', max_length=2, choices=DayOfWeek.choices, default=DayOfWeek.SUNDAY, blank=False,)
    title = models.CharField('Document Title', max_length=64, blank=False,)
    descriptor = models.CharField('Descriptor', max_length=120, blank=False,)
    search_str = json.loads(request.body).get('searchText')

    documents = Document.objects.filter(title__starts_with=search_str, descriptor=request.user)


  pass
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
  lookups = translation.lookups.all
  return render(request, 'tranai/show_document_translation.html', {'document': document, 'translation': translation, 'tasks': tasks, 'sentences': sentences, 'lookups': lookups})

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

# from .forms import UploadFileForm
# def lookup_link(request, document_id, translation_id):
#   if request.method == 'POST':
#     form = UploadFileForm(request.POST, request.FILES)
#     if form.is_valid():
#       handle_uploaded_file(request.FILES['myfile'])
#       # return HttpResponseRedirect('/success/url/')
#       return redirect(f'/documents/{document_id}/translations/{translation_id}')
#   else:
#     form = UploadFileForm()
#   return render(request, 'tranai/upload.html', {'form': form})

# https://stackoverflow.com/questions/50521674/how-to-convert-content-of-inmemoryuploadedfile-to-string
def handle_lookup_file(f, translation_id):
  # print(f.name); print(f.size); print(f)
  translation = Translation.objects.get(pk=translation_id)
  str_text = ''
  for line in f: str_text = str_text + line.decode(); # "str_text" will be of `str` type
  str_split = str_text.split('\n')#; print(str_split)
  num_of_lookups = 0
  for line in str_split:
    if line.strip(): #non-empty after strip
      print(line)
      # get line parts
      line_parts = line.split(' ')
      blk = line_parts[0]
      sub = line_parts[1]
      rsub = line_parts[2]
      # create lookup
      new_lookup = Lookup(blk=blk, sub=sub, rsub=rsub, translation=translation)
      new_lookup.save()
      if new_lookup:
        print(f"new_lookup: {new_lookup.blk} {new_lookup.sub} {new_lookup.rsub}")
      else:
        print(f"ERROR: Could not create lookup {new_lookup.blk} {new_lookup.sub} {new_lookup.rsub}")
        # flash[:danger] = "ERROR: Could not create lookup #{new_lookup.blk} #{new_lookup.sub} #{new_lookup.rsub}"
      new_lookup = None
      num_of_lookups += 1
  # mark as imported
  Translation.objects.filter(id=translation_id).update(li=True)

def import_lookup(request, document_id, translation_id):
  if request.method == 'POST':
    handle_lookup_file(request.FILES['document'], translation_id)
    return redirect(f'/documents/{document_id}/translations/{translation_id}')
  else:
    return render(request, 'tranai/upload.html')

def delete_lookup(request, document_id, translation_id):
  translation = Translation.objects.get(pk=translation_id)
  # determine the lookups to be deleted
  # lookups = translation.lookups
  lookups = Lookup.objects.filter(translation_id=translation_id)
  num_of_lookups = len(lookups)
  print(f"num_of_lookups: {num_of_lookups}")
  if num_of_lookups > 0:
    for lookup in lookups:
      lookup.delete()
    #mark as not imported 
    Translation.objects.filter(id=translation_id).update(li=False)
    # flash[:danger] = "#{num_of_lookups} lookups for this translation deleted"
  else:
    pass
    # flash[:danger] = 'No lookups for this translation deleted'
  return redirect(f'/documents/{document_id}/translations/{translation_id}')

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

  #update E_change
  # @E_edit = Edit.joins(sentence: :translation).where(translations: {id: @sentence.translation.eng_tran_id}, sentences: {rsen: @sentence.rsen}).first
  E_change = Sentence.objects.filter(translation__id=sentence.translation.eng_tran_id, rsen=sentence.rsen)

  return render(request, 'tranai/show_translation_sentence.html', {'translation': translation, 'sentence': sentence, 'E_change': E_change})

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

def import_content_for_validation(request, task_id):
  if request.method == 'POST':
    # prepare file as list of strings
    str_text = ''
    for line in request.FILES['document']: str_text = str_text + line.decode()
    str_split = str_text.split('\n'); #print(str_split[:10])

    # remove title line
    str_split.pop(0)
    rsub_sen_ary = []
    for line in str_split:
      # line = line.strip()
      if line: #non-empty after strip, only non-blank lines
        print(line)
        # 1. test line for valid descriptor
        match = re.search('^[0-9]+\.[0-9]+\.[ncspqkhijv]\s', line)
        if match == None:
          print(f"ERROR: {line}")
          messages.error(request, f"ERROR: Invalid descriptor in line: {line}  (Validation failed. Import aborted.)")
          return redirect(f'/tasks/{task_id}/')
        # 2. test for unique rsub.sen combinations
        # get line parts
        line_parts = line.split(' ', 2) #split by space into 2 parts
        # get signature
        signature = line_parts[0]
        # get signature parts
        signature_parts = signature.split('.')
        rsub = signature_parts[0]
        sen = signature_parts[1]
        rsub_sen = rsub + '.' + sen; #print(f"rsub_sen: XXX{rsub_sen}XXX")
        if rsub_sen in rsub_sen_ary:
          print(f"ERROR: Duplicate rsub.sen combination found in line: {line}  (Validation failed. Import aborted.)")
          messages.error(request, f"ERROR: Duplicate rsub.sen combination found in line: {line}  (Validation failed. Import aborted.)")
          return redirect(f'/tasks/{task_id}/')
        else:
          rsub_sen_ary.append(rsub_sen)
    task = Task.objects.all().get(pk=task_id)
    required_unique_combinations = task.translation.senc #found_unique_combinations = rsub_sen_ary.uniq.length
    found_unique_combinations = len(rsub_sen_ary)
    print(f"Unique rsub.sen combinations required: {required_unique_combinations}")
    print(f"Unique rsub.sen combinations found: {found_unique_combinations}")
    messages.info(request, f"Unique rsub.sen combinations found: #{found_unique_combinations}, Required:  #{required_unique_combinations}.")
    return redirect(f'/tasks/{task_id}/')
  else:
    return render(request, 'tranai/upload.html')
  
# from django.core.exceptions import DoesNotExist
from django.core.exceptions import ObjectDoesNotExist

def import_content(request, task_id):
  task = Task.objects.all().get(pk=task_id)
  # determine the kind of additions to be created
  role = task.role
  if role in ['MT', 'HT', 'NT']:
    kind = 'T'
  elif role in ['TE', 'CE', 'LA']: #both 'C' and 'V' kinds
    messages.error(request, f"Content import for role #{role} is not currently supported")
    return redirect(f'/tasks/{task_id}/')
  elif role in ['EE', 'SE', 'PE']: #'C' kind
    messages.error(request, f"Content import for role {role} is not currently supported")
    return redirect(f'/tasks/{task_id}/')
  elif role in ['EP']:
    kind = 'E'
  else:
    messages.error(request, f"ERROR: Invalid role: {role}")
    return redirect(f'/tasks/{task_id}/')

  if request.method == 'POST':
    # prepare file as list of strings
    str_text = ''
    for line in request.FILES['document']: str_text = str_text + line.decode()
    str_split = str_text.split('\n'); print(str_split[:10])

    str_split.pop(0) #remove title line
    num_of_additions = 0
    for line in str_split:
      # line = line.strip()
      if line: #non-empty after strip, only non-blank lines
        print(line)

        # get line parts
        line_parts = line.split(' ', 1) #split by space into 2 parts

        # get signature
        signature = line_parts[0]

        # get content
        content = line_parts[1].strip() #remove NL at end: No NL here

        # get signature parts
        signature_parts = signature.split('.')
        rsub_num = int(signature_parts[0])
        sen_num = int(signature_parts[1])
        typ_char = signature_parts[2]; #print(f"==========={rsub_num}.{sen_num}============")

        #check if sentence already exists, if not, create
        # existing_sen = Sentence.joins(:translation).where(translations: {id: @assignment.translation_id}, sentences: {rsub: rsub_num, sen: sen_num})
        # try: 
        existing_sen = Sentence.objects.filter(translation__id=task.translation_id, rsub=rsub_num, sen=sen_num)
        if len(existing_sen) == 0:
          print('does not exist............')
          if task.translation.eng_tran is not None: #OTH
            # lookup = task.translation.eng_tran.lookups.where(rsub: rsub_num).first
            lookup = Lookup.objects.filter(translation_id=task.translation.eng_tran.id, rsub=rsub_num)[0]
          else: #ENG
            # lookup = task.translation.lookups.where(rsub: rsub_num).first
            lookup = Lookup.objects.filter(translation_id=task.translation.id, rsub=rsub_num)[0]; print('lookup:',lookup)
          blk_num = lookup.blk #was: blk_num = lookup.blk
          sub_num = lookup.sub #was: sub_num = lookup.sub
          # existing_sen = Sentence.create(rsen: num_of_contributions+1, blk: blk_num, sub: sub_num, rsub: rsub_num, sen: sen_num, typ: typ_char, tie: false, translation: @assignment.translation)
          existing_sen = Sentence.objects.create(rsen=num_of_additions+1, blk=blk_num, sub=sub_num, rsub=rsub_num, sen=sen_num, typ=typ_char, tie=False, translation=task.translation)
        elif len(existing_sen) == 1:
            print('exists............')
            existing_sen = existing_sen[0] #was: existing_sen = existing_sen.first
        else:
            messages.error(request, f"There is more than one sentence with rsub: {rsub_num} and sen: {sen_num}. This is an error!")
            return redirect(f'/tasks/{task_id}/')
        # except ObjectDoesNotExist: #was: if existing_sen.length == 0:if existing_sen.length == 0:

        #create new change
        new_change = Change.objects.create(content=content, hid=False, top='Z', sentence=existing_sen)
        #print(f"--- {new_change.edit_text}"
        if new_change:
          print(f"new_change: {new_change.content}")
        else:
          messages.error(request, f"ERROR: Could not create change with content: {content}, sentence: #{existing_sen.id}.")
          return redirect(f'/tasks/{task_id}/')

        #create addition
        new_addition = Addition.objects.create(kind=kind, effort_in_seconds=0, change=new_change, task=task)
        #print(f"--- #{new_addition.addition_text}")
        if new_addition:
          print(f"new_addition: {new_addition.change.content}")
        else:
          messages.error(request, f"ERROR: Could not create addition with kind: {kind}, change: {new_change.id}.")
          return redirect(f'/tasks/{task_id}/')

        new_edit = None
        new_addition = None
        num_of_additions += 1

    #mark as imported
    Task.objects.filter(id=task_id).update(ci=True) #was: @assignment.update(ci: true)

    messages.error(request, f"{num_of_additions} '{kind}' additions for this task imported")
    return redirect(f'/tasks/{task_id}/')
  else:
    return render(request, 'tranai/upload.html')
  
###############################################################################
# User
###############################################################################
from django.contrib.auth import get_user_model
from crum import get_current_user

def index_users(request):
  User = get_user_model()
  users = User.objects.all()
  return render(request, 'tranai/index_users.html', {'users': users})

def switch_current_task(request, task_id):
  task = Task.objects.get(pk=task_id)
  current_user = get_current_user(); #print(type(current_user))
  User = get_user_model()  
  User.objects.all().filter(id=current_user.id).update(cur_task=task.id)
#   if @user.save
#     flash[:success] = "Assignment was successfully switched"
#     if Assignment.admin_roles.include? @user.cur_assign.role
#       redirect_to assignment_path(assignment)
#     else
#       translation = @user.cur_assign.translation
#       sentence = translation.sentences.where(rsen: @user.cur_assign.place).first
#       redirect_to translation_sentence_path(translation, sentence)
#     end
#   else
#     flash[:danger] = "Assignment was NOT switched"
#     redirect_to :back
#   end
# end
  # return render(request, 'tranai/show_translation_sentence.html', {'translation': task.translation, 'sentence': 1})
  # return render(request, 'tranai/show_translation_sentence.html', {'translation': get_current_user().cur_task.translation, 'sentence': 1})
  # render(request, 'tranai/show_task.html', {'task': task})
  # return render(request, 'tranai/show_task.html', {'task': task})
  # return render(request, 'tranai/show_task.html', {'task': get_current_user().cur_task})
  # return redirect(f'switch_current_task/tasks/{task_id}')
  # return redirect('index-tasks') WORKS!!!!
  #- return redirect('switch-current-task')
  return redirect(f'/tasks/{task.id}/') #WORKS!!!
  #- return redirect(f'translations/{get_current_user().cur_task.translation.id}/sentences/1/')
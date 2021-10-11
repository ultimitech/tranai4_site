from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# abstract model to showcase inheritence and polymorphism
# class Translator(models.Model):
class Translator():
  # created = models.DateTimeField(auto_now_add=True)
  # updated = models.DateTimeField(auto_now=True)
  # email_address = models.CharField(max_length=255)
  # username = models.CharField(max_length=255)
  # created_at = models.DateTimeField(auto_now_add=True)
  # created_at = models.CharField(max_length=255)
  # cur_task = models.CharField(max_length=255)
  # admin = models.BooleanField(max_length=255)
  # is_staff = models.BooleanField(max_length=255)
  # is_active = models.BooleanField(max_length=255)
  # first_name = models.CharField(max_length=255)
  _is_active = models.BooleanField(max_length=255)
  _role = models.CharField(max_length=255)

  def __init__(self, is_active, role):
    self.is_active = is_active
    self.role = role

  def identify(self):
    # print report everything that goes on with that translator
    pass

  class Meta:
    abstract = True
    ordering = ['role']

class HumanTranslator(Translator):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)

  def __init__(self, is_active, role, first_name, last_name):
    super().__init__(is_active=is_active, role=role)
    self.first_name = first_name
    self.last_name = last_name

  
  def identify(self):
      print(f"IDENTITY OF HUMAN TRANSLATOR:\n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}")

  class Meta(Translator.Meta):
    ordering = ['-role']

class MachineTranslator(Translator):
  engine_name = models.CharField(max_length=255)
  engine_version = models.CharField(max_length=255)
  # nerual machine translation engine todma,todgaao, engine
  # e.g bing, yandex, google translate, DeepL,aws translate,self-trained
  # engine
  # engine_version
  # year number of bing etc
  # custom 1.0.0-.1


  def __init__(self, is_active, role, engine_name, engine_version):
    super().__init__(is_active=is_active, role=role)
    self.engine_name = engine_name
    self.engine_version = engine_version

  def identify(self):
      print(f"IDENTITY OF MACHINE TRANSLATOR:\n\tEngine Name: {self.engine_name}\n\tEngine Version: {self.engine_version}")    

  class Meta(Translator.Meta):
    ordering = ['-role']

class Document(models.Model):
  class TimeOfDay(models.TextChoices):
    NO_TOD = 'n', _('No Time Of Day')
    SUNRISE = 's', _('Sunrise')
    BREAKFAST = 'b', _('Breakfast')
    MORNING = 'x', _('Morning')
    AFTERNOON = 'y', _('Afternoon')
    EVENING = 'z', _('Evening')
  class DayOfWeek(models.TextChoices):
    SUNDAY = 'su', _('Sunday')
    MONDAY = 'mo', _('Monday')
    TUESDAY = 'tu', _('Tuesday')
    WEDNESDAY = 'we', _('Wednesday')
    THURSDAY = 'th', _('Thursday')
    FRIDAY = 'fr', _('Friday')
    SATURDAY = 'sa', _('Saturday')
  
  # dod = models.DateTimeField('Date Of Delivery')
  # dod = models.CharField('Date Of Delivery')
  # dod = models.CharField('Date Of Delivery', validators=[RegexValidator(regex='^[0-9]{2}-[0-9]{4}$', message='Format is yy-mmdd', code='nomatch')], max_length=7)
  dod = models.DateField('Date Of Delivery')
  # tod = models.CharField('Time Of Day', max_length=60)
  # tod = models.CharField('Time Of Day', validators=[RegexValidator(regex='^[bsxyz]?$', message='error', code='nomatch')], max_length=1))
  # tod = models.CharField('Time Of Day', max_length=1, choices=TimeOfDay.choices, default=TimeOfDay.NO_TOD, blank=False,)
  tod = models.CharField('Time Of Day', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=TimeOfDay.choices, default=TimeOfDay.NO_TOD, blank=False,)
  dow = models.CharField('Day Of Week', max_length=2, choices=DayOfWeek.choices, default=DayOfWeek.SUNDAY, blank=False,)
  # dow = models.CharField('Day Of Week', max_length=60)
  title = models.CharField('Document Title', max_length=64, blank=False,)
  descriptor = models.CharField('Descriptor', max_length=120, blank=False,)

  def __str__(self):
    # return self.title
    # return f"{self.dod}{self.tod} {self.title}"
    return f"{self.descriptor} {self.title}"

import datetime
class Translation(models.Model):
  class Transcription(models.TextChoices):
    ANDES = 'A', _('Andes')
    MAMALIS = 'M', _('Mamalis')

  lan = models.CharField('Language', max_length=3)
  tran_title = models.CharField('Translated title', max_length=70)
  # descrip = models.CharField('descrip', max_length=300)
  # models.Textarea instead of TextField for descrip////////////////////////////////
  descrip = models.TextField('Description', blank=True, null=True, max_length=500)
  blkc = models.IntegerField('Block count')
  subc = models.IntegerField('Sub-block count')
  senc = models.IntegerField('Sentence count')
  # xcrip = models.CharField('Transcription', max_length=1)
  # forms.Select should also be tried///////////////////////////////////////////////////
  xcrip = models.CharField('Transcription', max_length=1, choices=Transcription.choices, default=Transcription.ANDES, blank=False,)
  li = models.BooleanField('Lookup imported (eng) / translate contributions randomized (oth)')
  pubdate = models.DateField('Publication date', default=datetime.date.today)
  version = models.CharField('Version', max_length=20)
  document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.CASCADE, related_name='translations')
  eng_tran = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,)
  # Translation.Document.title?
  # email = models.EmailField('email')
  # username = models.CharField('username', max_length=300)
  # url = models.URLField('url',max_length=300)
  # admin = 
  # cur_assign_id = 

  def __str__(self):
    return self.tran_title

from django.conf import settings #for accounts app
# from django.contrib.auth.models import User #for members app

class Task(models.Model):
  class Role(models.TextChoices):
    EP = 'EP', _('English Provider (EP)')
    EE = 'EE', _('English Editor (EE)')
    NT = 'NT', _('No Translator (NT)')
    MT = 'MT', _('Machine Translator (MT)')
    HT = 'HT', _('Human Translator (HT)')
    TE = 'TE', _('Translation Editor (TE)')
    SE = 'SE', _('Scripture Editor (SE)')
    PE = 'PE', _('Poetry Editor (PE)')
    CE = 'CE', _('Chief Editor (CE)')
    LA = 'LA', _('Language Administrator (LA)')
  class Status(models.TextChoices):
    ip = 'ip', _('In Process (ip)')
    cd = 'cd', _('Completed (cd)')
    te = 'te', _('TE editing (te)')
    ce = 'ce', _('CE editing (ce)')
    qe = 'qe', _('QE editing (qe)')
    pg = 'pg', _('Publishing (pg)')
    pd = 'pd', _('Published (pd)')
    pr = 'pr', _('Pruned (pr)')
  translation = models.ForeignKey(Translation, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='tasks')
  # user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='tasks') #for members app
  user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='tasks') #for accounts app
  role = models.CharField('Role', max_length=2, validators=[MinLengthValidator(2), MaxLengthValidator(2)], choices=Role.choices, default=Role.TE, blank=False, null=False,)
  active = models.BooleanField('Active', default=False)
  # place = models.IntegerField('Place', default=1, validators=[MinValueValidator(1), MaxValueValidator(translation.senc)], blank=False, null=False,)
  place = models.IntegerField('Place', default=1, validators=[MinValueValidator(1)], blank=False, null=False,)
  ci = models.BooleanField('Content imported', default=False)
  status = models.CharField('Status', max_length=2, validators=[MinLengthValidator(2), MaxLengthValidator(2)], choices=Status.choices, default=Status.ip, blank=False, null=False,)
  ccs = models.IntegerField('Final Create additions', blank=True, null=True,)
  ccs_k = models.IntegerField('- by klearing', blank=True, null=True,)
  ccs_m = models.IntegerField('- by modding', blank=True, null=True,)
  vcs = models.IntegerField('Final Vote additions', blank=True, null=True,)
  vcs_a = models.IntegerField('- by accepting', blank=True, null=True,)
  vcs_c = models.IntegerField('- by creating', blank=True, null=True,)
  vcs_t = models.IntegerField('- by topping', blank=True, null=True,)
  vcs_p = models.IntegerField('- by picking', blank=True, null=True,)
  ct = models.IntegerField('Final Create time (s)', blank=True, null=True,)
  vt = models.IntegerField('Final Vote time (s)', blank=True, null=True,)
  majtes = models.IntegerField('Final Majority Top Changes', blank=True, null=True,)
  tietes = models.IntegerField('Final Tie Top Changes', blank=True, null=True,)
  notes = models.CharField('Notes', max_length=200, blank=True, null=True,)

  def __str__(self):
    return f"[{self.translation.lan} {self.translation.blkc}.{self.translation.subc}.{self.translation.senc}.{self.translation.xcrip}] {self.translation.document.descriptor} {self.translation.document.title} ({self.translation.version}) ({self.role}) {self.user.username} {self.place}"

class Sentence(models.Model):
  class SentenceType(models.TextChoices):
    n = 'n', _('Normal')
    c = 'c', _('Conversation')
    s = 's', _('Scripture')
    p = 'p', _('Poetry first line')
    q = 'q', _('Poetry other lines')
  blk = models.IntegerField('Block', blank=True, null=True,)
  sub = models.IntegerField('Sub-block', blank=True, null=True,)
  rsub = models.IntegerField('Running sub-block', blank=True, null=True,)
  sen = models.IntegerField('Sentence', blank=True, null=True,)
  rsen = models.IntegerField('Running sentence', blank=True, null=True,)
  typ = models.CharField('Sentence type', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=SentenceType.choices, default=SentenceType.n, blank=False, null=False,)
  tie = models.BooleanField('Tie', default=False)
  translation = models.ForeignKey(Translation, blank=False, null=False, on_delete=models.CASCADE, related_name='sentences')

  def __str__(self):
    return f"[{self.blk} {self.sub}.{self.rsub}.{self.sen}.{self.rsen}] {self.typ} {self.translation.tran_title}"

class Lookup(models.Model):
  blk = models.IntegerField('Block', blank=True, null=True,)
  rsub = models.IntegerField('Running sub-block', blank=True, null=True,)
  sub = models.IntegerField('Sub-block', blank=True, null=True,)
  translation = models.ForeignKey(Translation, blank=False, null=False, on_delete=models.CASCADE, related_name='lookups')

class Change(models.Model):
  class TopChangeType(models.TextChoices):
    N = 'N', _('Not top change')
    Z = 'Z', _('Zero vote top change')
    T = 'T', _('Tie top change')
    M = 'M', _('Majority top change')
  content = models.CharField('Content', max_length=1024, validators=[MinLengthValidator(0), MaxLengthValidator(1024)], blank=True, null=True,)
  hid = models.BooleanField('Hidden', default=False)
  top = models.CharField('Top Change', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=TopChangeType.choices, default=TopChangeType.Z, blank=False, null=False,)
  mods = models.IntegerField('Mods', blank=True, null=True,) #to be removed, not used
  sentence = models.ForeignKey(Sentence, blank=False, null=False, on_delete=models.CASCADE, related_name='changes')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Addition(models.Model):
  class Kind(models.TextChoices):
    E = 'E', _('English')
    T = 'T', _('Translate')
    C = 'C', _('Create')
    V = 'V', _('Vote')
  class Base(models.TextChoices):
    # kind C
    k = 'k', _('clearing')
    m = 'm', _('modding')
    # kind V
    a = 'a', _('accepting')
    c = 'c', _('creating')
    t = 't', _('topping')
    p = 'p', _('picking another')
  kind = models.CharField('Kind', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=Kind.choices, blank=False, null=False,)
  effort_in_seconds = models.IntegerField('Effort in seconds', blank=True, null=True,)
  base_change = models.ForeignKey(Change, blank=True, null=True, on_delete=models.CASCADE)
  base = models.CharField('Base', max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)], choices=Base.choices, blank=False, null=False,)
  task = models.ForeignKey(Task, blank=False, null=False, on_delete=models.CASCADE, related_name='additions')
  change = models.ForeignKey(Change, blank=False, null=False, on_delete=models.CASCADE, related_name='additions')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

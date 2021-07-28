from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# from rest_framework import serializers
# from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

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
  pubdate = models.DateField('Publication date')
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

class User(models.Model):
  email = models.EmailField('Email')
  username = models.CharField('Username', max_length=30)
  admin = models.BooleanField('Admin', default=False)
  cur_assign_id = models.IntegerField('current Assignment ID', blank=True, null=True)

  def __str__(self):
    return self.username + ' ' + self.email

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
  user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING, related_name='tasks')
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
    return self.role


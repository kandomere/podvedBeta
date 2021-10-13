from django.db import models
from django.utils.translation import ugettext as _
import datetime
from slugify import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

CONS_FORMAT = ['zip', 'rar', 'RAR', 'ZIP', '7z', '7Z']



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, max_length=500)


class FeedFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Действителен'),
        ('draft', 'Срок вышел'),

    )
    title = models.CharField(_('Покупатель'), max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    data_add = models.DateField(_('Дата начала'), default=datetime.date.today())
    date_end = models.DateField(_('Дата конца'), default=datetime.date.today() + datetime.timedelta(days=365))
    cover = models.FileField(_('Договор'), upload_to='images/', validators=[FileExtensionValidator(['pdf'])])
    more = models.FileField(_('Дополнительные файлы в архиве'), upload_to='images/',null=True, blank=True,
                            validators=[FileExtensionValidator(CONS_FORMAT)])

    # cover = models.ManyToManyField(FeedFile)

    status = models.CharField(_('Статус'), max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               null=True, blank=True, )

    # published = PublishedManager()
    objects = models.Manager()
    active = models.BooleanField(default=True)

    @property
    def days_count(self):
        d = (self.date_end - datetime.date.today())
        return int(d.days)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date_end',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class PostFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

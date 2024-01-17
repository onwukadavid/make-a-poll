from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
import datetime


class SoftDeleteManager(models.Manager):
    def with_deleted(self):
        return super().get_queryset().all()


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()


class Question(SoftDeleteModel, models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    thumbnail   = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    question    = models.CharField(max_length=255)
    pub_date    = models.DateTimeField(verbose_name='Date published', default=timezone.now) # remove default and set auto_now_add=True
    updated_at  = models.DateTimeField(verbose_name='Last update', default=timezone.now) # remove default and set auto_now=True
    status      = models.CharField(max_length=11, default='published')

    def __str__(self):
        return self.title
    
    # Override save method to automatically create slugs
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def save_as_draft(self):
        self.pub_date = None
        self.updated_at = None
        self.status = 'draft'
        self.save()
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    class Meta:
        db_table = 'Questions'

    

# Create choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text     = models.CharField(max_length=255)
    votes    = models.IntegerField()

    class Meta:
        db_table = 'Choices'
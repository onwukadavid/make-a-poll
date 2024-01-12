from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
from  datetime import date


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
    thumbnail   = models.ImageField(upload_to='/uploads/%Y/%m/%d/', null=True, blank=True)
    question    = models.CharField(max_length=255)
    pub_date    = models.DateTimeField(verbose_name='Date published', default=date.today)
    updated_at  = models.DateTimeField(verbose_name='Last update', default=timezone.now)


    def __str__(self):
        return self.title
    

    # Override save method to automatically create slugs
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
# Create choice model
from django.db import models
from django.conf import settings
from django.utils import timezone


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


class Poll(SoftDeleteModel, models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    thumbnail   = models.ImageField(upload_to='/uploads/%Y/%m/%d/', null=True, blank=True)
    question    = models.CharField(max_length=255)
    #choices     = models.

    # Override save method to automativally create slugs

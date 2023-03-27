from django.db import models
from django.urls import reverse

from .services import generate_short_url


class RedirectModel(models.Model):
    target_url = models.URLField()
    short_path = models.CharField(unique=True, max_length=6)

    redirect_counter = models.PositiveBigIntegerField(default=0, editable=False)

    def __str__(self):
        return f"{self.target_url} -> {self.short_path}"

    def save(self, *args, **kwargs):
        if not self.short_path:
            self.short_path = generate_short_url(self._meta.model, 'short_path')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('url_shorter_app:detail', args=(self.short_path, ))

from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

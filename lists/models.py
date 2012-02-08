from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    list = models.ForeignKey(List)

    def __unicode__(self):
        return unicode(self.name)

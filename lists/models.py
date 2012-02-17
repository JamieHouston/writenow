from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class List(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('lists.views.view_list', (),
        {
            'user_name': self.user.username,
            'list_name': self.name
        }
    )


class Item(models.Model):
    name = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    list = models.ForeignKey(List)

    def __unicode__(self):
        return unicode(self.name)

admin.site.register(List)
admin.site.register(Item)

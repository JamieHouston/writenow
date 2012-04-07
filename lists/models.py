from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models import F


class SortableModel(models.Model):
    """
    Abstract model which makes an inherited model's records sortable
    by calling instance.move(position)
    """
    order = models.IntegerField(default=1)

    class Meta:
        abstract = True
        ordering = ['order']

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        """
        makes sure we have a value for order. This must be connected to the
        pre_save event for the inheriting model.
        """
        if not instance.order or instance.order == 0:
            #get last order
            try:
                last = sender.objects.values('order').order_by('-order')[0]
                instance.order = last['order'] + 1
            except IndexError:
                instance.order = 1

    def move(self, to):
        to = int(to)
        orig = self.order
        if to == orig:
            return

        # make sure initial ordering is "clean". Not ideal, but sometimes needed
        list = self.list
        for i, f in enumerate(list.item_set.all()):
            f.order = i + 1
            f.save()

        # make some room
        shift, range = to < orig and (1, (to, orig - 1)) or (-1, (orig + 1, to))
        Item.objects.filter(list__pk=self.list.pk).filter(order__range=range).update(order=F('order') + shift)

        # move it
        self.order = to
        self.save()


class List(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

    def incomplete_items(self):
        return self.item_set.filter(complete=False).count()

    @models.permalink
    def get_absolute_url(self):
        return ('lists.views.view_list', (),
        {
            'user_name': self.user.username,
            'list_name': self.name
        }
    )


class Item(SortableModel):
    name = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    list = models.ForeignKey(List)

    def __unicode__(self):
        return unicode(self.name)

admin.site.register(List)
admin.site.register(Item)

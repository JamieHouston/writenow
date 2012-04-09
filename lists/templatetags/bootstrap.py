from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()


@register.filter
def bootstrap(element, icon=None):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrap/field.html")
        context_dic = {'field': element}
        if icon:
            context_dic["icon"] = icon
        context = Context(context_dic)
    elif element_type == "item":
        template = get_template("bootstrap/item.html")
        context = Context({'item': element})
    elif element_type == "tag":
        template = get_template("bootstrap/tag.html")
        context = Context({'item': element})
    else:
        template = get_template("bootstrap/form.html")
        context = Context({'form': element})

    return template.render(context)


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"

from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}


# @register.inclusion_tag('women/menu.html')
# def show_menu():
#     menu = [{'title': "About", 'url_name': 'about'},
#             {'title': "Add post", 'url_name': 'add_post'},
#             {'title': "Contact", 'url_name': 'contact'},
#             {'title': "Sign in", 'url_name': 'sign_in'}
#             ]
#     return {"menu": menu}

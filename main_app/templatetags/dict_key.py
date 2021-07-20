#from django.template.defaultfilters import register
from django import template

register = template.Library()

@register.simple_tag
def reaction_count(count_dict, review_id, icon):
    if review_id in count_dict and icon in count_dict[review_id]:
        return count_dict[review_id][icon]
    else:
        return 0

# @register.filter(name='dict_key')
# def dict_key(d, args):
#     # k = args[0]
#     # icon = args[1]
#     # if k in d and icon in d[k]:
#     #     return d[k][icon]
#     # else:
#     #     return 0
#     return args
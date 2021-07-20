from django.template.defaultfilters import register


@register.filter(name='dict_key')
def dict_key(d, args):
    # k = args[0]
    # icon = args[1]
    # if k in d and icon in d[k]:
    #     return d[k][icon]
    # else:
    #     return 0
    return args
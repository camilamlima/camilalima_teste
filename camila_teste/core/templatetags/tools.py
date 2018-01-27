from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', "").split(' ')
    if value.errors:
        css_classes.append('is-invalid ')

    if arg not in css_classes:
        css_classes.append(arg)

    css_classes = ' '.join(css_classes)
    return value.as_widget(attrs={'class': css_classes})

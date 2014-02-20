from django import template

register = template.Library()

@register.filter
def form_control(field):
    """Add the form-control CSS class to a field."""
    field.field.widget.attrs.update({'class': 'form-control',})
    return field

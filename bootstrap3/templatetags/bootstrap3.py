from django import forms, template

register = template.Library()

@register.simple_tag
def render_field(field):
    """Render the field."""
    if isinstance(field.field.widget, forms.MultiWidget):
        def format_output(rendered_widgets):
            width = max(12 / len(rendered_widgets), 3)
            cols = ('<div class="col-xs-%d">%s</div>' % (width, w,) for w in rendered_widgets)
            return '<div class="row">%s</div>' % ''.join(cols)
        field.field.widget.format_output = format_output
    if not issubclass(field.field.__class__, forms.FileField):
        field.field.widget.attrs.update({
            'class': 'form-control',
        })
    return field

@register.filter
def widget_type(field):
    """Return the widget type of the field."""
    return field.field.widget.__class__.__name__.lower()

from bs4 import BeautifulSoup
from django import forms, template

register = template.Library()

# Note: BeautifulSoup is required since there is almost no control provided
# for customizing markup for widgets. It gets worse with MultiWidget which
# acts as a container for other widgets, which may all be styled differently.
# Even still, this isn't perfect. But it works for all built-in widgets.

def parse_widget_html(html):
    """Parses widget HTML, adjusting as necessary."""
    soup = BeautifulSoup(html)
    for i in soup.find_all(('input', 'textarea', 'select',)):
        if not 'type' in i.attrs or not i['type'] == 'file':
            i['class'] = 'form-control'
        if i.name == 'select' and 'multiple' in i.attrs:
            i['style'] = 'min-height: 160px;'
    return str(soup)

@register.simple_tag
def render_field(field):
    """Render the field."""
    if isinstance(field.field.widget, forms.MultiWidget):
        def format_output(rendered_widgets):
            width = max(12 / len(rendered_widgets), 3)
            cols = ('<div class="col-xs-%d">%s</div>' % (width, w,) for w in rendered_widgets)
            return '<div class="row">%s</div>' % ''.join(cols)
        field.field.widget.format_output = format_output
    return parse_widget_html(str(field))

@register.filter
def widget_type(field):
    """Return the widget type of the field."""
    return field.field.widget.__class__.__name__.lower()

## Django Bootstrap 3 Templates

More and more Django projects are taking advantage of the excellent [Bootstrap 3](http://getbootstrap.com) framework.
This app provides a set of reusable templates that can be used to create a Bootstrap-based website using Django.

### Features

Here is a brief list of features included in the app:

 * Django contrib apps are displayed with their Bootstrap equivalent
 * Carefully organized templates that are easy to extend
 * Bootstrap theme for the Django admin interface
 * Support for any Bootstrap theme

### Basic Usage

To use this app in your Django project, begin by adding the app to `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'bootstrap3'
    )

Each view in your project should include "title" in the template context dictionary.
For example, the view for your home page might look something like this:

    from django.shortcuts import render

    def home(request):
        """Render the project home page."""
        return render(request, 'home.html', {
            'title': "Home Page",
        })

Each template in your project must then extend "base.html":

    {% extends "base.html" %}

Page content should be placed in the "content" block:

    {% block content %}
        <h2>Home Page</h2>
        ...
    {% endblock %}

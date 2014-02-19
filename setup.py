from distutils.core import setup

setup(name='django-bootstrap3-templates',
      version='0.1',
      description="Django app providing a set of Bootstrap 3 templates for projects",
      author='Nathan Osman',
      author_email='admin@quickmediasolutions.com',
      url='https://github.com/nathan-osman/django-bootstrap3-templates',
      license='MIT',
      packages=['bootstrap3',],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ])

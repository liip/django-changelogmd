=====
Django-ChangelogMD
=====

A Django app to implement rendering of Markdown-based CHANGELOG files

Quick start
-----------

1. Install `django-changelogmd` in your Python environment: `pip install git+https://github.com/danickfort-liip/django-changelogmd.git`
2. Add `django_changelogmd` to your `INSTALLED_APPS`
3. Implement a view based on **ChangelogMDView** or **AdminProtectedChangelogMDView**
4. Make a template and include the changelogmd.html template: `{% include "changelogmd/changelog.html" %}`
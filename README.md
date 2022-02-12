# django-utents
a django app to manage user inside a django project

=======
utents
=======


utents is a Django app to manage users in a website

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "utents" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'utents',
    ]

2. Include the 'utents' URLconf in your project urls.py like this::

    path('', include(('utents.urls', 'utents'), namespace="utents")),

3. Run ``python manage.py migrate`` to create the 'utents' models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create the models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the website
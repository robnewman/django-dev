Introduction
============
You init a Django app like a Ruby-on-Rails app:

> python2.7 manage.py startapp shapes

This creates a directory 'shapes'
with the following components:

__init__.py
models.py
tests.py
views.py

Detail
======
__init__.py tells Django that the current directory
            is a package and where you define any
            package-level initialization code.

You define:

* application models in models.py
* any tests (for TDD) in tests.py
* your application specific views in views.py

Create the database tables
==========================
Once you have defined your models, you sync with the
database, which creates the tables based on your
model definitions:

> python2.7 manage.py syncdb
Creating tables ...
Creating table shapes_shape
Creating table shapes_item_shapes
Creating table shapes_item
Installing custom SQL ...
Installing indexes ...
No fixtures found.

Note the auto-creation of the table that defines
the many-to-many shape relationship to items
(shapes_item_shapes)

Add to the Django Admin interface
=================================
Make sure you create an admin.py in order to expose
your app to the Django admin interface:


from django.contrib import admin
from models import Item, Shape

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Shape, ShapeAdmin)


Restart Apache
==============
Then restart your webserver to see this in the Django
admin interface:

./apache2/bin/restart

Add some items or shapes
========================
Within the Django Admin interface we can now
add/edit/delete an Item and a Shape, and assign
multiple Shape values to an Item.

from django.db import models

class Shape(models.Model):
    """
    Model to define shapes
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        "Shape Name", 
        max_length=100
    )

    class Meta:
        verbose_name = "shape"
        verbose_name_plural = "shapes"
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return ('shape_view', [str(self.id)])

class Item(models.Model):
    """
    Model to define items
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        "Item Name",
        max_length=100
    )
    """
    Django's ManyToManyField relational mapper:
    used here because an Item can have multiple
    shapes. You have to tell the Item model to
    use the Shape model with a ManyToMany mapping.
    This will create a third database table
    defining the relationship.
    """
    shapes = models.ManyToManyField(
        Shape,
        verbose_name="the list of shapes an item can have"
    )

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ('name',)

    def __unicode__(self):
        """
        A Python "magic method" that returns a unicode "representation"
        of any object. This is what Python and Django will use whenever
        a model instance needs to be coerced and displayed as a plain
        string. Most notably, this happens when you display an object
        in an interactive console or in the admin.
        You'll always want to define this method; the default isn't very
        helpful at all.
        """
        return u'%s' % self.name

    def get_absolute_url(self):
        """
        This tells Django how to calculate the URL for an object. Django
        uses this in its admin interface, and any time it needs to figure
        out a URL for an object.
        Any object that has a URL that uniquely identifies it should
        define this method.
        """
        return ('item_view', [str(self.id)])

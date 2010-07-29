from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Tags"

    def __unicode__(self):
        return self.tag

class Author(models.Model):
    name = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

class Quotes(models.Model):
    quote = models.TextField()
    book = models.ForeignKey(Book)
    author = models.ManyToManyField(Author)
    page = models.IntegerField()
    paragraph = models.IntegerField()
    tags = models.ManyToManyField(Tags, null=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __unicode__(self):
        return self.quote


class HierarchyDB(models.Model):
    tag = models.ForeignKey(Tags, related_name="to_tag")
    parent = models.ForeignKey(Tags, null=True, related_name="to_parent")
    left = models.ForeignKey(Tags, null=True, related_name="to_left")

    class Meta:
        db_table = "codea_hierarchy"

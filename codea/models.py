from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Tags"

    def __unicode__(self):
        return self.tag

class Quotes(models.Model):
    quote = models.TextField()
    source = models.CharField(max_length=1024)
    author = models.CharField(max_length=512)
    page = models.IntegerField()
    paragraph = models.IntegerField()
    tags = models.ManyToManyField(Tags, null=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __unicode__(self):
        return "%s, %s page %d" % (self.source, self.author, self.page)


class Hierarchy(models.Model):
    tag = models.ForeignKey(Tags)
    parent = models.ForeignKey(Tags)
    left = models.ForeignKey(Tags)

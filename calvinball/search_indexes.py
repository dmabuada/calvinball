from haystack import indexes
from calvinball.models import Comic


class ComicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Comic

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

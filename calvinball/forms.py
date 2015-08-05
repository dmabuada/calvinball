from haystack.forms import SearchForm


class ComicSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

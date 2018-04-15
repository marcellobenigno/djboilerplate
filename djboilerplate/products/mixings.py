from django.db.models import Q


class SearchMixin(object):
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset

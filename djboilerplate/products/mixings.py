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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_terms'] = self.request.GET.get('q')
        context['total_itens'] = self.get_queryset().count()
        return context

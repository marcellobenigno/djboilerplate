class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        name = self.request.GET.get('name') or ''
        description = self.request.GET.get('description') or ''
        return queryset.filter(
            name__icontains=name,
            description__icontains=description
        )

        return queryset

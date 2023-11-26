from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

class DeChangeList(ChangeList):

    def get_ordering(self, request, queryset):
        """
        Removes the fake field used to show upper
        and lower arrow in changelist table header
        """
        ordering = super().get_ordering(request, queryset)
        if 'cielcio_to_be_removed' in ordering:
            ordering.remove('cielcio_to_be_removed')
        if '-cielcio_to_be_removed' in ordering:
            ordering.remove('-cielcio_to_be_removed')
        return ordering


class DeAdmin(admin.ModelAdmin):

    list_display = ("[...]", "s_d", "gd", "na", "de", "fr" )

    def get_changelist(self, request, **kwargs):
        return DeChangeList

    def get_paginator(self, request, queryset, per_page, orphans=0, allow_empty_first_page=True):
        """
        Intercepts queryset and order by values with 'sorted'
        """

        index_s_p = self.list_display.index('s_p')
        ordering = request.GET.get('o', "99999")

        instances = []
        for nf in ordering.split("."):
            reverse = int(nf) < 0
            if abs(int(nf)) == index_s_p+1:
                instances = sorted(
                    queryset,
                    key=lambda a: (a.s_p is not None if reverse else a.s_p is None, a.s_p),
                    reverse=reverse
                )

        return super().get_paginator(
                request, instances or queryset,
                per_page, orphans, allow_empty_first_page)

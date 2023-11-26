class YourModelAdmin(admin.ModelAdmin):
    ...
    def get_form(self, request, obj=None, **kwargs):
        form = super(YourModelAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields["your_foreign_key_field"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False
        return form

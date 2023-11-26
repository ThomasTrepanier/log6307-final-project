def get_formset(self, request, obj=None, **kwargs):
     formset = super().get_formset(request, obj, **kwargs)
     field = formset.form.base_fields["your_foreign_key_field"]
     field.widget.can_add_related = False
     field.widget.can_change_related = False
     field.widget.can_delete_related = False
     return formset


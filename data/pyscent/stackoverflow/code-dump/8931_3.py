class EditForm(forms.Form):

    # your fields defined here followed by Meta

    class Meta:
        fields = ['title', 'body' ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }

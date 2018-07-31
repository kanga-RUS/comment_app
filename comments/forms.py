from django import forms
from .models import Comment, City

custom_errors = {
    'required': 'Заполните поле'
}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    error_css_class = "error"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        for field in self.fields:
            self.fields[field].error_messages = custom_errors

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['city'].queryset = City.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.feilds['city'].queryset = self.instance.region.city_set.order_by('name')

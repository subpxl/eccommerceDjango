from django import forms

from .models import Address


class AddressForm (forms.ModelForm):
    
    class Meta:
        model=Address
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control border border-dark'
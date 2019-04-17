from django.contrib import admin

# Register your models here.

from .models import Property

from django import forms

class PropertyForm(forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea)
    class Meta:
        model = Property

class Property_Admin(admin.ModelAdmin):
    form = PropertyForm


admin.site.register(Property)

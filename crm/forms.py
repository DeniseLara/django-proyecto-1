from django import forms
from .models import Client, Interaction, Company

class ClientForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, label='Empresa')

    class Meta:
        model = Client
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.company:
            self.fields['company_name'].initial = self.instance.company.name

    def save(self, commit=True):
        client = super().save(commit=False)
        
        company_name = self.cleaned_data['company_name']
        
        company, created = Company.objects.get_or_create(name=company_name)
        
        client.company = company
        
        if commit:
            client.save()
            
        return client

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['client', 'notes']
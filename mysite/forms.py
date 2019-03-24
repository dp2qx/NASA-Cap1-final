from django import forms


class SearchForm(forms.Form):
    Query = forms.CharField(max_length=200, required=False)
    Location = forms.CharField(max_length=200,required=False)
    StartYear = forms.CharField(max_length=4,required=False)
    EndYear = forms.CharField(max_length=4,required=False)


    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        Query = cleaned_data.get('Query')
        Location = cleaned_data.get('Location')
        StartYear = cleaned_data.get('StartYear')
        EndYear = cleaned_data.get('EndYear')

        if not (Query or Location or StartYear or EndYear):
            raise forms.ValidationError('At least one field required')

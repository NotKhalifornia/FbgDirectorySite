from django import forms

# Search form with only one universal search bar
class ListingSearchForm(forms.Form):
    search_terms = forms.CharField( max_length=100, required=False)

# Each searchable field has its own search bar
class IndividualListingSearchForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=250, required=False)
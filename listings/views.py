from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import ListingSearchForm
from listings.models import Listing, Vendor

from django.db.models import Q


# Homepage view #
# Contains search form
#
# Loads with empty form, on submit it reloads empty form and returns database results that matched
# previous query
def listing_search(request):

    result = Vendor.objects.all()  # grab all listings
    form = ListingSearchForm(request.POST)  # Grabs (submitted) form data

    # if recieves a POST request, that means the form has been submitted,
    # and the data must be processed
    if request.method == 'POST':

        # Checks if form is valid, allows you to use form.cleaned_data
        # which checks for malicious submissions, incorrect submissions,
        # incorrectly formatted submissions, ensures requred fields aren't blank, etc.
        if form.is_valid():

            # sets search variable equal to the result set of the search query
            search = Vendor.objects.filter(

                # checks database to see if field contains form.cleaned_data['search_terms']
                # which is the value entered into the form by the user
                # TODO: add support for products 6-10
                Q(company_name__icontains=form.cleaned_data['search_terms']) |
                Q(duns__icontains=form.cleaned_data['search_terms']) |
                Q(prod_1_naic__icontains=form.cleaned_data['search_terms']) |
                Q(prod_2_naic__icontains=form.cleaned_data['search_terms']) |
                Q(prod_3_naic__icontains=form.cleaned_data['search_terms']) |
                Q(prod_4_naic__icontains=form.cleaned_data['search_terms']) |
                Q(prod_5_naic__icontains=form.cleaned_data['search_terms']) |
                Q(product_1__icontains=form.cleaned_data['search_terms']) |
                Q(product_2__icontains=form.cleaned_data['search_terms']) |
                Q(product_3__icontains=form.cleaned_data['search_terms']) |
                Q(product_4__icontains=form.cleaned_data['search_terms']) |
                Q(keyword_1__icontains=form.cleaned_data['search_terms']) |
                Q(keyword_2__icontains=form.cleaned_data['search_terms']) |
                Q(keyword_3__icontains=form.cleaned_data['search_terms']) |
                Q(keyword_4__icontains=form.cleaned_data['search_terms']) |
                Q(keyword_5__icontains=form.cleaned_data['search_terms']) |
                Q(company_url__icontains=form.cleaned_data['search_terms']) |
                Q(gsa_1__icontains=form.cleaned_data['search_terms']) |
                Q(gsa_2__icontains=form.cleaned_data['search_terms']) |
                Q(gsa_3__icontains=form.cleaned_data['search_terms']) |
                Q(gsa_4__icontains=form.cleaned_data['search_terms']) |
                Q(gsa_5__icontains=form.cleaned_data['search_terms']) |
                Q(duns__icontains=form.cleaned_data['search_terms']) |
                Q(cage__icontains=form.cleaned_data['search_terms'])

                # Q(prod_6_naic__icontains=form.cleaned_data['search_terms']) |
                # Q(prod_7_naic__icontains=form.cleaned_data['search_terms']) |
                # Q(prod_8_naic__icontains=form.cleaned_data['search_terms']) |
                # Q(prod_9_naic__icontains=form.cleaned_data['search_terms']) |
                # Q(prod_10_naic__icontains=form.cleaned_data['search_terms']) |
            )

            # dict to be returned in render response
            context = {
                'search': search,
                'form': ListingSearchForm(),
            }
            # returns search_results page with context from above (search results, new blank form)
            return render(request, 'listings/search_results.html', context)
    else:
        # creates empty form
        form = ListingSearchForm()

    # returns empty form on first page load
    return render(request, 'listings/index.html', {'form': form, 'result': result})

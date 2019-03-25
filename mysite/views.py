from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import requests
import urllib
import json



from .forms import SearchForm

def _form_view(request, template_name='bootstrap4.html', form_class=SearchForm):
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            queryString = queryStringBuilder(form)
            #get a JSON response from the NASA site
            response = requests.get(queryString)
            infoFromJson = json.loads(response.text)
            htmlString = htmlStringBuilder(infoFromJson)
            return render(request, "searchResults.html", {"results" : htmlString})
    else:
        form = form_class()
    return render(request, template_name, {'form': form})




def bootstrap4(request):
    return _form_view(request, template_name='bootstrap4.html')



def queryStringBuilder(form):
    # this function builds a query based on the fields that were entered in the search page
    queryString = "https://images-api.nasa.gov/search?"
    if (form.cleaned_data['Query'] != ''):
        queryString += "q=" + urllib.parse.quote_plus(form.cleaned_data['Query']) + "&"
    if (form.cleaned_data['Location'] != ''):
        queryString += "location=" + urllib.parse.quote_plus(form.cleaned_data['Location']) + "&"
    if (form.cleaned_data['StartYear'] != ''):
        queryString += "year_start=" + urllib.parse.quote_plus(form.cleaned_data['StartYear']) + "&"
    if (form.cleaned_data['EndYear'] != ''):
        queryString += "year_end=" + urllib.parse.quote_plus(form.cleaned_data['EndYear']) + "&"
    queryString = queryString + "media_type=image"

    return queryString

def htmlStringBuilder(jsonInfo):
	# Dynamically Build HTML as string
    htmlString = ''



    #the NASA website returns "irregular" json objects. not ever item has the exact same fields filled in, so we need to catch errors
    for i in jsonInfo["collection"]["items"]:


        try:
            thumbnail = i["links"][0]["href"]

            #print("including link to more sizes")
            htmlString += '<a href="' + thumbnail.replace("thumb", "orig") + '">' + '<img class="resize" src="' + thumbnail + '">' + '</a>'

        except:
            pass

        try:
            title = i["data"][0]["title"]
            htmlString += '<p>' + title + '</p>'
        except:
            pass
        try:
            description = i["data"][0]["description_508"]
            if (description != title):
                htmlString += '<p>' + description + '</p>'
        except:
            pass

        try:
            photographer = i["data"][0]["photographer"]
            htmlString += '<p>' + photographer + '</p>'
        except:
            pass
        try:
            secondaryCreator = i["data"][0]["secondary_creator"]
            htmlString += '<p>' + secondaryCreator + '</p>'
        except:
            pass

        try:
            location = i["data"][0]["location"]
            htmlString += '<p>' + location + '</p>'
        except:
            pass

        try:
            center = i["data"][0]["center"]
            htmlString += '<p>' + center + '</p>'
        except:
            pass

        try:
            date = i["data"][0]["date_created"]
            htmlString += '<p>' + date + '</p>'
        except:
            pass
        htmlString += '<br><br>'
    return htmlString

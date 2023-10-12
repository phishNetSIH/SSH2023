from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from api.functions import extract_features, get_prediction


# Create your views here.
import bs4
import requests
from googlesearch import search
from urllib.parse import urlparse
import tldextract

def googled(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
    except:
        return False

    res = []
    for i in search(title, stop=3):
        res.append(str(i))
    print(res)
    real_website = False
    for i in range(3):
        if tldextract.extract(res[i]).domain == tldextract.extract(url).domain:
            real_website = True
        print(tldextract.extract(res[i]).domain)
        print("urldomain: ", tldextract.extract(url).domain)
    return not real_website


def verify_view(request):
    fin = None  # Initialize fin as None
    url = "Enter URL"
    if request.method == 'POST':
        url = request.POST.get("url")
        res = get_prediction(url)

        if res > 90 and not googled(url):
            fin = "The website is possibly unsafe"
        else:
            fin = "The website is confirmed to be safe"
        print(res)

    return render(request, 'verify_template.html', context={"response": fin, "url": url})

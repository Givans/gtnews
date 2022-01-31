from django.shortcuts import render, redirect
import requests


# Create your views here.
def main(request):
    return render(request, 'index.html')


def updates(request):
    api_key = 'your_api_key'
    if request.method == 'POST':
        search = request.POST['search']
    else:
        search = 'kenya'

    url = f'http://api.mediastack.com/v1/news?access_key={api_key}&keywords={search}&countries=ke'
    r = requests.get(url)
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    date = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        date.append(i['published_at'])

    articles = zip(title, description, image, url, date)
    return render(request, 'news.html', {'articles': articles, 'search': search})

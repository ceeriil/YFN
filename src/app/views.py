# from django.shortcuts import render
from django.views.generic import TemplateView
from app.vars import NAME
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = f"{NAME}/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        card_data_list = [
            {
                'image_url': '/static/app/img/enterpreneur.png',
                'alt_text': 'Card 1',
                'card_title': 'Entrepreneurs',
            },
            {
                'image_url': '/static/app/img/writers.png',
                'alt_text': 'Card 2',
                'card_title': 'Writers',
            },
            {
                'image_url': '/static/app/img/creators.png',
                'alt_text': 'Card 3',
                'card_title': 'Content Creators',
            },
            {
                'image_url': '/static/app/img/artists.png',
                'alt_text': 'Card 4',
                'card_title': 'Artists',
            },
        ]

        trending_card_list = [
            {
                'image_url': '/static/app/img/writers2.png',
                'alt_text': 'Card 1',
                'card_title': 'Writers',
                'desc': "Uncover a treasure trove of compelling narratives and fresh perspectives from today's trending writers.",
            },
            {
                'image_url': '/static/app/img/creators2.png',
                'alt_text': 'Card 2',
                'card_title': 'Content Creators',
                'desc': "Dive headfirst into an innovative world of content where creativity knows no bounds, courtesy of the trendsetters in our community.",
            },
            {
                'image_url': '/static/app/img/gossip.png',
                'alt_text': 'Card 3',
                'card_title': 'Gossip',
                'desc': 'Get your daily dose of excitement with the juiciest stories and the most buzz-worthy gossip circulating in the entertainment world.',
            },
            {
                'image_url': '/static/app/img/enterpreneur2.png',
                'alt_text': 'Card 4',
                'card_title': 'Enterpreneur',
                'desc': "Embark on a journey of innovation and inspiration with the stories of entrepreneurs who are reshaping the business landscape and setting trends.",
            },
            {
                'image_url': '/static/app/img/fashion.png',
                'alt_text': 'Card 5',
                'card_title': 'Fashion',
                'desc': "Elevate your style with a glimpse into the latest trends and timeless elegance, crafted by the fashion visionaries of our time.",
            },
            {
                'image_url': '/static/app/img/artists2.png',
                'alt_text': 'Card 6',
                'card_title': 'Artists',
                'desc': 'Step into a realm of creativity and expression, where every stroke and shade tells a story, as created by the trending artists of our vibrant community.',
            },
        ]

        context['card_data_list'] = card_data_list
        context['trending_card_list'] = trending_card_list
        return context



def signup(request):
    return render(request, f"{NAME}/signup.html")

def login(request):
    return render(request, f"{NAME}/login.html")

def blog(request):
    return render(request, f"{NAME}/blog.html")
    
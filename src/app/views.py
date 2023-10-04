# from django.shortcuts import render
from django.views.generic import TemplateView
from app.vars import NAME


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
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
            {
                'image_url': '/static/app/img/creators2.png',
                'alt_text': 'Card 2',
                'card_title': 'Content Creators',
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
            {
                'image_url': '/static/app/img/gossip.png',
                'alt_text': 'Card 3',
                'card_title': 'Gossip',
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
            {
                'image_url': '/static/app/img/enterpreneur2.png',
                'alt_text': 'Card 4',
                'card_title': 'Enterpreneur',
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
            {
                'image_url': '/static/app/img/fashion.png',
                'alt_text': 'Card 5',
                'card_title': 'Fashion',
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
            {
                'image_url': '/static/app/img/artists2.png',
                'alt_text': 'Card 6',
                'card_title': 'Artists',
                'desc': 'tands for “search engine dnjjsjjsjsj optimization.” In simple terms, it means the process of improving',
            },
        ]

        context['card_data_list'] = card_data_list
        context['trending_card_list'] = trending_card_list
        return context

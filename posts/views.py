from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortaños',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
{
        'title': 'Mountain Adventure',
        'user': {
            'name': 'Emily Davis',
            'picture': 'https://picsum.photos/60/60/?random=926'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=758'
    },
    {
        'title': 'Urban Exploration',
        'user': {
            'name': 'John Doe',
            'picture': 'https://picsum.photos/60/60/?random=315'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=589'
    },
    {
        'title': 'Sunset on the Beach',
        'user': {
            'name': 'Alex Johnson',
            'picture': 'https://picsum.photos/60/60/?random=844'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=177'
    },
    {
        'title': 'Urban Exploration',
        'user': {
            'name': 'Jane Smith',
            'picture': 'https://picsum.photos/60/60/?random=76'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=122'
    },
    {
        'title': 'City Lights',
        'user': {
            'name': 'John Doe',
            'picture': 'https://picsum.photos/60/60/?random=315'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=589'
    },
    {
        'title': 'Sunset on the Beach',
        'user': {
            'name': 'Alex Johnson',
            'picture': 'https://picsum.photos/60/60/?random=844'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=177'
    },
    {
        'title': 'Urban Exploration',
        'user': {
            'name': 'Jane Smith',
            'picture': 'https://picsum.photos/60/60/?random=76'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=122'
    },
    {
        'title': 'City Lights',
        'user': {
            'name': 'John Doe',
            'picture': 'https://picsum.photos/60/60/?random=15'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=51'
    },
    {
        'title': 'Mountain Adventure',
        'user': {
            'name': 'Emily Davis',
            'picture': 'https://picsum.photos/60/60/?random=926'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=758'
    },
    {
        'title': 'Urban Exploration',
        'user': {
            'name': 'John Doe',
            'picture': 'https://picsum.photos/60/60/?random=3'
        },
        'timestamp': 'Jan 20th, 2024 - 12:34 hrs',
        'photo': 'https://picsum.photos/800/600/?random=1'
    }
]


def list_posts(request: HttpRequest):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime

posts = [
    {
        'name': 'My Dog.',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
    {
        'name': 'Photoshop',
        'user': 'Maria Rodriguez',
        'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
        'picture': 'https://apollo-virginia.akamaized.net/v1/files/wpp3ygn0meax-CO/image;s=850x0'

    },
    {
        'name': 'Colores',
        'user': 'Juan Romero',
        'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
        'picture': 'https://cdn.britannica.com/70/191970-131-A85628DA/Color-wheel-light-color-spectrum.jpg'

    },
    {
        'name': 'Travel to the moon',
        'user': 'Joseph Rasinger',
        'timestamp': datetime.now().strftime('%b %dth , %Y - %H:%M:%S hrs'),
        'picture': 'https://petapixel.com/assets/uploads/2019/02/details-800x787.jpg'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request: HttpRequest) -> HttpResponse:
    """List existing posts."""
    content = list()
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))

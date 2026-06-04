from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Detail

@api_view(['GET'])
def index(request):
    return Response("Hey Extras!!! This is the ulitmate appreciation page for the Great Explosion Murder God Dynamight!")

@api_view(['GET'])
def general_details(request):
    details = Detail.objects.all()
    data1 = {}
    for d in details:
        data1.update(d.detail)
        
    data2 = {
        'name': 'Bakugo Katsuki',
        'hero_name': 'Great Explosion Murder God Dynamight (Daibaku Kisshin Dainamaito)',
        'quirk': 'Explosion',
        'birthday': 'April 20',
        'birthplace': 'near Shizuoka Prefecture',
        'manga/anime': 'My Hero Academia (Boku no Hiro Akademia)',
        'author/creator': 'Kohei Horikoshi',
        'role': 'Supporting character (Deuteragonist)',
        'occupation': 'Pro Hero',
        'Mother': 'Bakugo Mitsuki',
        'Father': 'Bakugo Masaru',
        'Blood Type': 'A',
        'Japanese VA': 'Nobuhiko Okamoto',
        'English VA': 'Clifford Chapin',
        'fighthing_style': 'close-ranged combat',
        'education': ['Aldera Junior High', 'U.A. High School'],
        'appearane': ['lean muscular build', 'sharp intense bright red eyes', 'short, spiky, ash blond hair with choppy bangs']
    }
    data = {**data1, **data2}
    return Response(data)

from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hey Extras!!! This is the ulitmate appreciation page for the Great Explosion Murder God Dynamight!")

def general_details(request):
    data = {
        'name': 'Bakugo Katsuki',
        'hero_name': 'Great Explosion Murder God Dynamight (Daibaku Kisshin Dainamaito)',
        'quirk': 'Explosion',
        'birthday': 'April 20',
        'birthplace': 'near Shizuoka Prefecture',
        'manga/anime': 'My Hero Academia (Boku no Hiro Akademia)',
        'author/creator': 'Kohei Horikoshi',
        'role': 'Supporting character (Deuteragonist)',
        'Mother': 'Bakugo Mitsuki',
        'Father': 'Bakugo Masaru',
        'Blood Type': 'A',
        'Japanese VA': 'Nobuhiko Okamoto',
        'English VA': 'Clifford Chapin',
    }
    return JsonResponse(data)
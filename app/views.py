from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hey Extras!!! This is the ulitmate appreciation page for the Great Explosion Murder God Dynamight!")


def general_details(self):
    data = {
        'name': 'Bakugo Katsuki',
        'hero_name': 'Great Explosion Murder God Dynamight (Daibaku Kisshin Dainamaito)',
        'birthday': 'April 20',
        'manga/anime': 'My Hero Academia (Boku no Hiro Akademia)',
        'author/creator': 'Kohei Horikoshi',
        'role': 'Supporting character (Deuteragonist)'
    }
    return JsonResponse(data)
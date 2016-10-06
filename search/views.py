from models import Topics, KeyWords
from django.http import HttpResponse
from django.template import loader
from .forms import CascadeForm
import simplejson




def topic_to_keywords(request):
    topic = request.GET.get('topic')
    ret = []
    title = "Search"
    template = loader.get_template('search/search.html')
    form = CascadeForm(request.GET or None)
    context = {"form": form, "title": title}

    if topic:
        for keywords in KeyWords.objects.filter(topic_id=topic):
            ret.append(dict(id=keywords.key_word_id, value=unicode(keywords)))
    if len(ret)!=1:
        ret.insert(0, dict(id='', value='---'))

    return HttpResponse(simplejson.dumps(ret))

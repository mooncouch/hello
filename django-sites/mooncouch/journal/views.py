from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the journal index.")

def detail(request, author_id):
    return HttpResponse("you're looking at author %s." %author_id)

def entry(request, author_id):
    response = "You're looking at the entries of author %s."
    return HttpResponse(response % author_id)

def summary(request, author_id):
    return HttpResponse("You're the summary of author %s." % author_id)

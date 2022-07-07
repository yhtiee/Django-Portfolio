from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request, "db/home.html", {"active" : "homepage"})
# def Virtual(request):
#     return render(request, "db/virtualpage.html")
def Projects(request):
    return render(request, "db/projects.html", {"active" : "projects"})
def Skills(request):
    return render(request, "db/skills.html", {"active" : "skills"})
def Contact(request):
    return render(request, "db/contact.html", {"active" : "contact"})
def Cv(request):
    return render(request, "db/cv.html", {"active" : "cv"})
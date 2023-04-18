from django.shortcuts import render

# Create your views here.
def dashboard(request) :
    data = "dashboard"
    return render(request, "dashboard/dashboard.html", {"key":data})
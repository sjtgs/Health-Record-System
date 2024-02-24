from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="Doctor").exists():
                return redirect("doctor-dashboard")
            elif user.groups.filter(name="Nurse").exists():
                return redirect("nurse-record")
            elif user.groups.filter(name="Patient").exists():
                return redirect("patient-dashboard")
        else:
            # Authentication failed
            return render(
                request,
                "accounts_template/login.html",
                {"error": "Invalid credentials"},
            )
    else:
        return render(request, "accounts_template/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


# Create your views here.

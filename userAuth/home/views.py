from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Password for test user is Sami2580 in admin panel

# Create your views here.
def index(request):
   print(request.user)
   if request.user.is_anonymous:
      return redirect("/login")
   return render(request,'index.html')



def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Trying login with: {username} / {password}")

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login successful!")
            return redirect("/")
        else:
            print("Invalid credentials!")
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# def loginUser(request):
#   if request.method=="POST":
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     print(username, password)

#     #   check if user has enterd correct credentials
#     user = authenticate(username=username, password=password)

#     if user is not None:
#          login(request, user)
#          return redirect("/")
    
#     else:

#         return render(request,'login.html')
#   return render(request,'login.html')

def logoutUser(request):
   logout(request)
   return redirect("/login")

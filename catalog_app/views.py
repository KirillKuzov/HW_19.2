from django.shortcuts import render


def home(request):
    print("Главная страница")
    return render(request, template_name='catalog_app/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog_app/contacts.html')
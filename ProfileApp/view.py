from django.shortcuts import render, HttpResponse, redirect,get_object_or_404

def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")

def home(request):
    return render(request, 'home.html')

def dreamJob(request):
    return render(request, 'dreamJob.html')

def educationalRecord(request):
    return render(request, 'educationalRecord.html')

def hedder(request):
    return render(request, 'hedder.html')

def interests(request):
    return render(request, 'interests.html')

def personalRecord(request):
    return render(request, 'personalRecord.html')

def roleModel(request):
    return render(request, 'roleModel.html')

def showMrData(request):
    name = "นวรัตน์"
    surname = "พิบูลย์"
    gender = "หญิง"
    status = "นักเรียน"
    work = "work"
    context = {'name' : name, 'surname' : name, 'gender' : name, 'status' : name, 'work' : name,}
    return render(request, 'showMyData.html', context)


def product(request):
    name = "นวรัตน์"
    surname = "พิบูลย์"
    nickname = "ฟีฟ่า"
    age = "22 ปี"
    weight = "55"
    height = "165"
    color = "สีฟ้า"
    song = "พบกันใหม่"
    phoneNumber = "0943879402"
    studenCode = "65342310144-4"
    listNameProduct = [
        ['รองเท้า Adidas', 2400, '../../static/images/Adidas.jpg'],
        ["รองเท้า Converse", 1890, '../../static/images/Converse.jpg'],
        ["รองเท้า Nike", 5500, '../../static/images/nikee.jpg'],
        ["รองเท้า Vans", 2400, '../../static/images/Vans.jpg'],
        ["รองเท้า Keds", 1390, '../../static/images/k.webp'],
        ["รองเท้า Keen", 4900, '../../static/images/keen.jpeg'],
        ["รองเท้า Crocs", 3190, '../../static/images/Crocs.jpg'],
        ["กระเป๋า Freitag", 5890, '../../static/images/Freitag.jpg'],
        ["กระเป๋า Gentlewoman", 390, '../../static/images/Gentlewoman.jpg'],
        ["กระเป๋า Coach", 8690, '../../static/images/Coach.jpg']
    ]
    return render(request, 'product.html',
                  {'name': name, 'surname': surname, 'nickname': nickname, 'age': age, 'wight': weight,
                   'height': height,
                   'color': color, 'song': song, 'phoneNumber': phoneNumber, 'studenCode': studenCode,
                   'ListNameProduct': listNameProduct})

listOutProduct = []
from ProfileApp.forms import *
from ProfileApp.models import *



def lisProduct(request):
    context = {'product': listOutProduct}
    return render(request, 'listProduct.html', context)


def inputproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand = form.get('brand')
            price = form.get('price')
            amount = form.get('amount')
            detail = form.get('detail')

            if amount < 3:
                discountlate = 0
            elif amount < 5:
                discountlate = 0.05
            else:
                discountlate = 0.10

            total = price * amount
            discount = total * discountlate
            net = total - discount

            product = Product(id, name, brand, price, amount, detail, total, discount, net)
            listOutProduct.append(product)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, 'inputProduct.html', context)


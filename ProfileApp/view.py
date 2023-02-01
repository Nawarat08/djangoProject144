from django.shortcuts import render, HttpResponse, redirect

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
    name = "นวญลหง"
    surname = "เชื้อสาวะถี"
    nickname = "ชมพู่"
    age = "21 ปี"
    weight = "53"
    height = "153"
    color = "สีน้ำเงิน-ขาว"
    song = "ข้างกาย"
    phoneNumber = "0967691570"
    studenCode = "65342310132-6"
    listNameProduct = [
        ['มาร์คมะขามน้ำผึ้ง', 190, '../../static/images/muse1.png'],
        ["มาร์คมะกู้ด", 199, '../../static/images/muse2.png'],
        ["ยาสีฟันนมแพะ", 199, '../../static/images/pro3.png'],
        ["น้ำหอม JANUA กลิ่น flower shop", 290, '../../static/images/pro4.PNG'],
        ["น้ำหอม JANUA กลิ่น wood sand and fresh vibe", 290, '../../static/images/pro5.PNG'],
        ["น้ำหอม JANUA กลิ่น srxy on the beach", 290, '../../static/images/pro6.PNG'],
        ["น้ำหอม JANUA กลิ่น sweetie picnic", 290, '../../static/images/pro7.PNG'],
        ["กลอสดอกไม้ 01-poppy pink", 199, '../../static/images/pro8.png'],
        ["กลอสดอกไม้ 02-sunny flower", 199, '../../static/images/pro9.png'],
        ["กลอสดอกไม้ 03-ruby tulip", 199, '../../static/images/pro10.png']
    ]
    return render(request, 'product.html',
                  {'name': name, 'surname': surname, 'nickname': nickname, 'age': age, 'wight': weight,
                   'height': height,
                   'color': color, 'song': song, 'phoneNumber': phoneNumber, 'studenCode': studenCode,
                   'ListNameProduct': listNameProduct})


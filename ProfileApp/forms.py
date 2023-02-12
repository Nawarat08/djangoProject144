from django.forms import *


class ProductForm(Form):
    BRANDLIST = [('JANUA', 'JANUA'), ('ลิปจีวาน่า', 'ลิปจีวาน่า')]
    NAMELIST = [
        ('น้ำหอม กลิ่น flower shop', 'น้ำหอม กลิ่น flower shop'),
        ('น้ำหอม กลิ่น wood sand and fresh vibe', 'น้ำหอม กลิ่น wood sand and fresh vibe'),
        ('น้ำหอม กลิ่น srxy on the beach', 'น้ำหอม กลิ่น srxy on the beach'),
        ('น้ำหอม กลิ่น sweetie picnic', 'น้ำหอม กลิ่น sweetie picnic'),
        ('กลอสดอกไม้ 01-poppy pink', 'กลอสดอกไม้ 01-poppy pink'),
        ('กลอสดอกไม้ 02-sunny flower', 'กลอสดอกไม้ 02-sunny flower'),
        ('กลอสดอกไม้ 03-ruby tulip', 'กลอสดอกไม้ 03-ruby tulip'),
    ]
    id = CharField(label="รหัสสินค้า", widget=TextInput(attrs={"size": "15"}))
    name = ChoiceField(label="ชื่อสินค้า", widget=Select, choices=NAMELIST)
    brand = ChoiceField(label="แบรนด์", widget=RadioSelect(attrs={"size": "15"}), choices=BRANDLIST)
    price = FloatField(label="ราคา", widget=TextInput(attrs={"size": "15"}))
    amount = IntegerField(label="จำนวน", widget=TextInput(attrs={"size": "15"}))
    detail = CharField(label="รายละเอียด", widget=Textarea(attrs={"size": "15"}))
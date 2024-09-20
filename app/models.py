from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


STATE_CHOICES = [
    ('Achham', 'Achham'), 
    ('Arghakhanchi', 'Arghakhanchi'), 
    ('Baglung', 'Baglung'), 
    ('Baitadi', 'Baitadi'), 
    ('Bajhang', 'Bajhang'), 
    ('Bajura', 'Bajura'), 
    ('Banke', 'Banke'), 
    ('Bara', 'Bara'), 
    ('Bardiya', 'Bardiya'), 
    ('Bhaktapur', 'Bhaktapur'), 
    ('Bhojpur', 'Bhojpur'), 
    ('Chitwan', 'Chitwan'), 
    ('Dadeldhura', 'Dadeldhura'), 
    ('Dailekh', 'Dailekh'), 
    ('Dang', 'Dang'), 
    ('Darchula', 'Darchula'), 
    ('Dhading', 'Dhading'), 
    ('Dhankuta', 'Dhankuta'), 
    ('Dhanusha', 'Dhanusha'), 
    ('Dolakha', 'Dolakha'), 
    ('Dolpa', 'Dolpa'), 
    ('Doti', 'Doti'), 
    ('Gorkha', 'Gorkha'), 
    ('Gulmi', 'Gulmi'), 
    ('Humla', 'Humla'), 
    ('Ilam', 'Ilam'), 
    ('Jajarkot', 'Jajarkot'), 
    ('Jhapa', 'Jhapa'), 
    ('Jumla', 'Jumla'), 
    ('Kailali', 'Kailali'), 
    ('Kalikot', 'Kalikot'), 
    ('Kanchanpur', 'Kanchanpur'), 
    ('Kapilvastu', 'Kapilvastu'), 
    ('Kaski', 'Kaski'), 
    ('Kathmandu', 'Kathmandu'), 
    ('Kavrepalanchok', 'Kavrepalanchok'), 
    ('Khotang', 'Khotang'), 
    ('Lalitpur', 'Lalitpur'), 
    ('Lamjung', 'Lamjung'), 
    ('Mahottari', 'Mahottari'), 
    ('Makwanpur', 'Makwanpur'), 
    ('Manang', 'Manang'), 
    ('Morang', 'Morang'), 
    ('Mugu', 'Mugu'), 
    ('Mustang', 'Mustang'), 
    ('Myagdi', 'Myagdi'), 
    ('Nawalpur', 'Nawalpur'), 
    ('Nuwakot', 'Nuwakot'), 
    ('Okhaldhunga', 'Okhaldhunga'), 
    ('Palpa', 'Palpa'), 
    ('Panchthar', 'Panchthar'), 
    ('Parasi', 'Parasi'), 
    ('Parbat', 'Parbat'), 
    ('Parsa', 'Parsa'), 
    ('Pyuthan', 'Pyuthan'), 
    ('Ramechhap', 'Ramechhap'), 
    ('Rasuwa', 'Rasuwa'), 
    ('Rautahat', 'Rautahat'), 
    ('Rolpa', 'Rolpa'), 
    ('Rukum East', 'Rukum East'), 
    ('Rukum West', 'Rukum West'), 
    ('Rupandehi', 'Rupandehi'), 
    ('Salyan', 'Salyan'), 
    ('Sankhuwasabha', 'Sankhuwasabha'), 
    ('Saptari', 'Saptari'), 
    ('Sarlahi', 'Sarlahi'), 
    ('Sindhuli', 'Sindhuli'), 
    ('Sindhupalchok', 'Sindhupalchok'), 
    ('Siraha', 'Siraha'), 
    ('Solukhumbu', 'Solukhumbu'), 
    ('Sunsari', 'Sunsari'), 
    ('Surkhet', 'Surkhet'), 
    ('Syangja', 'Syangja'), 
    ('Tanahun', 'Tanahun'), 
    ('Taplejung', 'Taplejung'), 
    ('Terhathum', 'Terhathum'), 
    ('Udayapur', 'Udayapur')
]


class customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    localtiy = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=200)
     
     
def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICE=(
    ("M", "MOBILE"),
    ("L", "LAPTOP")

    
)    
class product(models.Model):
    title  = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    dicount  = models.FloatField()
    description  = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    pruduct_image = models.ImageField(upload_to="productimg")
    
    
def __str__(self):
        return str(self.id)
    
    
status_choice = (
    
    ("Accepted" , "Accepted"),
    ("Packed" , "Packed"),
    ("On The Way" , "On The Way"),
    ("Delivered" , "Delivered"),
    ("Cancle" , "Cancle")
    
)


class orderPlace(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     customer  = models.ForeignKey(customer,on_delete=models.CASCADE)
     product   =  models.ForeignKey(product,on_delete=models.CASCADE)
     quantiy = models.PositiveIntegerField(default=1)
     ordered_date = models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=50, choices=status_choice,default="Pending")
     @property
     def total_cost(self):
        return self.quantiy * self.product.selling_price
     
class card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantiy = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantiy * self.product.selling_price

def __str__(self):
        return str(self.id)
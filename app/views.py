from django.shortcuts import render,redirect
from django.views import View
from .models import(
    customer,product,card,orderPlace
)
from decimal import Decimal
from .forms import CustomerRegister, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class productview(View):
    def get(self,request):
        MOBILE = product.objects.filter(category = "M")
        return render(request, 'app/home.html',{"MOBILE":MOBILE})

class productdetailview(View):
    def get(self,request,pk):
        
        product1 = product.objects.get(pk=pk)
        item_alredy = False
        if request.user.is_authenticated:
            item_alredy = card.objects.filter(Q(product = product1.id) & Q(user = request.user)).exists()
        return render(request, 'app/productdetail.html',{"product1": product1,"item_alredy":item_alredy})
        
@login_required
def add_to_cart(request):
    user = request.user
    Product1_id = request.GET.get('prod_id')
    product1 = product.objects.get(id = Product1_id)
    # print(Product1_id) 
    card(user = user , product= product1).save()
    return redirect('/cart')

@login_required
def showCard(request):
    if  request.user.is_authenticated:
        user = request.user
        card1 = card.objects.filter(user=user)  
        amount = Decimal(0.0)
        shipping_amt = Decimal(100.0)
        total_amount = Decimal(0.0)
        cart_product = [p for p in card.objects.all() if p.user == user]
        
        if cart_product:
            for p in cart_product:
                tempamt = Decimal(p.quantiy * p.product.selling_price)
                amount = amount + tempamt 
                totalamt  = amount+shipping_amt
        
            return render(request, 'app/addtocart.html',{'card1': card1, 'totalamt':totalamt ,"amount":amount } )
        else:
             pass 
        #  for empty
    
def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = card.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantiy+=1
        c.save()
        amount = Decimal(0.0)
        shipping_amt = Decimal(100.0)
        cart_product = [p for p in card.objects.all() if p.user == request.user]
        
        for p in cart_product:
                tempamt = Decimal(p.quantiy * p.product.selling_price)
                amount = amount + tempamt 
        data = {
                "quantiy" : c.quantiy,
                "amount" : amount,
                "totalamt":amount+shipping_amt
                }
        return JsonResponse(data)


  
def  minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = card.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantiy-=1
        c.save()
        amount = Decimal(0.0)
        shipping_amt = Decimal(100.0)
        cart_product = [p for p in card.objects.all() if p.user == request.user]
        
        for p in cart_product:
                tempamt = Decimal(p.quantiy * p.product.selling_price)
                amount = amount + tempamt 
        data = {
                "quantiy" : c.quantiy,
                "amount" : amount,
                 "totalamt":amount+shipping_amt
                }
        return JsonResponse(data)
    
def  remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = card.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.delete()
        amount = Decimal(0.0)
        shipping_amt = Decimal(100.0)
        cart_product = [p for p in card.objects.all() if p.user == request.user]
        
        for p in cart_product:
                tempamt = Decimal(p.quantiy * p.product.selling_price)
                amount = amount + tempamt 
        data = {
                "amount" : amount,
                 "totalamt":amount+shipping_amt
                }
        return JsonResponse(data)
    
    
def buy_now(request):
 return render(request, 'app/buynow.html')

@method_decorator(login_required, name='dispatch')
class profileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html' ,{"form":form, 'active':'btn-primary'})
    def post(self,request):
        form =  CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            localtiy = form.cleaned_data['localtiy']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = customer(user = usr, name=name,localtiy=localtiy,city=city,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,"congratutions!! Profile Updated Successfully")
        return render(request, 'app/profile.html',{"form":form,'active':'btn-primary'})
    
@login_required
def address(request):
 add = customer.objects.filter(user= request.user) 
 return render(request, 'app/address.html',{"add":add , 'active':'btn-primary'})

@login_required
def orders(request):
 op = orderPlace.objects.filter(user = request.user)
 return render(request, 'app/orders.html',{'order':op})


def mobile(request, data=None):
    if data == None:
        mobiles = product.objects.filter(category = "M")
    elif data == "onePlus" or data == "samsung":
         mobiles = product.objects.filter(category = "M").filter(brand = data)
    elif data == 'below':
         mobiles = product.objects.filter(category = "M").filter(selling_price__lt = 10000)
    elif data == 'above':
         mobiles = product.objects.filter(category = "M").filter(selling_price__gt = 10000)
    return render(request, 'app/mobile.html',{"mobiles":mobiles})

# def login(request):
#  return render(request, 'app/login.html')



class customerregisterview(View):
    def get(self,request):
        form = CustomerRegister()
        return render(request, 'app/customerregistration.html',{"form":form})
    
    def post(self,request):
        form =  CustomerRegister(request.POST)
        if form.is_valid():
            messages.success(request,"congratutions!! Registered Successfully")
            form.save()
        return render(request, 'app/customerregistration.html',{"form":form})

def payment_done(request):
    user =request.user
    custid = request.GET.get("custid")
    Customer = customer.objects.get(id=custid)
    card1 = card.objects.filter(user=user)
    for c in card1:
        orderPlace(user=user,customer = Customer,product=c.product, quantiy = c.quantiy).save()
        c.delete()
    return redirect("orders")
           
    
@login_required
def checkout(request):
    user = request.user
    add = customer.objects.filter(user=user)
    cart_item = card.objects.filter(user=user)
    amount = Decimal(0.0)
    shipping_amt = Decimal(100.0)
    cart_product = [p for p in card.objects.all() if p.user == request.user]
    if cart_product:
     for p in cart_product:
                tempamt = Decimal(p.quantiy * p.product.selling_price)
                amount = amount + tempamt
     totalamt = amount+shipping_amt
    return render(request, 'app/checkout.html',{"add":add,"totalamt": totalamt,"cart_item":cart_item})


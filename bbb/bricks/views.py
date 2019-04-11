from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

import sys

from .models import Property,User



class IndexView(generic.ListView):
	"""docstring for IndexView."""

	template_name = "properties.html"
	property_list = Property.objects.order_by('-pub_date')
	model =  Property



# Create your views here.

def index(request):

	property_list = Property.objects.order_by('-pub_date')[:5]
	output = ', '.join([l.title for l in property_list])
	return render(request, 'index.html')


def registertoo(request):
	return render(request, 'registertoo.html')

def registerthree(request):
	return render(request, 'registerthree.html')

def kyc(request):
	return render(request, 'kyc.html')
def properties(request):
	property_list = Property.objects.order_by('-pub_date')[:5]
	output = ', '.join([l.title for l in property_list])

	context = {
		'property_list': property_list
	}
	return render(request, 'properties.html',context)



def login(request):
	return render(request, "login.html")

	# return HttpResponse("You're in the login page")


def home(request):
	return render(request, "home")

	# return HttpResponse("DASHBOARD Number of Bs, Current price, Current Value Held, Average Price Held rows of prices and then 3 cards with pie charts with national average and london average and the target")


def purchase(request):
	return HttpResponse("Amount and Units is it a gift, name of the recipient,email of the recipient, account number, would you like to lock the gift until the recipient reaches a certain age")


def logintoo(request):
	return render(request, "logintoo.html")


def sell(request):
	return render(request,"sell.html")

def buy(request):
	return render(request,"buy.html")
def gift2(request):
	return render(request,"gift2.html")
	
def success(request):
	return render(request,'success.html')

def convert(request):

	return HttpResponse( "\(warning of  at least 4 weeks notice) Date of Conversion, Amount to convert, Address to be acquired postcode lookup (GOOGLE PLACS) Solicitor Name, Email and Telephone, Total acquisition Price, Mortgage Details ")

def charts(request):
	return render(request, "charts.html")

def dashboard(request):
	return render(request, "dashboard.html")

def payment(request):

	return HttpResponse("Card Name , Card Number, Expiry, CCV and Billing Address")


def receiving_bank(request):
	return HttpResponse("Account Name and Account Number Bank and Sort Code")


def registration(request):
	u = User()

	try:
		u.first_name = request.POST['first_name']
		u.last_name = request.POST['last_name']
		u.postcode = request.POST['postcode']
		u.email = request.POST['email']
		u.phone_number = request.POST['phone_number']

		u.save()
		print(f'{u}')
		return render(request,'registration.html',{'success': "Congratulations you signed up!",})


	except:
		print("something is wrong!!! ")
		return render(request,'registration.html',{'error_message' : "Something went wrong  try again! ",})


def property(request,property_id):
	try:
		property = Property.objects.get(pk=property_id)
	except Property.DoesNotExist:
		raise Http404(" Property does not exist!! :( ")



	#property = get_object_or_404(Property,property_id)
	print(property)
	return render(request,'property.html', {'property': property})

def team(request):
	return render(request, 'team.html')
def structure(request):
	return render(request, "structure.html")

	# return HttpResponse("Org  structure")


def prospectus(request):
	return render(request, "prospectus.html")

def faq(request):
	return render(request, "faq.html")

	# return HttpResponse("List of Faq rows with drop down answers")


def settings(request):
	return render(request, "settings.html")

	# return HttpResponse("Edit name surname, email address, password, target saving amount " )


def regular_saving_scheme(request):
	return render(request, "savings.html")

	# return HttpResponse("Account Name, Bank Account, Sort Code, Savings Amount Token Amount, Pause Saving Scheme, Stop Saving Scheme")

def terms_and_conditions(request):
	return render(request, "tandc.html")

	# return HttpResponse("TnC")

def privacy_policy(request):
	return render(request, "privacy.html")

	# return HttpResponse("Privacy policy set out here")


def legal(request):
	return render(request, "legal.html")

	# return HttpResponse(" Legal information ")

def about(request):
	return render(request, "about.html")

	# return HttpResponse(" About page")



def gift(request):
	return render(request, "gift.html")

	# return HttpResponse(" generates an email or notification in the app on the dashboard, youve been sent a gift of .. ")


def notices(request):
	return render(request, "notices.html")

	# return HttpResponse(" Put notices of changes or gifts received or sent opened and auctioned")

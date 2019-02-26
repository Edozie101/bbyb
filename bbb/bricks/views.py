from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("You're in the properties index")



def properties(request):
	return HttpResponse("You're in the properties get page")



def login(request):
	return HttpResponse("You're in the login page")


def registration(request):
	return HttpResponse("Registration page")

def home(request):
	return HttpResponse("DASHBOARD Number of Bs, Current price, Current Value Held, Average Price Held rows of prices and then 3 cards with pie charts with national average and london average and the target")


def purchase(request):
	return HttpResponse("Amount and Units is it a gift, name of the recipient,email of the recipient, account number, would you like to lock the gift until the recipient reaches a certain age")

	


def sell(request):
	return HttpResponse("Amount and Units ")



def convert(request):

	return HttpResponse( "\(warning of  at least 4 weeks notice) Date of Conversion, Amount to convert, Address to be acquired postcode lookup (GOOGLE PLACS) Solicitor Name, Email and Telephone, Total acquisition Price, Mortgage Details ") 
	



def payment(request):

	return HttpResponse("Card Name , Card Number, Expiry, CCV and Billing Address")


def receiving_bank(request): 
	return HttpResponse("Account Name and Account Number Bank and Sort Code")



def property(request,property_id):
	return HttpResponse("Address and then images, Description , Features ")


def team(request):
	return HttpResponse("Describe team")

def structure(request):
	return HttpResponse("Org  structure")


def prospectus(request):
	return HttpResponse("Download link to prospectus beneath link")

def faq(request):
	return HttpResponse("List of Faq rows with drop down answers")


def settings(request):

	return HttpResponse("Edit name surname, email address, password, target saving amount " )


def regular_saving_scheme(request):
	return HttpResponse("Account Name, Bank Account, Sort Code, Savings Amount Token Amount, Pause Saving Scheme, Stop Saving Scheme")

def terms_and_conditions(request):
	return HttpResponse("TnC")

def privacy_policy(request):
	return HttpResponse("Privacy policy set out here")


def legal(request):
	return HttpResponse(" Legal information ")

def about(request):
	return HttpResponse(" About page")



def gift(request):
	return HttpResponse(" generates an email or notification in the app on the dashboard, youve been sent a gift of .. ")


def notices(request):
	return HttpResponse(" Put notices of changes or gifts received or sent opened and auctioned")



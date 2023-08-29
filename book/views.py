from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from .models import Details
# Create your views here.

def about(request):
   return HttpResponse(" this is working")

def book_all_data(request):
   
   books = Details.objects.all()
   return render(request,'show_data.html',{'books': books})





   
def book_add_data(request):
   print(request.method)
   

   if request.method == 'POST':
      print(request.POST)
      book_name = request.POST['book_name']
      book_author = request.POST['book_author']
      no_of_pages = request.POST['no_of_pages']
      publish_date = request.POST['publish_date']
      email_id = request.POST['email_id']
      book_price = request.POST['book_price']

      print(book_name,book_author,no_of_pages,publish_date,email_id,book_price)
      Details.objects.create(book_name=book_name,book_author=book_author,no_of_pages=no_of_pages,publish_date=publish_date,email_id=email_id,book_price=book_price)


      return HttpResponse("data added successfully")
   else:
      return render(request,'update_data/add_data.html')
   
      
   
   



 
 ######################## DELETE DATA (USING FORM TYPE) ###############################

# def book_data(request):

#    books = Details.objects.all()
#    if request.method == "POST":
   
#       id = request.POST.get('id')
      

#       try:
#          book = Details.objects.get(id=id)
#          book.delete()

#          return HttpResponse(f'data with id {id} was deleted')
      
#       except:
#          return HttpResponse(f'data with id {id} was not found')
      
#       return redirect('book_data')
      
#    return render(request,'book_data.html',{'books':books}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> DELETE DATA (using url type) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def book_data(request):
   books = Details.objects.all()
   return render(request,'delete_data.html',{'books':books})

def book_data_delete(request,id):

   try:
      book = Details.objects.get(id=id)
      book.delete()
      return redirect('book_data')
   except:
      return HttpResponse(f'data with id {id} was not found')
   

def show_book_data(request,id):
   

   try:
      book = Details.objects.get(id=id)
      return render(request,'show_data.html',{'book':book})
   except:
      return HttpResponse('data not found')
   


   # ********************************* UPDATE DATA ******************************

def books_data_list(request):
   
   books = Details.objects.all()
   return render(request,'update_data/books_data_list.html',{'books':books})

def update_book_data(request,id):

   print(request.method)
   print(id)
   print(Details.objects.get(id=id))
   

   

   if request.method == 'POST':
      
      book_name = request.POST['book_name']
      book_author = request.POST['book_author']
      no_of_pages = request.POST['no_of_pages']
      publish_date = request.POST['publish_date']
      email_id = request.POST['email_id']
      book_price = request.POST['book_price']

      

      try:

         book = Details.objects.get(id=id)
         

         book.book_name = book_name
         book.book_author = book_author
         book.no_of_pages = no_of_pages
         book.publish_date = publish_date
         book.email_id = email_id
         book.book_price = book_price
         book.save()
      
         return redirect('book_data')
      
      except:
         return HttpResponse('data not found of these data')
      
   else:
      book = Details.objects.get(id=id)
      return render(request,'update_data/update_book_data.html',{'book':book})

          
         
      

      

      

      



      



      



   


   
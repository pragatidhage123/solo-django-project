from django.urls import path
from . import views

urlpatterns = [
    #DEMO
    path("about/",views.about,name="about"),

    

    # ALL BOOK DATA
    path("book-data/",views.book_data,name="book_data"),

    # ADD NEW BOOK DATA
    path("book-add-data/",views.book_add_data,name="book_add_data"),

    ### DELETE DATA ###
    path("book-data-delete/<int:id>/",views.book_data_delete,name="book_data_delete"),

    ### VIEW DATA
    path("book-data-show/<int:id>/",views.show_book_data,name="show_book_data"),

    ### UPDATE DATA ###
    path("books-data-list/",views.books_data_list,name="books_data_list"),
    path("books-data-update/<int:id>/",views.update_book_data,name="update_book_data"),
    




    
    


]
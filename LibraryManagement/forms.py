from django import forms
from .models import Book, RentBook


#class AddStudent(forms.ModelForm):
    # class Meta:
    #     fields = '__all__'   # refrence a database
    #     model = addstudent


class AddBook(forms.ModelForm):
    class Meta:
        fields = '__all__'  # refrence a database
        model = Book



class BookIssued(forms.ModelForm):
    class Meta:
        #fields = '__all__'
        model = RentBook
        exclude = ['user']

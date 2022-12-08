from django.shortcuts import render, redirect
from .forms import AddStudent
from .models import addstudent
from .forms import AddBook
from .models import Book
from .forms import BookIssued
from .models import RentBook

# Create your views here.
def login(request):
    return None


def addStudent(request):
    form = AddStudent(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('showBooks')
    context = {'form': form}
    return render(request, 'LibraryManagement/AddStudent.html', context)


def addBook(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = AddBook(request.POST, request.FILES)  # request.FILES is added for the image field
        # check whether it's valid:
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # save the record into the db
            form.save()
            # after saving redirect to index page
            return redirect('showBooks')
    else:
        # if the request does not have post data, a blank form will be rendered
        form = AddBook()

    return render(request, 'LibraryManagement/AddBook.html', {'form': form})


def showBooks(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'LibraryManagement/ShowBooks.html', context)


def update_task(request, book_id):
    book = Book.objects.get(id=book_id)
    form = AddBook(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('showBooks')
    context = {'form': form}
    return render(request, 'LibraryManagement/updateTask.html', context)


def delete_task(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('showBooks')


def search(request):
    if request.method == "GET":
        search_term = request.GET.get('search') or ''
        books = Book.objects.filter(bookName__icontains=search_term)
        context = {'books': books}
        return render(request, 'LibraryManagement/ShowBooks.html', context)


def issue(request):
    if request.method == "POST":
        form = BookIssued(request.POST)
        if form.is_valid():
            # save data
            unsaved_form = form.save(commit=False)
            book_to_save = RentBook.objects.get(id=unsaved_form.book_instance.id)
            book_to_save.returned = True
            book_to_save.save()
            form.save()
            form.save_m2m()
        return redirect('showBooks')
    else:
        context = {'form': BookIssued, "book": RentBook.objects.filter(returned=False)}
        return render(request, 'LibraryManagement/updateTask.html', context=context)
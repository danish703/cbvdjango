from django.shortcuts import render,redirect
from .models import Book
from django.views import generic
from django.http import Http404
from .forms import BookCreateForm
from django.urls import reverse_lazy
# Create your views here.
# def booklist(request):
#     book  = Book.objects.all()
#     context= {
#         'book':book
#     }
#     return render(request,'booklist.html',context)

class BookList(generic.ListView):
    template_name = 'booklist.html'
    model = Book
    # queryset = Book.objects.filter(is_publish=True)
    context_object_name = 'book'
    ordering = ['-name']
    paginate_by = 4

# def details(request,pk):
#     try:
#         book = Book.objects.get(id=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#     return render(request,'details.html',context={'book':book})

class BookDetails(generic.DetailView):
    template_name = 'details.html'
    model = Book
    pk_url_kwarg = 'pk'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Book.objects.filter(id=self.kwargs[self.pk_url_kwarg])
        else:
            return Book.objects.none()

class AboutUs(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self,*args, **kwargs):
        context = super(AboutUs,self).get_context_data(*args,**kwargs)
        context["name"]="ram"
        return context


class BookCreateView(generic.CreateView):
    template_name = 'createbook.html'
    def get(self,request,*args,**kwargs):
        context = {
            'form':BookCreateForm()
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
        return render(request,self.template_name,{'form':form})


class ContactView(generic.View):
    template_name = 'contactus.html'
    def get(self,request,*args,**kwargs):
        context = {
            'abc':10
        }
        return render(request,self.template_name,context)


class UpdateView(generic.UpdateView):
    model = Book
    #fields = ['name','isbn','price','author']
    form_class = BookCreateForm
    template_name = 'update.html'
    success_url = reverse_lazy('booklist')


class MyDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')
    # template_name_suffix = '_delete'
    template_name = 'confirm.html'


from django.views.generic import ListView, CreateView, UpdateView

from .forms import PostForm, LoginForm, FeedModelForm, FileModelForm, AddForm, AddFormFile
from .models import Post, PublishedManager, FeedFile, PostFile
from django.urls import reverse_lazy

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# def create_to_feed(request):
#     user = request.user
#     if request.method == 'POST':
#         form = FeedModelForm(request.POST)
#         file_form = FileModelForm(request.POST, request.FILES)
#         files = request.FILES.getlist('file')  # field name in model
#         if form.is_valid() and file_form.is_valid():
#             feed_instance = form.save(commit=False)
#             feed_instance.user = user
#             feed_instance.save()
#             for f in files:
#                 file_instance = FeedFile(file=f, feed=feed_instance)
#                 file_instance.save()
#     else:
#         form = FeedModelForm()
#         file_form = FileModelForm()
#         return render(request, 'updocks/adddoc/postFile.html', {'form': form, 'file_form': file_form,
#                                                                 })

def add_post_and_file(request):
    user = request.user
    if request.method == 'POST':
        form = AddForm(request.POST)
        file_form = AddFormFile(request.POST, request.FILES)
        files = request.FILES.getlist('file')  # field name in model
        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save(commit=False)
            feed_instance.user = user
            feed_instance.save()

            for f in files:
                file_instance = PostFile(file=f, post=feed_instance)
                file_instance.save()
            return redirect('all')
    else:
        form = PostForm()
        file_form = AddFormFile()
        return render(request, 'updocks/adddoc/postFile.html', {'form': form, 'file_form': file_form,
                                                                })


class ListDocsPageView(ListView):
    queryset = Post.objects.filter(status='published').order_by('date_end')
    model = Post
    template_name = 'updocks/adddoc/list_docs.html'
    paginate_by = 5


def curuser(request):
    try:
        # object_list = Post.objects.filter(author=request.user)
        object_list = Post.objects.filter(author=request.user).order_by('author', 'status')

        paginator = Paginator(object_list, 5)  # 3 поста на каждой странице
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            posts = paginator.page(paginator.num_pages)
        return render(request, 'updocks/adddoc/curuser.html', {'page': page,
                                                               'posts': posts})
    except TypeError:
        return redirect('login')


class DrafPageView(ListView):
    queryset = Post.objects.filter(status='draft')
    template_name = 'updocks/adddoc/draf.html'
    paginate_by = 5


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'updocks/adddoc/post.html'
    success_url = reverse_lazy('curuser')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('file_field')
    #     if form.is_valid():
    #         id = form.save().pk
    #         author = Post.objects.get(pk=id)
    #         for f in files:
    #             fl = Post(author=author,file = f)
    #             fl.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class CreateUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'updocks/adddoc/post.html'
    success_url = reverse_lazy('curuser')

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj)
        return super(CreateUpdateView, self).dispatch(request, *args, **kwargs)


def detail(request, pk):
    post = Post.objects.get(id=pk)

    return render(request, 'updocks/adddoc/detail.html', {'post': post,
                                                          })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('all')
                else:
                    return HttpResponse('Забанен')
            else:
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'updocks/adddoc/login.html', {'form': form})


def page_not_found_view(request, exception):
    return render(request, 'updocks/adddoc/404.html', status=404)

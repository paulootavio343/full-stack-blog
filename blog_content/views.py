from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator


class PostIndex(ListView):
    template_name: str = 'index.html'
    paginate_by: int = 12
    model = Post
    context_object_name: str = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published=True).order_by('-id')
        qs = qs.select_related('post_category', 'user')

        return qs


class PostDetail(DetailView):
    template_name: str = 'post.html'
    model = Post
    context_object_name: str = 'post'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published=True)
        qs = qs.select_related('post_category', 'user')

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        similar_posts = Post.objects.filter(
            published=True, post_category=self.object.post_category
        ).order_by('-id').select_related('post_category', 'user')

        similar_posts = similar_posts.exclude(pk=self.kwargs['pk'])
        paginator = Paginator(similar_posts, 1)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

        return context


class PostCategory(PostIndex):
    template_name: str = 'search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.kwargs.get('category_slug', None)

        qs = Post.objects.filter(
            published=True, post_category__category_slug=slug).order_by('-id')
        qs = qs.select_related('post_category', 'user')

        return qs


class PostSearch(PostIndex):
    template_name = 'search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Post.objects.filter(published=True).order_by('-id')
        qs = qs.select_related('post_category', 'user')
        search = self.request.GET.get('search')

        if not search:
            return qs

        qs = qs.filter(
            Q(title__icontains=search) |
            Q(slug__icontains=search) |
            Q(user__first_name__iexact=search) |
            Q(content__icontains=search) |
            Q(excerpt__icontains=search) |
            Q(keywords__icontains=search) |
            Q(post_category__category_name__icontains=search) |
            Q(post_category__category_slug__icontains=search) |
            Q(publication_date__icontains=search) |
            Q(update_date__icontains=search)
        ).order_by('-id')

        return qs

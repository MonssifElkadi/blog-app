from django.shortcuts import get_object_or_404, render , redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request , 'blog/index.html' , {'posts' : posts})

def detail(request , id):
    post = get_object_or_404(Post , pk=id)
    return render(request , 'blog/details.html' , {'post' : post})

def create(request):
    form = PostForm(request.POST or None)
    if (form.is_valid()):
        form.save()
        return redirect('index')
    else : 
        form = PostForm()
    return render(request, 'blog/create.html', {'form' : form})

def modify(request , id):
    post = get_object_or_404(Post , pk=id)
    if request.method == "POST":
        form = PostForm(request.POST , instance=post )  
        if form.is_valid():
            form.save()
            return redirect('detail' , id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit.html', {'form': form, 'post': post})
        
def delete(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {
        'post': post
    }
    return render(request, 'blog/delete.html', context)
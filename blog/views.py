from django.shortcuts import render

# Create your views here.
def post_list(request){
  turn render(request, 'blog/post_list.html', {})
}
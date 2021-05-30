from django.shortcuts import render

def document(request):
  return render(request, 'document/html/index.html', {})
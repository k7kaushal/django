from django.shortcuts import render
# from django.http import HttpResponse #We dont need this now as we are using render and http response
posts = [ #just a dummy content so ssee how to loop thr content in html
    {
        'author': 'Kaushal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 22, 2021'
    },
    {
         'author': 'Mr.White',
        'title': 'Crystal Meth',
        'content': '1 4 8 3 6 to the 9 representing the Abq',
        'date_posted': 'June 23, 2021'
    }
]

def home(request):#by request we specify that this is howe are handling the request traffic
    # return HttpResponse('<h1>Blog Home Page</h1>')#this will need us to write the complete html code here so use render
    context = {
        'posts': posts
    }
    return render( request, "blog/home.html", context)#here by adding context we add the variable "posts" we defined above which contains the list of dict which will now be accessable thr our html template

def About(request):
    # return HttpResponse('<h1>About Page</h1>')
        return render( request, "blog/About.html", {'title': 'About'})#if the data is small enough we can directly add them to render without creating context

# def contact(request):
#     return HttpResponse('<h1>Contact Us</h1>')
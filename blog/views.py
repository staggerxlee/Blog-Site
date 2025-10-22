from django.shortcuts import render

posts=[
    {
        'author':'CoreyMS',
        'title':'First Post',
        'content':'Hey guys!',
        'date_posted':'August 27,2023'
    },
     {
        'author':'Khatry',
        'title':'Second Post',
        'content':'Hey Corey!',
        'date_posted':'August 9,2023'
    },
        {
        'author':'Nirjal',
        'title':'Painful Post',
        'content':'Teeth hurting',
        'date_posted':'August 9,2023'
    },
]



def home(request):
    context={
        'posts':posts
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})




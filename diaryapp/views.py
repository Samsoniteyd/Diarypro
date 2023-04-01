from django.shortcuts import redirect, render

from . models import Diary

# Create your views here.



def index(request):
    # create
    if request.method == 'POST':
        vtitle = request.POST['title']
        vdescription = request.POST['description']


        c = Diary(title = vtitle,description=vdescription)
        c.save()
        return redirect('index')
    
             
    # retrieve

    ra = Diary.objects.all()[:3]
    context ={
        'alls':ra
    }

    return render(request, 'diary/index.html', context)


def story(request,id):

    rs= Diary.objects.get(id=id)

    context ={
        'all':rs
    }

    return render(request, 'diary/story.html', context)

def complete(request,id):

    grab= Diary.objects.get(id=id)

    if request.method == 'POST':
        grab.complete = True

        grab.save()

        return redirect('index')   

def deletediary(request,id):
   grab= Diary.objects.get(id=id)

   if request.method == 'POST':
       grab.delete()
       grab.save()
       return redirect('index')


   context ={
       'item': grab
   }

   return render(request, 'diary/delete.html', context)   


def updatediary(request,id):
   grab= Diary.objects.get(id=id)

   if request.method== 'POST':
       grab.title= request.POST.get('title')
       grab.description= request.POST.get('description')
       grab.save()

       return redirect('index')

   context ={
       'content': grab
   }

   return render(request, 'diary/update.html', context)   
 
def about(request):
    return render(request, 'diary/about.html')

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Submission
def home(req):
    if req.method=='GET':
        return render(req, 'one.html')
    if req.method == 'POST':
            
            name = req.POST.get('name', '')
            Submission.objects.create(name=name)

            return render(req,'two.html',{'name':name})
def bc(req):
    submissions = Submission.objects.all()

    # Pass the retrieved data to the template
    return render(req, 'three.html', {'submissions': submissions}) 
def dele(req,subid):
    try:
        submission = Submission.objects.get(id=subid)
        submission.delete()
    except Submission.DoesNotExist:
        pass  # Do nothing if no records are found
    
    # Query all submissions after deletion
    submissions = Submission.objects.all()
    
    return render(req, 'three.html', {'submissions': submissions})
     
    #  try:
    #     submission = get_object_or_404(Submission, id=subid)
    #     submission.delete()
    #     return HttpResponse('Submission deleted successfully')
    #  except Exception as e:
    #     return HttpResponse(f'An error occurred: {e}', status=500)
    
    
     
   

# def fun(req):
   
    # return render(req,'one.html',{'name':"mohith","hi":'hello'})


# Create your views here.

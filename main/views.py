from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Job
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    error = User.objects.basic_validator(request.POST)
    if len(error) > 0:
        for message in error.values():
            messages.error(request, message)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(request.POST['password'].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password= pw_hash
    )
    request.session['user_id'] = new_user.id
    return redirect('/success')

def login(request):
    error = User.objects.login_validator(request.POST)
    if len(error) > 0:
        for message in error.values():
            messages.error(request, message)
        return redirect('/')
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode("utf-8"), user.password.encode("utf-8")):
            request.session['user_id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    print(logged_in_user.__dict__)
    all_job = Job.objects.all()
    all_user = User.objects.all()
    context = {
        'logged_in_user': logged_in_user,
        'user' : user,
        'all_job' : Job.objects.all(),
        'all_user' : User.objects.all()
    }
    return render(request, "success.html", context)

def edit_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'job': Job.objects.get(id=job_id),
        'logged_in_user': logged_in_user,
        'user' : user,
    }
    return render (request, "edit_job.html", context)

def job_details(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    logged_in_user = User.objects.get(id=request.session['user_id'])
    this_job = Job.objects.get(id=job_id)
    context ={
        'job': this_job,
        'all_job': Job.objects.all(),
        'logged_in_user': logged_in_user,
        'user' : user,
    }
    return render (request, "job_details.html", context)

def create_a_job(request):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context ={
        'logged_in_user': logged_in_user,
        'user' : user,
    }
    return render (request, "create_a_job.html", context)

def process_create_a_job(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    err = Job.objects.job_validator(request.POST)
    if len(err) > 0:
        for item in err.values():
            messages.error(request, item)
        return redirect('/create_a_job')
    new_job = Job.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        location=request.POST['location'],
        submitted_by=logged_in_user,
    )
    return redirect(f'/success')

def process_edit_a_job(request):
    err = Job.objects.job_validator(request.POST)
    if len(err) > 0:
        for item in err.values():
            messages.error(request, item)
        return redirect('/edit_job')
    job_id = request.POST['job_id']
    job = Job.objects.get(id=job_id)
    job.title = request.POST['title']
    job.description = request.POST['description']
    job.location = request.POST['location']
    job.save()
    return redirect(f'/job_details/{job.id}')

def destroy(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('/success')




def logout(request):
    request.session.clear()
    return redirect('/')




# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


from .models import Classroom, Student
from .forms import ClassroomForm, SigninForm, SignupForm

def classroom_list(request):
	classrooms = Classroom.objects.all()
	context = {
		"classrooms": classrooms,
	}
	return render(request, 'classroom_list.html', context)


def classroom_detail(request, classroom_id):
	classroom = Classroom.objects.get(id=classroom_id)
	context = {
		"classroom": classroom,
	}
	return render(request, 'classroom_detail.html', context)


def classroom_create(request):
	if request.user.is_anonymous:
		return redirect('signin')
	form = ClassroomForm()
	if request.method == "POST":
		form = ClassroomForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Created!")
			return redirect('classroom-list')
		print (form.errors)
	context = {
	"form": form,
	}
	return render(request, 'create_classroom.html', context)


def classroom_update(request, classroom_id):
	classroom = Classroom.objects.get(id=classroom_id)
	form = ClassroomForm(instance=classroom)
	if request.method == "POST":
		form = ClassroomForm(request.POST, request.FILES or None, instance=classroom)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Edited!")
			return redirect('classroom-list')
		print (form.errors)
	context = {
	"form": form,
	"classroom": classroom,
	}
	return render(request, 'update_classroom.html', context)


def classroom_delete(request, classroom_id):
	Classroom.objects.get(id=classroom_id).delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('classroom-list')



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("classroom-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('classroom-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")


############################################################################

 def student_list(request):
	stdn = Student.objects.all()
	context = {
		"students": stdn,
	}
	return render(request, 'student_list.html', context)


def student_detail(request, student_id):
	stdn = Student.objects.get(id=student_id)
	context = {
		"students": stdn,
	}
	return render(request, 'student_detail.html', context)


def student_create(request):
	if request.user.is_anonymous:
		return redirect('signin')
	form = StudentForm()
	if request.method == "POST":
		form = StudentForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Created!")
			return redirect('student-list')
		print (form.errors)
	context = {
	"form": form,
	}
	return render(request, 'create_student.html', context)


def student_update(request, student_id):
	stdn = Student.objects.get(id=student_id)
	form = StudentForm(instance=stdn)
	if request.method == "POST":
		form = StudentForm(request.POST, request.FILES or None, instance=stdn)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Edited!")
			return redirect('student-list')
		print (form.errors)
	context = {
	"form": form,
	"classroom": stdn,
	}
	return render(request, 'update_student.html', context)


def student_delete(request, classroom_id):
	Student.objects.get(id=student_id).delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('student-list')
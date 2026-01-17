from django.shortcuts import render
from django.http import Http404
from django.template.loader import get_template, TemplateDoesNotExist
from django.urls import path
from django.http import JsonResponse
import random
from .nlp_suggestor import suggest

def home(request):
    return render(request, 'careerBackend/index.html')

def about(request):
    return render(request, 'careerBackend/Aboutus.html')

def courses(request):
    return render(request, 'careerBackend/Courses.html')

def defence(request):
    return render(request, 'careerBackend/Defence.html')

def engineering(request):
    return render(request, 'careerBackend/Engineering.html')

def law(request):
    return render(request, 'careerBackend/Law.html')

def medical(request):
    return render(request, 'careerBackend/Medical.html')

def contact(request):
    return render(request, 'careerBackend/contactus.html')

def government(request):
    return render(request, 'careerBackend/government.html')

def others(request):
    return render(request, 'careerBackend/others.html')

def register(request):
    if request.method == 'POST':
        qualification = request.POST.get('Qualifications:')
        skills = request.POST.get('Skills:')
        interests = request.POST.get('Interests:')
        goals = request.POST.get('Message:')
        field, job_title = suggest(qualification, skills, interests, goals)
        context = {
            'career_suggestion': field,
            'job_suggestion': str(job_title),
        }
        return render(request, 'careerBackend/output.html', context)
    return render(request, 'careerBackend/Register.html')

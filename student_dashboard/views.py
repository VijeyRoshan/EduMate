from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ai_core.summarizer import summarize_text
from ai_core.quiz_generator import generate_quiz
from ai_core.doubt_solver import clarify_doubt

# Dashboard home

def dashboard(request):
    return render(request, 'dashboard.html')

# Summarization view
@csrf_exempt
def summarize(request):
    summary = None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        summary = summarize_text(text)
    return render(request, 'summarize.html', {'summary': summary})

# Quiz generation view
@csrf_exempt
def quiz(request):
    quiz_output = None
    if request.method == 'POST':
        topic = request.POST.get('topic', '')
        num_questions = int(request.POST.get('num_questions', 5))
        quiz_output = generate_quiz(topic, num_questions)
    return render(request, 'quiz.html', {'quiz': quiz_output})

# Doubt clarification view
@csrf_exempt
def doubt(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question', '')
        context = request.POST.get('context', '')
        answer = clarify_doubt(question, context)
    return render(request, 'doubt.html', {'answer': answer})

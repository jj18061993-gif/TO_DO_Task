from django.shortcuts import render, get_object_or_404
from .models import Todo


def index(request):
    todos = Todo.objects.all().order_by("id")

    return render(
        request,
        "index.html",
        {"todos": todos}
    )


def add_todo(request):

    if request.method == "POST":

        title = request.POST.get("title")

        if title:
            Todo.objects.create(title=title)

    todos = Todo.objects.all().order_by("id")

    return render(
        request,
        "todo_list.html",
        {"todos": todos}
    )


def delete_todo(request, pk):

    todo = get_object_or_404(Todo, pk=pk)

    todo.delete()

    todos = Todo.objects.all().order_by("id")

    return render(
        request,
        "todo_list.html",
        {"todos": todos}
    )


def update_todo(request, pk):

    todo = get_object_or_404(Todo, pk=pk)

    title = request.POST.get("title")

    if title:
        todo.title = title
        todo.save()

    todos = Todo.objects.all().order_by("-id")

    return render(
        request,
        "todo_list.html",
        {"todos": todos}
    )
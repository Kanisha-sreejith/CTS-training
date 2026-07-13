from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Student


@require_http_methods(["GET", "POST"])
def student_list(request):
    if request.method == "POST":
        student = Student.objects.create(
            name=request.POST.get("name", "Unknown"),
            course=request.POST.get("course", "Python"),
        )
        return JsonResponse({"id": student.id, "name": student.name, "course": student.course})

    students = list(Student.objects.values("id", "name", "course"))
    return JsonResponse(students, safe=False)


@require_http_methods(["GET", "PUT", "DELETE"])
def student_detail(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    if not student:
        return JsonResponse({"error": "Student not found"}, status=404)

    if request.method == "PUT":
        student.name = request.POST.get("name", student.name)
        student.course = request.POST.get("course", student.course)
        student.save()
        return JsonResponse({"id": student.id, "name": student.name, "course": student.course})

    if request.method == "DELETE":
        student.delete()
        return JsonResponse({"message": "Student deleted"})

    return JsonResponse({"id": student.id, "name": student.name, "course": student.course})

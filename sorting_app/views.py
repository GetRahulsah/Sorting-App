# sorting_project/sorting_app/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import SortingResult

def home(request):
    if request.method == 'POST':
        unsorted_data = request.POST.get('unsorted_data', '')
        sorting_algorithm = request.POST.get('sorting_algorithm', '')

        # Perform sorting based on the selected algorithm
        if sorting_algorithm == 'bubble_sort':
            sorted_data = bubble_sort(unsorted_data)
        elif sorting_algorithm == 'selection_sort':
            sorted_data = selection_sort(unsorted_data)
        elif sorting_algorithm == 'insertion_sort':
            sorted_data = insertion_sort(unsorted_data)
        else:
            sorted_data = None  # Handle other cases or provide a default behavior

        # Save the sorting result to the database
        sorting_result = SortingResult.objects.create(
            unsorted_data=unsorted_data,
            sorted_data=' '.join(map(str, sorted_data)) if sorted_data else None,
            sorting_algorithm=sorting_algorithm,
            timestamp=timezone.now()
        )

        return render(request, 'home.html', {'sorting_result': sorting_result})

    return render(request, 'home.html')

# bubble_sort algorithm
def bubble_sort(unsorted_data):
    data = list(map(int, unsorted_data.split()))
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

# selection_sort algorithm
def selection_sort(unsorted_data):
    data = list(map(int, unsorted_data.split()))
    n = len(data)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    return data


# insertion_sort algorithm
def insertion_sort(unsorted_data):
    data = list(map(int, unsorted_data.split()))
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

    return data

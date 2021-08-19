from .models import Category


def basetest(request):

    cat_list = Category.objects.values_list("category_name", flat=True)
    return {
        'testname': cat_list
    }
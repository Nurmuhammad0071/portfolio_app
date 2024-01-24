from django.shortcuts import render, redirect
from django.views import View
from portfolio_app.form import CommentForm
from portfolio_app.models import MyInfo, Site, Skill, Summary, Experience, Category, Portfolio, Testimonial


# Create your views here.
class IndexPage(View):
    def get(self, request):
        form = CommentForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('index.html')

        context = {
            'form': form,
            'info': MyInfo.objects.filter(status=1).first(),
            'site': Site.objects.filter(status=1).first(),
            'skill': Skill.objects.filter(status=1),
            'summary': Summary.objects.filter(status=1),
            'experience': Experience.objects.filter(status=1),
            'category': Category.objects.filter(status=1),
            'portfolio': Portfolio.objects.filter(status=1),
            'testimonial': Testimonial.objects.filter(status=1)
        }
        return render(request, 'index.html', context)


def portfolio(request, id):
    portfolios = Portfolio.objects.get(id=id)
    context = {
        'info': MyInfo.objects.filter(status=1).first(),
        'portfolio': portfolios
    }
    return render(request, 'portfolio-details.html', context)

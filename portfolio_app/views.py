from django.shortcuts import render, redirect
from django.views import View
from portfolio_app.form import CommentForm
from portfolio_app.models import MyInfo, Site, Skill, Summary, Experience, Category, Portfolio, Testimonial


# Create your views here.
from django.http import HttpResponseNotAllowed

class IndexPage(View):
    template_name = 'index.html'

    def get(self, request):
        form = CommentForm()
        info = MyInfo.objects.filter(status=1).first()
        site = Site.objects.filter(status=1).first()
        skill = Skill.objects.filter(status=1)
        summary = Summary.objects.filter(status=1)
        experience = Experience.objects.filter(status=1)
        category = Category.objects.filter(status=1)
        portfolio = Portfolio.objects.filter(status=1)
        testimonial = Testimonial.objects.filter(status=1)

        context = {
            'form': form,
            'info': info,
            'site': site,
            'skill': skill,
            'summary': summary,
            'experience': experience,
            'category': category,
            'portfolio': portfolio,
            'testimonial': testimonial
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Define the URL pattern for message_list
        else:
            # Handle invalid form data
            return HttpResponseNotAllowed(["GET"])  # You may want to customize the response for invalid data


def portfolio(request, id):
    portfolios = Portfolio.objects.get(id=id)
    context = {
        'info': MyInfo.objects.filter(status=1).first(),
        'portfolio': portfolios
    }
    return render(request, 'portfolio-details.html', context)

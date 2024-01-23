from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexPage(View):
    def get(self, request):
        # info = MyInfo.objects.all()
        # job = Job.objects.all()
        # site = Site.objects.all()
        # skill = Skill.objects.all()
        # summary = Summary.objects.all()
        # experience = Experience.objects.all()
        # portfolio = Portfolio.objects.all()
        # context = {
        #     'info': info,
        #     'job': job,
        #     'site': site,
        #     'skill': skill,
        #     'summary': summary,
        #     'experience': experience,
        #     'portfolio': portfolio
        # }
        return render(request, 'index.html')

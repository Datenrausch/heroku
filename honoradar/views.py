from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.template.defaultfilters import slugify
import datetime
from .models import *
from django.db.models import Q

#this entire view handles the process of sending data, checking it and saving it in the backend
def senddata(request):
    #this variable checks if all compulsory fields are filled and hence, a new instance should be created in the backend
    sanitycheck=0

    if request.method == 'POST':
        print("senddata")
        print("Messages here")
        for i in list(messages.get_messages(request)):
            print(i)

        #we get the three categories that all entries have in common regardless of
        #freelance, pauschalist or employed
        MediumName=(request.POST.get('MediumName'))
        FreeOrEmployed=(request.POST.get('FreeOrEmployed'))
        Comment=(request.POST.get('Comment'))
        AGB=(request.POST.get('AGB'))
        print(request.POST)


        # if the mediumname or the AGB is not given, we set the sanitycheck to 1
        #and create a warning message that will pop-up
        if MediumName:
            pass
        else:
            print("No Mediumname!!")
            sanitycheck=1
            messages.info(request, 'Medium')

        if AGB=="on":
            pass
        else:
            print("No AGB!!")
            sanitycheck=1
            messages.info(request, 'AGB fehlen')


        #CHECKING WHETHER THERE ARE ALREADY ENTIRES WITH THIS MEDIUM
        try:
            mediumobj=Medium.objects.get(
            Q(mediumname=MediumName),
            Q(freeoremployed=FreeOrEmployed)
            )
            print("Found it")
            print(mediumobj)



            #CHECKING FOR FEST, PAUSCHAL, FREI
            #if the criteria for free or employed is "fest",
            #we get the data relevant for this case
            if FreeOrEmployed=="fest":
                SalaryPerMonthEmpMix=(request.POST.get('SalaryPerMonthEmpMix'))
                Happiness=(request.POST.get("Happiness"))
                HoursPerWeekEmp=(request.POST.get("HoursPerWeekEmp"))
                JobPosition=(request.POST.get("JobPosition"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                print(request.POST)

                #check the compulsory three of them and send warning if they are missing
                if SalaryPerMonthEmpMix:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Gehalt')
                if int(Happiness) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')
                if int(HoursPerWeekEmp) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Arbeitszeit')

                #if all these data sanitychecks are okay, we bind the input to an existing medium
                if(sanitycheck==0):
                    d = mediumobj.datacollection_set.create(
                    SalaryPerMonthEmpMix=int(SalaryPerMonthEmpMix),
                    Happiness=int(Happiness),
                    HoursPerWeekEmp=int(HoursPerWeekEmp),
                    JobPosition=JobPosition,
                    Experience=Experience,
                    Comment=Comment
                    )
                else:
                    pass

            #if the criteria for free or employed is "pauschal",
            #we get the data relevant for this case
            if FreeOrEmployed=="pauschal":
                SalaryPerMonthEmpMix=(request.POST.get('SalaryPerMonthEmpMix'))
                DaysPerMonthMix=(request.POST.get("DaysPerMonthMix"))
                HoursPerDayMix=(request.POST.get("HoursPerDayMix"))
                JobPosition=(request.POST.get("JobPosition"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                Happiness=(request.POST.get("Happiness"))
                Comment=(request.POST.get("Comment"))

                #check the compulsory four of them and send warning if they are missing
                if SalaryPerMonthEmpMix:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Gehalt')

                if int(Happiness) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')

                if int(DaysPerMonthMix) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zu Tagen pro Monat')

                if int(HoursPerDayMix) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zu Stunden pro Tag')

                #if all these data sanitychecks are okay, we bind the input to an existing medium
                if(sanitycheck==0):
                    d = mediumobj.datacollection_set.create(
                        SalaryPerMonthEmpMix=int(SalaryPerMonthEmpMix),
                        DaysPerMonthMix=int(DaysPerMonthMix),
                        HoursPerDayMix=int(HoursPerDayMix),
                        JobPosition=JobPosition,
                        Experience=Experience,
                        Happiness=int(Happiness),
                        Comment=Comment,
                    )
                else:
                    pass


            if FreeOrEmployed=="frei":

                FeeFree=(request.POST.get('FeeFree'))
                VideoAudioTextFree=(request.POST.get("VideoAudioTextFree"))
                Genre=(request.POST.get("Genre"))
                AnalogDigitalFree=(request.POST.get("AnalogDigitalFree"))
                JobPosition=(request.POST.get("JobPosition"))
                HoursSpentFree=(request.POST.get("HoursSpentFree"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                Happiness=(request.POST.get("Luckiness"))
                Comment=(request.POST.get("Comment"))

                #check the compulsory four of them and send warning if they are missing
                if FeeFree:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Honorar')

                if int(Happiness) != 0:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')

                if int(HoursSpentFree) != 0.5:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Zeitaufwand')
                if(sanitycheck==0):
                    d = mediumobj.datacollection_set.create(
                    FeeFree=int(FeeFree),
                    VideoAudioTextFree=VideoAudioTextFree,
                    Genre=Genre,
                    AnalogDigitalFree=AnalogDigitalFree,
                    JobPosition=JobPosition,
                    HoursSpentFree=int(HoursSpentFree),
                    Experience=Experience,
                    Happiness=int(Happiness),
                    Comment=Comment,
                    )

        except Medium.DoesNotExist:

            if FreeOrEmployed=="fest":
                SalaryPerMonthEmpMix=(request.POST.get('SalaryPerMonthEmpMix'))
                Happiness=(request.POST.get("Happiness"))
                HoursPerWeekEmp=(request.POST.get("HoursPerWeekEmp"))
                JobPosition=(request.POST.get("JobPosition"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                print(request.POST)

                #check the compulsory three of them and send warning if they are missing
                if SalaryPerMonthEmpMix:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Gehalt')
                if int(Happiness) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')

                if float(HoursSpentFree) != 0.5:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Zeitaufwand')

                #if all these data sanitychecks are okay, we bind the input to an existing medium
                if(sanitycheck==0):
                    mediumobj = Medium(mediumname=MediumName, freeoremployed=FreeOrEmployed)
                    mediumobj.save()
                    d = mediumobj.datacollection_set.create(
                    SalaryPerMonthEmpMix=int(SalaryPerMonthEmpMix),
                    Happiness=int(Happiness),
                    HoursPerWeekEmp=int(HoursPerWeek),
                    JobPosition=JobPosition,
                    Experience=Experience,
                    Comment=Comment
                    )



            if FreeOrEmployed=="pauschal":
                SalaryPerMonthEmpMix=(request.POST.get('SalaryPerMonthEmpMix'))
                DaysPerMonthMix=(request.POST.get("DaysPerMonthMix"))
                HoursPerDayMix=(request.POST.get("HoursPerDayMix"))
                JobPosition=(request.POST.get("JobPosition"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                Happiness=(request.POST.get("Happiness"))
                Comment=(request.POST.get("Comment"))
                #check the compulsory four of them and send warning if they are missing
                if SalaryPerMonthEmpMix:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Gehalt')

                if int(Happiness) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')

                if int(DaysPerMonthMix) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zu Tagen pro Monat')

                if int(HoursPerDayMix) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zu Stunden pro Tag')

                if(sanitycheck==0):

                    mediumobj = Medium(mediumname=MediumName, freeoremployed=FreeOrEmployed)
                    mediumobj.save()

                    d = mediumobj.datacollection_set.create(
                    SalaryPerMonthEmpMix=int(SalaryPerMonthEmpMix),
                    DaysPerMonthMix=int(DaysPerMonthMix),
                    HoursPerDayMix=int(HoursPerDayMix),
                    JobPosition=str(JobPosition),
                    Experience=str(Experience),
                    Happiness=int(Happiness),
                    Comment=str(Comment),
                    )


            if FreeOrEmployed=="frei":
                FeeFree=(request.POST.get('FeeFree'))
                VideoAudioTextFree=(request.POST.get("VideoAudioTextFree"))
                Genre=(request.POST.get("Genre"))
                AnalogDigitalFree=(request.POST.get("AnalogDigitalFree"))
                JobPosition=(request.POST.get("JobPosition"))
                HoursSpentFree=(request.POST.get("HoursSpentFree"))
                Experience=(request.POST.get("ExperienceEmplMix"))
                Happiness=(request.POST.get("Luckiness"))
                Comment=(request.POST.get("Comment"))

                #check the compulsory four of them and send warning if they are missing
                if FeeFree:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Honorar')

                if int(Happiness) != 1:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zur Zufriedenheit')

                if float(HoursSpentFree) != 0.5:
                    pass
                else:
                    sanitycheck=1
                    messages.info(request, 'Angabe zum Zeitaufwand')
                if(sanitycheck==0):
                    mediumobj = Medium(mediumname=MediumName, freeoremployed=FreeOrEmployed)
                    mediumobj.save()

                    d = mediumobj.datacollection_set.create(
                    FeeFree=int(FeeFree),
                    VideoAudioTextFree=VideoAudioTextFree,
                    Genre=Genre,
                    AnalogDigitalFree=AnalogDigitalFree,
                    JobPosition=JobPosition,
                    HoursSpentFree=int(HoursSpentFree),
                    Experience=Experience,
                    Happiness=int(Happiness),
                    Comment=Comment,
                    )

    #return render(request, 'honoradar/index.html')
    return HttpResponseRedirect(reverse('honoradar:index'))

def getdata(request):
    print(request.GET)
    MediumGet=(request.GET.get('mediumget'))
    FreeOrEmployedGet=(request.GET.get('switch'))
    print(MediumGet)
    print(FreeOrEmployedGet)

    try:
        mediumobj=Medium.objects.get(
        Q(mediumname=MediumGet),
        Q(freeoremployed=FreeOrEmployedGet)
        )
        print(mediumobj.mediumname)
        entries = DataCollection.objects.filter(Medium = mediumobj)
        print("found")
        for i in entries:
            print(i.Happiness)


        return HttpResponseRedirect(reverse('honoradar:index'))


    except Medium.DoesNotExist:
        print("Sorry, wir haben noch keine Daten")

        return HttpResponseRedirect(reverse('honoradar:index'))




class IndexView(generic.ListView):
    template_name = 'honoradar/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'honoradar/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'honoradar/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'honoradar/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('honoradar:results', args=(question.id,)))

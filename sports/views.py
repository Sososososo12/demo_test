from django.shortcuts import render

# Create your views here.
from sports import models
from sports import models


# sel_order=0
# search_messages=0

def getsearchhtml(request):
    return (render(request, 'search new.html'))

def gettable(request):

    all_messages=models.SportsPaper.objects.filter(paperauthor__authorname__icontains='1')
    # for message in all_messages:    #     print(message)

    # return (render(request, 'table_test.html',{'papers_list':all_messages}))

def searchindex(request):

    sel_content=request.POST.get("select", None)
    sel_order = request.POST.get("select_order", None)
    searchtext= request.POST.get("textfield", None)
    # search_me_order=models.SportsPaper.objects
    if searchtext=='':
        return(render(request,'table_test_blank.html'))

    if sel_content == "1":   #post到表单中select组件的值为1的时候
        if sel_order=="21":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by('title')
        elif sel_order=="22":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by('-title')
        elif sel_order == "23":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by(
                'paperauthor__authorname')
        elif sel_order == "24":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by(
                '-paperauthor__authorname')
        elif sel_order == "25":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by('publicdate')
        elif sel_order == "26":
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext).order_by('-publicdate')
        else:
            search_messages = models.SportsPaper.objects.filter(title__icontains=searchtext)
        return (render(request, 'table_test_pa.html', {'papers_list': search_messages,'trantext':searchtext}))

    if sel_content == "2":   #post到表单中select组件的值为2的时候
        if sel_order=="21":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by('title')
        elif sel_order=="22":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by('-title')
        elif sel_order == "23":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by(
                'paperauthor__authorname')
        elif sel_order == "24":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by(
                '-paperauthor__authorname')
        elif sel_order == "25":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by('publicdate')
        elif sel_order == "26":
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext).order_by('-publicdate')
        else:
            search_messages = models.SportsPaper.objects.filter(paperauthor__authorname__icontains=searchtext)
        return (render(request, 'table_test_au.html', {'authors_list': search_messages,'trantext':searchtext}))



    if sel_content == "3":   #post到表单中select组件的值为3的时候
        if sel_order=="21":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by('title')
        elif sel_order=="22":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by('-title')
        elif sel_order == "23":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by(
                'paperauthor__authorname')
        elif sel_order == "24":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by(
                '-paperauthor__authorname')
        elif sel_order == "25":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by('publicdate')
        elif sel_order == "26":
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext).order_by('-publicdate')
        else:
            search_messages = models.SportsPaper.objects.filter(bejournalid__journalname__icontains=searchtext)
        return (render(request, 'table_test_jl.html', {'journal_list': search_messages,'trantext':searchtext}))

    return (render(request, 'search_url.html'))

def getsta_index(request):
    return (render(request, 'statistics_index.html'))

def getsta_table1(request):
    return (render(request, 'core_quote.html'))

def getsta_core_fund_table(request):
    return (render(request, 'core_fund.html'))
def getsta_core_fund_pic(request):
    return (render(request, 'core_fund_pic.html'))

def getsta_pa_org_table(request):
    return (render(request, 'pa_org.html'))
def getsta_pa_org_pic(request):
    return (render(request, 'pa_org_pic.html'))

def getsta_pa_dis_table(request):
    return (render(request, 'pa_dis.html'))
def getsta_pa_dis_pic(request):
    return (render(request, 'pa_dis_pic.html'))

def getsta_bo_table(request):
    return (render(request, 'book_quote.html'))
def getsta_bo_quote_pic(request):
    return (render(request, 'book_quote_pic.html'))

def backhome(request):
    return (render(request,'index_welcome.html'))

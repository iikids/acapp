from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align:center">我的第一个界面 </h1>'
    line2 = '<a href = "/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line2)


def play(request):
    line1 = '<h1 style = "text-align:center">游戏界面</h1>'
    line2 = '<a href = "/">返回上一层</a>'
    return HttpResponse(line1 + line2)

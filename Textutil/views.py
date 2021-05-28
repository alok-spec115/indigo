from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'text_analyze.html')

def removepunct(request):
    input_text = request.POST.get('text', 'nothing to show')
    removepunc = request.POST.get('removepunct', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lineremove = request.POST.get("lineremover", 'off')
    spaceremove = request.POST.get('spaceremover', 'off')

    if spaceremove == 'on':
        display_text = ''
        for index, word in enumerate(input_text):
            if not(input_text[index] == ' ' and input_text[index + 1] == ' '):
                display_text += word
        input_text = display_text

    if removepunc == 'on':
        punctuations = '''{}[];':",./?-~!()'''
        display_text = ''
        for word in input_text:
            if word not in punctuations:
                display_text += word
        input_text = display_text

    if uppercase == 'on':
        display_text = ''
        display_text += input_text.upper()
        input_text = display_text

    if lineremove == 'on':
        display_text = ''
        for word in input_text:
            if word != '\n' and word !='\r':
                display_text += word
        input_text = display_text

    if uppercase == 'on' or removepunc == 'on' or lineremove == 'on' or spaceremove == 'on':
        dic = {
        "analyzed_text": display_text,
        'content': 'Your analyzed text is :-',
        }
        return render(request, 'result.html', dic)

    else:
        dicti = {'error': "Please choose one of the checkbox!"}
        return render(request, 'result.html', dicti)
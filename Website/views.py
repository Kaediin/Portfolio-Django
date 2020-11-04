import json
import os.path

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Website.models import Tile, ButtonLink, ResumeItem

# Create your views here.

BASE = os.path.dirname(os.path.abspath(__file__))

def index(request):
    json_data = open(os.path.join(BASE, "templates/languages_text_EN.json"))
    data = getJson(json_data)
    return returnToPage(request, data, 'EN', False)

def english(request):
    json_data = open(os.path.join(BASE, "templates/languages_text_EN.json"))
    data = getJson(json_data)
    return returnToPage(request, data, 'EN', False)


def dutch(request):
    json_data = open(os.path.join(BASE, "templates/languages_text_NL.json"))
    data = getJson(json_data)
    return returnToPage(request, data, 'NL', False)


def sendmailtouser(request):
    print('Mail should be sent')

    lang = request.POST.get('lang_hidden')
    subject = request.POST.get('contact_form_subject')
    message = request.POST.get('contact_form_message')
    email_from = request.POST.get('contact_form_email')
    recipient_list = ['skaedin@gmail.com', email_from]

    send_mail(subject, message, email_from, recipient_list, )
    if lang == 'NL':
        json_data = open(os.path.join(BASE, "templates/languages_text_NL.json"))
    else:
        json_data = open(os.path.join(BASE, "templates/languages_text_EN.json"))

    data = getJson(json_data)
    return returnToPage(request, data, lang, True)



def getJson(json_data):
    deserialized_json = json.load(json_data)
    dump = json.dumps(deserialized_json)
    data = json.loads(dump)
    return data

def returnToPage(request, data, lang, isForm):
    centered_img_button_left = data['centered_img_button_left']
    centered_img_button_right = data['centered_img_button_right']
    navbar_link1 = data['navbar_link1']
    navbar_link2 = data['navbar_link2']
    navbar_link3 = data['navbar_link3']
    navbar_link4 = data['navbar_link4']
    aboutme_header = data['aboutme_header']
    aboutme_typewriter_title = data['aboutme_typewriter_title']
    aboutme_typewriter_description = data['aboutme_typewriter_description']
    projects_header = data['projects_header']
    contact_header = data['contact_header']
    contact_form_title = data['contact_form_title']
    contact_form_subject_placeholder = data['contact_form_subject_placeholder']
    contact_form_email_placeholder = data['contact_form_email_placeholder']
    contact_form_message_placeholder = data['contact_form_message_placeholder']
    contact_form_button_submit = data['contact_form_button_submit']
    form_alert_sendingmail = data['form_alert_sendingmail']
    form_alert_invalidform = data['form_alert_invalidform']

    tiles = []

    for tile in data['tiles']:
        project = str(tile['project'])
        img = str(tile['img'])
        softwares = str(tile['softwares'])
        description = str(tile['description'])
        buttonsJson = tile['buttons']
        buttons = []

        for button in buttonsJson:
            buttons.append(ButtonLink(
                str(button['imgPath']),
                button['buttonUrl']
            ))

        Tile(
            project,
            img,
            softwares,
            description,
            buttons
        )

        tiles.append(tile)

    if isForm:
        return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'index.html', {
            'lang': lang,
            'centered_img_button_left': centered_img_button_left,
            'centered_img_button_right': centered_img_button_right,
            'navbar_link1': navbar_link1,
            'navbar_link2': navbar_link2,
            'navbar_link3': navbar_link3,
            'navbar_link4': navbar_link4,
            'aboutme_header': aboutme_header,
            'aboutme_typewriter_title': aboutme_typewriter_title,
            'aboutme_typewriter_description': aboutme_typewriter_description,
            'projects_header': projects_header,
            'contact_header': contact_header,
            'contact_form_title': contact_form_title,
            'contact_form_subject_placeholder': contact_form_subject_placeholder,
            'contact_form_email_placeholder': contact_form_email_placeholder,
            'contact_form_message_placeholder': contact_form_message_placeholder,
            'contact_form_button_submit': contact_form_button_submit,
            'tiles': tiles,
            'form_alert_sendingmail': form_alert_sendingmail,
            'form_alert_invalidform': form_alert_invalidform
        })

def toResume(request):
    json_data = open(os.path.join(BASE, "templates/resume_text.json"))
    data = getJson(json_data)

    biography = data['biography']
    experiences = fillListsResumeItems(data, 'experiences')
    educations = fillListsResumeItems(data, 'educations')
    skills = fillListsResumeItems(data, 'skills')


    return render(request, 'resume.html', {
        'biography': biography,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    })

def fillListsResumeItems(data, listKeyword):

    list = []

    for jsonItem in data[listKeyword]:
        time = str(jsonItem['time'])
        title = str(jsonItem['title'])
        show_circle = bool(jsonItem['show_circle'])

        resumeItem = ResumeItem(
            time,
            title,
            show_circle
        )

        list.append(resumeItem)
    return list

def spacexPrivacy(request):
    return render(request, 'privacy_spacex.html', {})





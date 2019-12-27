from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import PostForm, UpdatePostForm
from datetime import date
from .models import Post
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# POST CREATE
@login_required(login_url="Account:login")
def createV(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        # commit işlemi ile , formu kendimiz kaydedeceğimizi söylüyoruz.
        post = form.save(commit=False)
        # Formu hangi kullanıcının oluşturduğunu belirliyoruz.
        post.author = request.user
        post.save()

        htmly = get_template('email_message.html')
        d = {'author': post.author, 'title': post.title,
             'subject': post.get_subject_display(), 'docnumber': post.docnumber,
             'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content}

        subject, from_email, to = 'KAPP İletişim Portalı - Yeni Mesaj !', 'planlama@kapp.com.tr', 'planlama@kapp.com.tr'
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, "Mesaj başarı ile gönderildi.")
        return redirect("index")

    content = {
        "form": form
    }
    return render(request, "create_post.html", content)

# POST UPDATE
@login_required(login_url="Account:login")
def updateV(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    adminform = UpdatePostForm(request.POST or None, instance=post)
    if request.user.is_admin:
        if adminform.is_valid():
            # commit işlemi ile , formu kendimiz kaydedeceğimizi söylüyoruz.
            post = adminform.save(commit=False)
        # Formu hangi kullanıcının oluşturduğunu belirliyoruz.
            #post.author = request.user
            post.save()

            # KAPP İletişim Portalı - Mesaj Onaylandı !
            for email in request.POST.getlist('mail_group'):
                if post.status == "1" and email == "Y":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "M":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'muhasebe@kapp.com.tr', 'b.aykan@kapp.com.tr', 'personel@kapp.com.tr', 'h.erturk@kapp.com.tr', 't.aksari@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "F":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'm.ercin@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "IH":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'export@kapp.com.tr', 'export2@kapp.com.tr', 'export3@kapp.com.tr', 'lojistik2@kapp.com.tr', 'lojistik3@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "S":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'b.oguz@kapp.com.tr', 'malkabul@kapp.com.tr', 'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "IP":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        't.ozsirvan@kapp.com.tr', 't.tanagar@kapp.com.tr', 'n.yildemir@kapp.com.tr', 'lojistik@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "P":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'planlama@kapp.com.tr', 'planlama1@kapp.com.tr', 'donusum@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "U":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'y.aydogar@kapp.com.tr', 'a.baspinar@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "D":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'malkabul@kapp.com.tr', 'n.yildemir@kapp.com.tr', 'lojistik3@kapp.com.tr', 'lojistik@kapp.com.tr', 't.ozsirvan@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "B":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'bilgiislem@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "E":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'mertcan@kapponline.com.tr', 'elif@kapponline.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "IK":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'personel@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "1" and email == "G":
                    htmly = get_template('email_confirmed.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', ['mertcan@kapponline.com.tr', 'elif@kapponline.com.tr', 'bilgiislem@kapp.com.tr', 'malkabul@kapp.com.tr', 
                                                                                                                    'n.yildemir@kapp.com.tr', 'lojistik3@kapp.com.tr', 
                                                                                                                    'lojistik@kapp.com.tr', 't.ozsirvan@kapp.com.tr',
                                                                                                                    'y.aydogar@kapp.com.tr', 'a.baspinar@kapp.com.tr',
                                                                                                                    'planlama1@kapp.com.tr', 'donusum@kapp.com.tr',
                                                                                                                    'personel@kapp.com.tr', 't.tanagar@kapp.com.tr', 'b.oguz@kapp.com.tr',
                                                                                                                    'export@kapp.com.tr', 'export2@kapp.com.tr', 'export3@kapp.com.tr', 'lojistik2@kapp.com.tr',
                                                                                                                    'm.ercin@kapp.com.tr', 'muhasebe@kapp.com.tr', 'b.aykan@kapp.com.tr', 'personel@kapp.com.tr', 'h.erturk@kapp.com.tr',
                                                                                                                    't.aksari@kapp.com.tr', 'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                # MESSAGE REFUSED
                if post.status == "2" and email == "Y":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "M":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Onaylandı !', 'planlama@kapp.com.tr', [
                        'muhasebe@kapp.com.tr', 'b.aykan@kapp.com.tr', 'personel@kapp.com.tr', 'h.erturk@kapp.com.tr', 't.aksari@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "F":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'm.ercin@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "IH":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'export@kapp.com.tr', 'export2@kapp.com.tr', 'export3@kapp.com.tr', 'lojistik2@kapp.com.tr', 'lojistik3@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "S":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'b.oguz@kapp.com.tr', 'malkabul@kapp.com.tr', 'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "IP":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        't.ozsirvan@kapp.com.tr', 't.tanagar@kapp.com.tr', 'n.yildemir@kapp.com.tr', 'lojistik@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "P":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'planlama@kapp.com.tr', 'planlama1@kapp.com.tr', 'donusum@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "U":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'y.aydogar@kapp.com.tr', 'a.baspinar@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "D":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'malkabul@kapp.com.tr', 'n.yildemir@kapp.com.tr', 'lojistik3@kapp.com.tr', 'lojistik@kapp.com.tr', 't.ozsirvan@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "B":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'bilgiislem@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "E":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'mertcan@kapponline.com.tr', 'elif@kapponline.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "IK":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', [
                        'personel@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                if post.status == "2" and email == "G":
                    htmly = get_template('email_refused.html')
                    d = {'author': post.author, 'title': post.title,
                         'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                         'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                         }
                    subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Reddedildi !', 'planlama@kapp.com.tr', ['mertcan@kapponline.com.tr', 'elif@kapponline.com.tr', 
                                                                                                                    'bilgiislem@kapp.com.tr', 'malkabul@kapp.com.tr', 
                                                                                                                    'n.yildemir@kapp.com.tr', 'lojistik3@kapp.com.tr', 
                                                                                                                    'lojistik@kapp.com.tr', 't.ozsirvan@kapp.com.tr',
                                                                                                                    'y.aydogar@kapp.com.tr', 'a.baspinar@kapp.com.tr',
                                                                                                                    'planlama1@kapp.com.tr', 'donusum@kapp.com.tr',
                                                                                                                    'personel@kapp.com.tr', 't.tanagar@kapp.com.tr', 'b.oguz@kapp.com.tr',
                                                                                                                    'export@kapp.com.tr', 'export2@kapp.com.tr', 'export3@kapp.com.tr', 'lojistik2@kapp.com.tr',
                                                                                                                    'm.ercin@kapp.com.tr', 'muhasebe@kapp.com.tr', 'b.aykan@kapp.com.tr', 'personel@kapp.com.tr', 'h.erturk@kapp.com.tr',
                                                                                                                    't.aksari@kapp.com.tr', 'a.gurkaynak@kapp.com.tr', 'y.onkul@kapp.com.tr']
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(
                        subject, html_content, from_email, to)
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()                                                            

            messages.success(request, "Mesaj başarı ile güncellendi.")
            return redirect("index")

        content = {
            "adminform": adminform
        }
        return render(request, "update_post.html", content)

    else:
        if form.is_valid():
            # commit işlemi ile , formu kendimiz kaydedeceğimizi söylüyoruz.
            post = form.save(commit=False)
        # Formu hangi kullanıcının oluşturduğunu belirliyoruz.
            post.author = request.user
            post.save()
            htmly = get_template('email_message.html')
            d = {'author': post.author, 'title': post.title,
                 'subject': post.get_subject_display(), 'docnumber': post.docnumber,
                 'duedate': post.duedate, 'status': post.get_status_display(), 'content': post.content
                 }
            subject, from_email, to = 'KAPP İletişim Portalı - Mesaj Kullanıcı Tarafından Güncellendi !', 'planlama@kapp.com.tr', 'planlama@kapp.com.tr'
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Mesaj başarı ile güncellendi.")
            return redirect("index")

        content = {
            "form": form
        }
        return render(request, "update_post.html", content)

# POST DELETE
@login_required(login_url="Account:login")
def deleteV(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Mesaj başarı ile silindi.")
    return redirect("index")


# SENT POST
class sentpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    context_object_name = 'post'
    template_name = "sent_post.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).all()


# INBOX POST
class inboxpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    context_object_name = 'inbox_post'
    template_name = "inbox_post.html"

    def get_queryset(self):
        return Post.objects.exclude(author=self.request.user).all()


# USER PENDING POST
class pendingpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    context_object_name = 'pending_post'
    template_name = "pending_post.html"

    def get_queryset(self):
        return Post.objects.filter(status=0, author=self.request.user).all()


# ADMIN PENDING POST
class adminpendingpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    context_object_name = 'admin_pending_post'
    template_name = "admin_pending_post.html"

    def get_queryset(self):
        return Post.objects.filter(status=0).exclude(author=self.request.user).all()


# USER CONFIRMED POST
class confirmedpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    template_name = "confirmed_post.html"
    context_object_name = "confirmed_post"

    def get_queryset(self):
        return Post.objects.filter(status="1", author=self.request.user).all()

# ADMIN CONFIRMED POST


class adminconfirmedpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    template_name = "admin_confirmed_post.html"
    context_object_name = "admin_confirmed_post"

    def get_queryset(self):
        return Post.objects.filter(status="1").all()


# user REFUSED POST
class refusedpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    template_name = "refused_post.html"
    context_object_name = "refused_post"

    def get_queryset(self):
        return Post.objects.filter(status="2", author=self.request.user).all()

# ADMIN REFUSED POST


class adminrefusedpostV(LoginRequiredMixin, ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by = 3
    template_name = "admin_refused_post.html"
    context_object_name = "admin_refused_post"

    def get_queryset(self):
        return Post.objects.filter(status="2").all()

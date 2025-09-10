from django.shortcuts import (render,redirect,resolve_url,HttpResponse)
from django.views import View
from Models.models import (profile_model,send_message,upload_product,
                          home_dalevery_model,kuriar_dalevery_model,blog_model,
                          upload_videos,)
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout,user_logged_in
from .forms import register_forms
from django.db.models import Q
# Create your views here.

class HOME_PAGE(View):
    def get(self,request):
        ALL_UPLOAD_PRODUCT = upload_product.objects.filter().order_by('-id')
        self.notification_list = []
        noti = request.user.profile_model.welcome_notification
        self.notification_list.append(str(noti))
        self.notification_length = len(self.notification_list)
        return render(request,'index.html',{'ALL_UPLOAD_PRODUCT':ALL_UPLOAD_PRODUCT,'notification_length':self.notification_length})

    def post(self,request):
        pass

class REGISTER_PAGE(View):
    def get(self,request):
        REGISTER_FROM = register_forms()
        return render(request,'register.html')

    def post(self,request):
        if 'sumbits' in request.POST:
            REGISTER_FROM = register_forms(request.POST)
            if REGISTER_FROM.is_valid():
                REGISTER_FROM.save()
                self.username = request.POST['username']
                self.address = request.POST['address']
                self.phone = request.POST['phone']
                self.password1 = request.POST['password1']
                self.password2 = request.POST['password2']

                if self.username == '' and self.address == '' and self.phone == '' and self.password1 == '' and self.password2 == '':
                    return redirect('/REGISTER_PAGE')

                else:

                    USERNAME = User.objects.get(username=self.username)
                    login(request, USERNAME)

                    self.PROFILE_CREATED = profile_model.objects.create(
                    username = USERNAME,address = self.address,
                    phone = self.phone,password1 = self.password1,
                    password2 = self.password2,is_saller = False,
                    )
                    self.PROFILE_CREATED.save()

                    return redirect('/LOGIN_PAGE')

            return redirect('/REGISTER_PAGE')


class LOGIN_PAGE(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        if 'sumbits' in request.POST:
            username = request.POST['username']
            password = request.POST['password2']
            USER = authenticate(request, username=username, password=password)
            if USER is not None:
                login(request, USER)
                #---------Login User ID---------------------------#
                return redirect('/')
            else:
                print('Username and Password Incorrect')

        return redirect('/LOGIN_PAGE')


#--------------------------------Logout Method--------------------------------#
class LOGOUT_PAGE(View):
    def get(self,request):
        logout(request)
        return redirect('/LOGIN_PAGE')

#--------------------------------Upload Product---------------------------------------------------#
class UPLOAD_PRODUCT(View):
    def get(self, request, pk):

        return render(request,'upload_product.html')

    def post(self,request,pk):
        if 'product_upload_button' in request.POST:
            product_name = request.POST['product_name']
            ammount = request.POST['ammount']
            details = request.POST['details']
            saller = request.user.profile_model

            if request.method =='POST' and request.FILES is not None:

                product_image = request.FILES.get('image_upload')

                UPLOAD_PRODUCT_CREATE = upload_product.objects.create(
                saller = saller,
                product_name = product_name,
                ammount = ammount,
                details = details,
                product_image = product_image,
                )
                UPLOAD_PRODUCT_CREATE.save()
                return redirect('/'+str(request.user.profile_model.pk) +'/' +'UPLOAD_PRODUCT')
            else:
                return redirect('/' + str(request.user.profile_model.pk) + '/' + 'UPLOAD_PRODUCT')
#----------------------------Product Details-----------------------------#
class PRODUCT_DETAILS(View):
    def get(self,request,pk):
        CURRENT_PRODUCT_DETAIS = upload_product.objects.filter(id=pk)
        return render(request,'product_details.html',{'CURRENT_PRODUCT_DETAIS':CURRENT_PRODUCT_DETAIS})

    def post(self,request,pk):
        pass
#------------------------------Setting-----------------------------------#
class SETTING_PAGE(View):
    def get(self, request, pk):
    #----------------Show Current Upload Product----------------------#
        UPLOAD_PRODUCT = upload_product.objects.filter().order_by('-id')
        return render(request,'setting.html',{'UPLOAD_PRODUCT':UPLOAD_PRODUCT},)

    def post(self,request,pk):
    #-----------------------------Upload Profile Image-----------------------------------------#
        if request.method =='POST' and request.FILES is not None:
            select_image = request.FILES.get('profile_select_button')

            UPLOAD_PRFILE_IMAGE = profile_model(id=request.user.profile_model.pk,username=request.user.profile_model.username,
            address = request.user.profile_model.address,phone = request.user.profile_model.phone,
            password1= request.user.profile_model.password1,password2=request.user.profile_model.password2,
            profile_image = select_image,is_saller = request.user.profile_model.is_saller,)
            UPLOAD_PRFILE_IMAGE.save()
            return redirect('/' + str(request.user.profile_model.pk) + '/' +'SETTING_PAGE')

#------------------------------Buy Product-----------------------------------#
class BUY_PAGE(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            CURRETN_PRODUCT_DEATILS = upload_product.objects.filter(id=pk)
            return render(request,'buy_product.html',{'CURRETN_PRODUCT_DEATILS':CURRETN_PRODUCT_DEATILS,})
        else:
            return redirect('/LOGIN_PAGE')


    def post(self,request,pk):
        CURRENT_PRODUCT_BUY = upload_product.objects.filter(id=pk)
        for PRODUCT in CURRENT_PRODUCT_BUY:
            self.PRODUCTS = PRODUCT.product_name
            self.PRODUCTS_IMAGE_HOME = PRODUCT.product_image
            self.PRODUCTS_IMAGE_KURIAR = PRODUCT.product_image
        #----------------Home Delevery-------------------#
        if 'hsubmit' in request.POST:
            self.item_name = self.PRODUCTS
            self.weight = request.POST['weight']
            #self.customars_name = request.POST['hname']
            #self.customars_address = request.POST['haddress']
            #self.customars_phone = request.POST['hphone']

            HOME_DELEVERY_MODEL = home_dalevery_model.objects.create(
            item_name = self.item_name,
            weight = self.weight,
            customars_name1 = request.user.profile_model,
            customars_address = request.user.profile_model.address,
            customars_phone = request.user.profile_model.phone,
            home_product_image = self.PRODUCTS_IMAGE_HOME,
            )
            HOME_DELEVERY_MODEL.save()
            return redirect('/')
        #----------------Kuriar Delevery-----------------#
        if 'ksubmit' in request.POST:
            self.item_name = self.PRODUCTS
            self.weight = request.POST['weight']
            #self.customars_name = request.POST['kname']
            #self.customars_phone = request.POST['kphone']
            self.kuriar_address = request.POST['kaddress']

            KURIAR_DELEVERY_MODEL = kuriar_dalevery_model.objects.create(
            item_name = self.item_name,
            weight = self.weight,
            customars_name2 = request.user.profile_model,
            customars_phone = request.user.profile_model.phone,
            kuriar_address = self.kuriar_address,
            kuriar_product_image = self.PRODUCTS_IMAGE_KURIAR,
            )
            KURIAR_DELEVERY_MODEL.save()
            return redirect('/' + str(request.user.profile_model.pk) + '/' + 'BUY_PAGE')
#------------------------------Delevery Information---------------------------------#
class HOME_DELEVERY_INFORMATION(View):
    def get(self,request,pk):
        HOME_DELEVERY_INFORMATION = home_dalevery_model.objects.filter().order_by('-id')
        return render(request,'home_delevery_info.html',{'HOME_DELEVERY_INFORMATION':HOME_DELEVERY_INFORMATION})

    def post(self,request,pk):
        pass
#------------------------------Kuriar Information---------------------------------#
class KURIAR_DELEVERY_INFORMATION(View):
    def get(self,request,pk):
        KURIAR_DELEVERY_INFORMATION = kuriar_dalevery_model.objects.filter().order_by('-id')
        return render(request,'kuriar_delevery_info.html',{'KURIAR_DELEVERY_INFORMATION':KURIAR_DELEVERY_INFORMATION})

    def post(self,request,):
        pass

#------------------------------Find Friend---------------------------------#
class FINDE_FRIEND(View):
    def get(self,requert,pk):
        ALL_USER = profile_model.objects.filter()
        return render(requert,'finde_friend.html',{'ALL_USER':ALL_USER})

    def post(self,request):
        pass

class PUBLIC_PROFILE_PAGE(View):
    def get(self,request,pk):
        ALL_PUBLIC = profile_model.objects.filter(id=pk)
        CURRENT_USER = request.user.profile_model.pk
        return render(request,'public_profile.html',{'ALL_PUBLIC':ALL_PUBLIC})

    def post(self,request,pk):
        pass

class FACE_TO_FACE_MESSAGE(View):
    def get(self,request,pk):
        #--------------------------Finding Current Sender and Recever Message--------------------------------------#
        CURRENT_PUBLIC = profile_model.objects.filter(id=pk)
        for RECEVER in CURRENT_PUBLIC:
            self.CURRENT_PUBLIC = RECEVER

        self.FINDING_SEND_RECEV_MESSAGE = send_message.objects.filter(Q(sender=request.user.profile_model) | Q(recever=request.user.profile_model)).order_by('-id')
        for CURRENT_SENDER_RECEVER_MESSAGE in self.FINDING_SEND_RECEV_MESSAGE:
            if request.user.profile_model == CURRENT_SENDER_RECEVER_MESSAGE.sender and self.CURRENT_PUBLIC == CURRENT_SENDER_RECEVER_MESSAGE.recever or self.CURRENT_PUBLIC == CURRENT_SENDER_RECEVER_MESSAGE.sender and request.user.profile_model == CURRENT_SENDER_RECEVER_MESSAGE.recever:
                pass
        #--------------------------Seen Incomming Message--------------------------------------#
        FINDING_SEEN_SENDER = send_message.objects.filter(sender=pk)
        FINDING_SEEN_RECEVER = send_message.objects.filter(recever=pk)
        for SENDER_SEEN in FINDING_SEEN_SENDER:
            id = SENDER_SEEN.pk
            sender = SENDER_SEEN.sender
            recever = SENDER_SEEN.recever
            text_message = SENDER_SEEN.text_message
            seen = SENDER_SEEN.seen

            SEEN_CURRENT_MESSAGE = send_message(id=id,sender=sender,recever=recever,text_message=text_message,seen=True)
            SEEN_CURRENT_MESSAGE.save()

        return render(request,'face_to_face_message.html',{'FINDING_SEND_RECEV_MESSAGE':self.FINDING_SEND_RECEV_MESSAGE,'CURRENT_PUBLIC':self.CURRENT_PUBLIC,})

    def post(self,request,pk):
    #--------------------------Send Message--------------------------------------#
        if 'send_button' in request.POST:
            CURRENT_PUBLIC = profile_model.objects.filter(id=pk)
            for RECEVER in CURRENT_PUBLIC:

                CURRENT_USER = request.user.profile_model

                self.text_message = request.POST['text_message']

                sender = CURRENT_USER
                recever = RECEVER
                text_message = self.text_message

                SEND_MESSAGE = send_message.objects.create(
                sender = sender,
                recever =recever,
                text_message = text_message,
                seen = False,
                )
                SEND_MESSAGE.save()
                return redirect('/' + str(RECEVER.pk) + '/' + 'FACE_TO_FACE_MESSAGE')

class INCOMMING_MESSAGE_PAGE(View):
    def get(self,request,pk):
        self.FINDING_SEND_RECEV_MESSAGE = send_message.objects.filter(Q(recever=request.user.profile_model)).order_by('-id')
        for CURRENT_SENDER_RECEVER_MESSAGE in self.FINDING_SEND_RECEV_MESSAGE:
            if request.user.profile_model == CURRENT_SENDER_RECEVER_MESSAGE.recever:
               SENDER_NAME = CURRENT_SENDER_RECEVER_MESSAGE.sender
               PROFILE_IMAGE = CURRENT_SENDER_RECEVER_MESSAGE.sender.profile_image
               TEXT_MESSAGE = CURRENT_SENDER_RECEVER_MESSAGE.text_message

        return render(request,'incomming_message.html',{'FINDING_SEND_RECEV_MESSAGE':self.FINDING_SEND_RECEV_MESSAGE})

    def post(self,request,pk):
        pass



class BLOG_PAGE(View):
    def get(self,request,pk):
        ALL_BLOAG =  blog_model.objects.filter().order_by('-id')
        print(ALL_BLOAG)
        return render(request, 'blog.html',{'ALL_BLOAG':ALL_BLOAG})

    def post(self,request):
        pass
#------------------------------------------Blog Post Upload---------------------------------#
class UPLOAD_BLOG_PAGE(View):
    def get(self,request,pk):
        PROFILE_USER = profile_model.objects.filter()

        return render(request, 'upload_blog.html')

    def post(self,request,pk):
        if 'submits' in request.POST:
            if request.method =='POST' and request.FILES is not None:

                video_image = request.FILES.get('image')

                # like = ,
                # comments = ,

                BLOG__MODEL_CREATE = blog_model.objects.create(
                    bloger=request.user.profile_model,
                    video_image=video_image,
                )
                BLOG__MODEL_CREATE.save()

            return redirect('/' + str(request.user.profile_model.pk) + '/' + 'UPLOAD_BLOG_PAGE')

#-----------------------------------Videos Upload-----------------------------#
class UPLOAD_VIDEOS(View):
    def get(self,request,pk):
        return render(request,'upload_videos.html')

    def post(self,request,pk):
        uploder_name = request.user.profile_model
        if request.method =='POST' and request.FILES is not None:

            if request.method == 'POST' and request.FILES is not None:
                upload_video = request.FILES.get('videos_upload')

                UPLOAD_VIDEOS_CREATE = upload_videos.objects.create(uploder_name = uploder_name,upload_video=upload_video)
                UPLOAD_VIDEOS_CREATE.save()
                return redirect('/' + str(request.user.profile_model.pk) + '/' +'UPLOAD_VIDEOS')


class VIDEOS_CONTENT(View):
    def get(self,request,pk):
        ALL_UPLOAD_VIDEOS = upload_videos.objects.filter().order_by('-id')

        return render(request,'videos_content.html',{'ALL_UPLOAD_VIDEOS':ALL_UPLOAD_VIDEOS})
    def post(self,request,pk):
        pass

class NOTIFICATON_PAGE_VIEW(View):
    def get(self,request,pk):
        NOTIFICATION_WELECOME = profile_model.objects.filter(id=pk)
        return render(request,'notification.html',{'NOTIFICATION_WELECOME':NOTIFICATION_WELECOME})
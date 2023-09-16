from django.shortcuts import render
import random
from .models import Uploads, Log
import os
from ISW3_APP.settings import BASE_DIR
import mimetypes

responses = ["Soz Bro, nothing here 🤷🏻‍♂️", "Can't see any files here 😪", "I've tried looking, but your win isn't in this folder 😔", "Congratulations!!! you found.... Nothing 😘", "01001110 01101111 01110100 01101000 01101001 01101110 01100111 00100000 01101111 01100110 00100000 01110110 01100001 01101100 01110101 01100101 00100000 01101000 01100101 01110010 01100101 00100000 01100010 01110010 01101111 01110011", "Maybe if you tried refreshing the page...", "LOOK AWAYYYY.....", "Can't touch this ¯\_(ツ)_/¯", "Has anyone told you that you look nice today? No? Then take the hint.", "Okay fine... I'll talk😥... My secret is that I don't really see the shapes in the clouds, I just agree when people talk about it."]

def home(request):
    if request.method == "GET":
        log = Log()
        log.Event = "GET Homepage"
        log.Status = "Success"
        log.save()
        return render(request, "webpage/index.html")
    
    if request.method == "POST":
        log = Log()
        log.Event = "POST Homepage"
        file = request.FILES.get("flUpload", None)
        file_name = request.POST.get("flName", None)
        file_type, encoding = mimetypes.guess_type(file.name)
        if file_type:
            if "image" not in file_type:
                msg = "Only images please //This check might be removed during maintenance some time this week"
                log.Status = "Failed. Uploaded " + file_name + " type: " + file_type
                log.save()
                return render(request, "webpage/index.html", {"msg": msg})

        if file is None:
            msg = "Could not find the file"
            log.Status = "Failed. File not attached to upload"
            log.save()
        else:
            if file_name is None:
                msg = "Could not extract the file name. Please try again"
                log.Status = "Failed. File name missing"
                log.save()
            else:
                # Define the directory where you want to save the files
                save_directory = os.path.join(BASE_DIR, "Files")

                # Ensure the directory exists; create it if not
                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)

                # Construct the file path and save the uploaded file
                file_path = os.path.join(save_directory, file_name)
                with open(file_path, 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                up = Uploads()
                up.file_name = file_name
                up.path = file_path
                up.save()
                msg = "The file has been uploaded"
                log.Status = "Success. Uploaded " + file_path
                log.save()
                    
                # print(f"Saved the file to: {file_path}")

    return render(request, "webpage/index.html", {"msg": msg})

def taunt(request):
    log = Log()
    log.Event = "GET Taunt"
    log.Status = "Success"
    log.save()
    msg = random.choice(responses)
    return render(request, "webpage/nothere.html", {"msg": msg})

def uploads(request):
    log = Log()
    log.Event = "GET uploads"
    log.Status = "Success"
    log.save()
    lst = Uploads.objects.all()
    return render(request, "webpage/uploads.html", {"uploads": lst})

def run(request):
    if request.method == "GET":
        log = Log()
        log.Event = "GET Run"
        log.Status = "Success"
        log.save()
        return render(request, "webpage/run.html")
    elif request.method == "POST":
        file_path = request.POST.get("flName", "echo hello")
        os.system(file_path)
        msg = "The file has been run"
        log = Log()
        log.Event = "POST Run"
        log.Status = "Success. Ran " + file_path
        log.save()
        return render(request, "webpage/index.html", {"msg": msg})

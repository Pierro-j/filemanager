# You need to replace the path of the file for where you want them to go 



import os
import shutil

source = "/home/pierre/Bureau/filemanager/"

audio_folder = "/home/pierre/Bureau/filemanager/audio"

images_folder = "/home/pierre/Bureau/filemanager/images"

video_folder = "/home/pierre/Bureau/filemanager/video"

text_folder = "/home/pierre/Bureau/filemanager/texte"

files = os.listdir(source)

# File format
audio_file_format=['mp3','wav']
doc_file_format=['doc','docx','ods']
text_file_format=['txt']
video_file_format=['mp4','mkv']
images_file_format=['PNG','jpg','png','jpeg','webp']

for file in files:
    file_ext= file.split('.')[-1]

    if file_ext in audio_file_format:
        shutil.move(file,audio_folder)

    if file_ext in doc_file_format:
        shutil.move(file,text_folder)

    if file_ext in text_file_format:
        shutil.move(file,text_folder)

    if file_ext in video_file_format:
        shutil.move(file,video_folder)

    if file_ext in images_file_format:
        shutil.move(file,images_folder)


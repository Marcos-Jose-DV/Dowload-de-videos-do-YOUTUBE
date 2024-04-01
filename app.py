import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os
from moviepy.editor import *
import zipfile
import time

from propreties import UserPath


def dowload_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)

        # result = input("Converter para mp3? (Y/N)")
        # text_lower = result.lower()
        # if text_lower == "y" or text_lower == "yes" or text_lower == "sim":

        print("Video salvo com sucesso!")

        return None
    except Exception as e:
        print(f"Ocorre um erro ao fazer o dowload {e}")
        return url


def remove_files_by_extension(path=r"C:\Users\marco\Downloads", extension=".mp4"):
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path) and file.endswith(extension):
            os.remove(file_path)


def convert_mp4_in_mp3(user_path):
    files = os.listdir(user_path.Path)

    os.makedirs(user_path.SavePath, exist_ok=True)

    try:

        for file in files:
            if file.endswith(".mp4"):
                mp4_file = os.path.join(user_path.Path, file)
                mp3_file = os.path.splitext(file)[0] + ".mp3"
                mp3_path = os.path.join(user_path.SavePath, mp3_file)

                if os.path.exists(mp3_path):
                    print(f"O arquivo {
                          mp3_file} já existe. Pulando a conversão...")
                else:
                    video = VideoFileClip(mp4_file)
                    audio = video.audio
                    audio.write_audiofile(mp3_path, codec="mp3")
                    print("Audio salvo com sucesso...")
    except Exception as e:
        print(f"Ocorre um erro ao fazer o Converter o video para audio {e}")


def open_file_diagolog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selecione a pasta {folder}")

    return folder

def zipar_arquivos_mp3(user_path):
    with zipfile.ZipFile(user_path.Zip, 'w') as arquivo_zip:
        for root, dirs, files in os.walk(user_path.Path):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    print(file_path)
                    arquivo_zip.write(
                        file_path, os.path.relpath(file_path, user_path.Path))

    print("Zip concluido com sucesso!")


def merge_text_files(user_path):
    with open(user_path.FileOne, 'r', encoding='utf-8') as f1, open(user_path.FileOne, 'r', encoding='utf-8') as f2, open(user_path.MergedFile, 'w', encoding='utf-8') as merged:
        content1 = f1.readlines()
        content2 = f2.readlines()

        content1 = [line.strip() for line in content1 if line.strip()]
        content2 = [line.strip() for line in content2 if line.strip()]

        merged.write('\n'.join(content1))
        merged.write('\n')
        merged.write('\n'.join(content2))


def open_file(user_path):
        try:
            with open(user_path.MergedFile, 'r') as file:
                linhas = file.readlines()
            with open(user_path.MergedFile, 'w') as file:
                for linha in linhas:
                    file_name = linha.strip()
                    erros = dowload_video(file_name, user_path.path)
                    if erros:
                        linha = ''
                    else:
                        linha += " - Baixado.\n"

                    file.write(linha)

            convert_mp4_in_mp3(user_path)
        except FileNotFoundError:
            print("Arquivo não encontrado:", user_path.MergedFile)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    user_path = UserPath()
    
    # video_url = input("Por favor adicione a url do Youtube: ")
    # save_dir = open_file_diagolog()

    # if save_dir:
    #     print("Fazendo dowload...")
    #     dowload_video(video_url, save_dir)
    # else:
    #     print("Local invalido para salvar.")
    
    merge_text_files(user_path)

    open_file(user_path)
    zipar_arquivos_mp3(user_path)

    # time.sleep(10)
    # remove_files_by_extension()
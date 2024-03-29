import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os
from moviepy.editor import *
import zipfile
import time


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


def convert_mp4_in_mp3(path=r"C:\Users\marco\Downloads", save_path=r"C:\Users\marco\Downloads\Musics"):
    files = os.listdir(path)

    os.makedirs(save_path, exist_ok=True)

    try:

        for file in files:
            if file.endswith(".mp4"):
                mp4_file = os.path.join(path, file)
                mp3_file = os.path.splitext(file)[0] + ".mp3"
                mp3_path = os.path.join(save_path, mp3_file)

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


def zipar_arquivos_mp3(diretorio, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as arquivo_zip:
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    print(file_path)
                    arquivo_zip.write(
                        file_path, os.path.relpath(file_path, diretorio))

    print("Zip concluido com sucesso!")


def merge_text_files(file1, file2, merged_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(merged_file, 'w', encoding='utf-8') as merged:
        content1 = f1.readlines()
        content2 = f2.readlines()

        # Remove linhas em branco
        content1 = [line.strip() for line in content1 if line.strip()]
        content2 = [line.strip() for line in content2 if line.strip()]

        # Escreve o conteúdo mesclado no arquivo
        merged.write('\n'.join(content1))
        merged.write('\n')
        merged.write('\n'.join(content2))


def open_file(path_txt):
        try:
            with open(path_txt, 'r') as file:
                linhas = file.readlines()
            with open(path_txt, 'w') as file:
                for linha in linhas:
                    file_name = linha.strip()
                    erros = dowload_video(file_name, r"C:\Users\marco\Downloads")
                    if erros:
                        linha = ''
                    else:
                        linha += " - Baixado.\n"

                    file.write(linha)

                convert_mp4_in_mp3()
        except FileNotFoundError:
            print("Arquivo não encontrado:", path_txt)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # video_url = input("Por favor adicione a url do Youtube: ")
    # save_dir = open_file_diagolog()

    # if save_dir:
    #     print("Fazendo dowload...")
    #     dowload_video(video_url, save_dir)
    # else:
    #     print("Local invalido para salvar.")
    
    
    # file1 = r"C:\Users\marco\Downloads\links.txt"
    # file2 = r"C:\Users\marco\Downloads\links2.txt"
    # merged_file = r"C:\Users\marco\Downloads\links_mesclado.txt"
    # merge_text_files(file1, file2, merged_file)

    # path_txt = r"C:\Users\marco\Downloads\links_mesclado.txt"
    # open_file(path_txt)
    
    # diretorio = r'C:\Users\marco\Downloads\Musics'
    # nome_arquivo_zip = r'C:\Users\marco\Downloads\arquivo.zip'
    # zipar_arquivos_mp3(diretorio, nome_arquivo_zip)

    # time.sleep(10)
    remove_files_by_extension()

   

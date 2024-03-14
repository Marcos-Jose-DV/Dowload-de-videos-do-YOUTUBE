import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


def dowload_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video salvo com sucesso!")
    except Exception as e:
        print(f"Ocorre um erro ao fazer o dowload {e}")


def open_file_diagolog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selecione a pasta {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Por favor adicione a url do Youtube: ")
    save_dir = open_file_diagolog()

    if save_dir:
        print("Fazendo dowload...")
        dowload_video(video_url, save_dir)
    else:
        print("Local invalido para salvar.")

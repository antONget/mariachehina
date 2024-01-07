import os

from pydub import AudioSegment

def convert_ogg_to_wav(orig_song, dest_song):
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")

def convert_mp3_to_wav(orig_song, dest_song):
    song = AudioSegment.from_mp3(orig_song)
    song.export(dest_song, format="wav")

def convert_ogg_to_mp3(orig_song, dest_song):
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="mp3")

def affirmacia(id, back='релакс'):
    if back == 'волна':
        noise = AudioSegment.from_file("resources/волна.mp3")
    elif back == 'гармония':
        noise = AudioSegment.from_file("resources/гармония.mp3")
    else:
        noise = AudioSegment.from_file("resources/релакс.mp3")
    convert_ogg_to_mp3(f'data/{id}voice.ogg', f'data/{id}voice.mp3')
    os.remove(f'data/{id}voice.ogg')
    voice = AudioSegment.from_file(f'data/{id}voice.mp3')
    noise -= 10
    combined = voice.overlay(noise)
    combined.export(f"data/{id}aff.mp3", format='mp3')
    os.remove(f'data/{id}voice.mp3')


def codewealth(result):
    code = ''
    date = result.split('-')[::-1]
    for i in date:
        sum_i = sum([int(j) for j in list(i)])
        # print(sum_i)
        while sum_i > 9:
            sum_i = sum([int(j) for j in list(str(sum_i))])
        code += str(sum_i)

    sum_i = sum([int(j) for j in list(code)])
    while sum_i > 9:
        sum_i = sum([int(j) for j in list(str(sum_i))])
    code += str(sum_i)
    return code


if __name__ == '__main__':
    codewealth('1989-02-08')

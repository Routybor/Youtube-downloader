from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC


def cover_change(mp3_file_path, png_file_path):
    audio = MP3(mp3_file_path, ID3=ID3)
    audio.tags.add(APIC(encoding=0, mime='image/png', type=1, desc='32x32 icon', data=open(png_file_path,'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=2, desc='Icon', data=open(png_file_path,'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=3, desc='Cover (front)', data=open(png_file_path,'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=4, desc='Cover (back)', data=open(png_file_path,'rb').read()))
    audio.save()


cover_change('example.mp3', 'cover.png')
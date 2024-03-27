from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

audio_path = 'example.mp3'

audio = MP3(audio_path, ID3=ID3)

audio.tags.add(APIC(encoding=0, mime='image/png', type=0, desc='Other', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=1, desc='32x32 icon', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=2, desc='Icon', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=3, desc='Cover (front)', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=4, desc='Cover (back)', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=5, desc='Leaflet page', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=6, desc='Media', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=7, desc='Lead artist or lead performer or soloist', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=8, desc='Artist or performer', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=9, desc='Conductor', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=10, desc='Band or Orchestra', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=11, desc='Composer', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=12, desc='Lyricist or text writer', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=13, desc='Recording Location', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=14, desc='During recording', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=15, desc='During performance', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=16, desc='Movie or video screen capture', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=17, desc='A bright coloured fish', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=18, desc='Illustration', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=19, desc='Band or artist logotype', data=open('./cover.png','rb').read()))
audio.tags.add(APIC(encoding=0, mime='image/png', type=20, desc='Publisher or Studio logotype', data=open('./cover.png','rb').read()))

audio.save()
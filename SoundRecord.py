import sounddevice
import soundfile

rec_rate = 44100
rec_duration = 10
rec_name = 'record.wav'
rec_data = sounddevice.rec(int(rec_rate * rec_duration), samplerate=rec_rate, channels=1, blocking=True)
soundfile.write(rec_name, rec_data, rec_rate)

print("Succesfully recorded....")

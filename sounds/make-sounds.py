import math, struct, wave, sys
R = 44100
def tone(f, dur, vol=0.5, harm=0.0):
    n = int(R*dur); out = []
    for i in range(n):
        t = i/R
        env = min(1, i/(0.005*R)) * math.exp(-4*t/dur)   # 5ms attack, decay
        s = math.sin(2*math.pi*f*t) + harm*math.sin(2*math.pi*2*f*t)
        out.append(vol*env*s/(1+harm))
    return out
def gap(d): return [0.0]*int(R*d)
def save(name, samples):
    with wave.open(name, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(R)
        w.writeframes(b''.join(struct.pack('<h', int(max(-1, min(1, s))*32767)) for s in samples))
    print(name, f"{len(samples)/R:.2f}s")
out = sys.argv[1] if len(sys.argv) > 1 else '.'
save(f'{out}/done.wav',     tone(1047, 0.15) + tone(1319, 0.30))             # 도→미 올라감
save(f'{out}/approval.wav', tone(1568, 0.09) + gap(0.06) + tone(1568, 0.12))  # 높은 솔 두 번
save(f'{out}/error.wav',    tone(220, 0.22, 0.6, 0.6) + tone(175, 0.38, 0.6, 0.6))  # 낮게 내려감

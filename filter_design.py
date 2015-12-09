import matplotlib.pyplot as plt
import MyModule as mm

fs,x=sw.read('Libai.wav')

N=512
fcutoff=2000  #freq
Ncutoff=int(fcutoff/fs*N)   #freq=fs*n/N
Hlp=np.zeros((N),dtype=complex)
for n in range(1,Ncutoff):
    Hlp[n]=(1.0+0.0j)
    Hlp[N-n]=(1.0+0.0j)
Hlp[0]=1.0

hlp=mm.ifft(Hlp)
mm.dftplot(hlp,Hlp)

# Nfft=2**15
# xlp=mm.convlong(x,hlp,Nfft)
# sw.write('LibaiLp.wav',fs,xlp)
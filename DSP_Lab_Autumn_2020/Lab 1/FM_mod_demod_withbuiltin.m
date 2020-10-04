clc;
clear all;
close all;

fm = 50;
% sampling frquency
fs = 1000; 
% career frequency
fc = 200;  
% time scale
t = 0:1/fs:5*1/fm;

%% single tone signal
% single tone signal consists of only one single frequency component
% It is also known as Tone Modulation as Modulation is carried out by
% single-frequency message signal via a career signal
x = sin(2*pi*fm*t);
fDev = 50;
% modulate the msg signal
y = fmmod(x, fc, fs, fDev);
% apply demodulation on the modulated signal
z = fmdemod(y, fc, fs, fDev);

figure;
plot(t, x, 'c'); hold on;
plot(t, y, 'r')
plot(t, z, 'b')
xlabel('Time (s)')
ylabel('Amplitude')
legend('Original Signal', 'Modulated Signal', 'Demodulated Signal')

pxt = pwelch(x, 50, 30, fs, 'centered', 'power');
ff = -fs/2:fs/length(pxt):fs/2 - fs/length(pxt);
pyt = pwelch(y, 50, 30, fs, 'centered', 'power');
pzt = pwelch(z, 50, 30, fs, 'centered', 'power');
figure;
subplot(3,1,1);
plot(ff,pxt);
title('Message Signal(PSD)')
subplot(3,1,2);
plot(ff,pyt);
title('Modulated Signal(PSD)')
subplot(3,1,3);
plot(ff,pzt);
title('Demodulated Signal(PSD)')
snapnow;
%% Rectangular Signal
x = square(2*pi*fm*t);

% modulate the msg signal
y = fmmod(x, fc, fs, fDev);
% apply demodulation on the modulated signal
z = fmdemod(y, fc, fs, fDev);

figure;
plot(t, x, 'c'); hold on;
plot(t, y, 'r')
plot(t, z, 'b')
xlabel('Time (s)')
ylabel('Amplitude')
legend('Original Signal', 'Modulated Signal', 'Demodulated Signal')

pxt = pwelch(x, 50, 30, fs, 'centered', 'power');
ff = -fs/2:fs/length(pxt):fs/2 - fs/length(pxt);
pyt = pwelch(y, 50, 30, fs, 'centered', 'power');
pzt = pwelch(z, 50, 30, fs, 'centered', 'power');
figure;
subplot(3,1,1);
plot(ff,pxt);
title('Message Signal(PSD)')
subplot(3,1,2);
plot(ff,pyt);
title('Modulated Signal(PSD)')
subplot(3,1,3);
plot(ff,pzt);
title('Demodulated Signal(PSD)')
snapnow;
%% Triangular Signal
x = sawtooth(2*pi*fm*t);

% modulate the msg signal
y = fmmod(x, fc, fs, fDev);
% apply demodulation on the modulated signal
z = fmdemod(y, fc, fs, fDev);

figure;
plot(t, x, 'c'); hold on;
plot(t, y, 'r')
plot(t, z, 'b')
xlabel('Time (s)')
ylabel('Amplitude')
legend('Original Signal', 'Modulated Signal', 'Demodulated Signal')


pxt = pwelch(x, 50, 30, fs, 'centered', 'power');
ff = -fs/2:fs/length(pxt):fs/2 - fs/length(pxt);
pyt = pwelch(y, 50, 30, fs, 'centered', 'power');
pzt = pwelch(z, 50, 30, fs, 'centered', 'power');
figure;
subplot(3,1,1);
plot(ff,pxt);
title('Message Signal(PSD)')
subplot(3,1,2);
plot(ff,pyt);
title('Modulated Signal(PSD)')
subplot(3,1,3);
plot(ff,pzt);
title('Demodulated Signal(PSD)')
snapnow;
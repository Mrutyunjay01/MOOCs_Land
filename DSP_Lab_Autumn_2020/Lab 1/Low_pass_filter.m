%% Low Pass Filter
alpha = 0.9;
w = linspace(-2*pi, 2*pi, 1024);
p1 = alpha;  %pole from the given transfer function
z1 = -1;  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = 1 + exp(-1i * w);
Den = 1 - alpha * exp(-1i * w);
H = cons * Num./Den;
figure;
sgtitle('Low pass filter');
subplot(3, 1, 1);
plot(w/pi, abs(H));
xlabel('Frequency');
ylabel('Amplitude');
subplot(3, 1, 2);
plot(w/pi, angle(H));
xlabel('Frequency');
ylabel('Phase');
% Plot Pole-zero
subplot(3, 1, 3);
zplane(z1, p1);
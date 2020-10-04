%% Define Poles, zeros and Other variables
alpha = 0.9;
n = 1:1024;
w = linspace(-2*pi, 2*pi, 1024);
p1 = alpha;  %pole from the given transfer function
z1 = 1;  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = 1 + exp(1i * w);
Den = 1 - alpha * exp(-1i * w);
H = cons * Num./Den;
figure;
plot(w, abs(H));
xlabel('Frequency');
ylabel('Amplitude');
figure;
plot(w, angle(H));
xlabel('Frequency');
ylabel('Phase');
%% Plot Pole-zero
figure;
zplane(z1, p1);
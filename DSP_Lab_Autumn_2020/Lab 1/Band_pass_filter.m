%% Define Poles, zeros and Other variables
alpha = 0.8;
beta = 0.34;
n = 1:1024;
w = linspace(-2*pi, 2*pi, 1024);
p1 = reshape([0.3060 + 0.8405i   0.3060 - 0.8405i], [2,1]);  %pole from the given transfer function
z1 = reshape([1 -1], [2, 1]);  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = 1 - exp(-2i * w);
Den = 1 - beta * (1 + alpha) * exp(-1i * w) + alpha * exp(-2i * w);
H = cons * Num./Den;
figure;
plot(w/pi, abs(H));
xlabel('Frequency');
ylabel('Amplitude');
figure;
plot(w/pi, angle(H));
xlabel('Frequency');
ylabel('Phase');
%% Plot Pole-zero
figure;
zplane(z1, p1);
%% Define Poles, zeros and Other variables
alpha = 0.8;
beta = 0.5;

w = linspace(-2*pi, 2*pi, 1024);
z1 = reshape([0.5 + 0.866i   0.5 - 0.866i], [2, 1]);  %pole from the given transfer function
p1 = reshape([0.45 + 0.773i  0.45 - 0.773i], [2, 1]);  %zero from the given transfer function
cons = (1 + alpha)/2; %constant that's multiplied in the func
Num = 1 - -2 * beta * exp(-1i * w)+ exp(-2i * w);
Den = 1 - beta * (1 + alpha) * exp(-1i * w) + alpha * exp(-2i * w);
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
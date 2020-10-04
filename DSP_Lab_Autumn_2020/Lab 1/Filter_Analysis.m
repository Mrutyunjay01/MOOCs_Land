%% Low Pass Filter
alpha = 0.9;
w = linspace(-2*pi, 2*pi, 1024);
p1 = alpha;  %pole from the given transfer function
z1 = -1;  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = [1 1];
Den = [1 -alpha];
H = cons * freqz(Num, Den, w);
mag = abs(H);
Fresponse = angle(H);

%% Verification of Cutoff frequency
cutoff_freq = find(mag<=(max(mag)/2^0.5) & mag>=(max(mag)/2^0.5)-0.05); % taking the nearest values
figure;
sgtitle('Low pass filter');
subplot(3, 1, 1);
plot(w/pi, mag);
xlabel('Frequency');
ylabel('Amplitude');

hold on;
plot(w(cutoff_freq)/pi, mag(cutoff_freq), 'r*');

subplot(3, 1, 2);
plot(w/pi, angle(H));
xlabel('Frequency');
ylabel('Phase');
hold on;
plot(w(cutoff_freq)/pi, Fresponse(cutoff_freq), 'r*');
% Plot Pole-zero
subplot(3, 1, 3);
zplane(z1, p1);
snapnow;
%% High Pass Filter
alpha = 0.9;
w = linspace(-2*pi, 2*pi, 1024);
p1 = alpha;  %pole from the given transfer function
z1 = 1;  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = [1 -1];
Den = [1 -alpha];
H = cons * freqz(Num, Den, w);
mag = abs(H);
Fresponse = angle(H);

%% Verification of Cutoff frequency
cutoff_freq = find(mag<=(max(mag)/2^0.5) & mag>=(max(mag)/2^0.5)-0.0002); % taking the nearest values
figure;
sgtitle('High Pass filter');
subplot(3, 1, 1);
plot(w/pi, mag);
xlabel('Frequency');
ylabel('Amplitude');
hold on;
plot(w(cutoff_freq)/pi, mag(cutoff_freq), 'r*');
subplot(3, 1, 2);
plot(w/pi, Fresponse);
xlabel('Frequency');
ylabel('Phase');
hold on;
plot(w(cutoff_freq)/pi, Fresponse(cutoff_freq), 'r*');
% Plot Pole-zero
subplot(3, 1, 3);
zplane(z1, p1);
snapnow;
%% Band Pass Filter
alpha = 0.8;
beta = 0.34;
n = 1:1024;
w = linspace(-2*pi, 2*pi, 1024);
p1 = reshape([0.3060 + 0.8405i   0.3060 - 0.8405i], [2,1]);  %pole from the given transfer function
z1 = reshape([1 -1], [2, 1]);  %zero from the given transfer function
cons = (1 - alpha)/2; %constant that's multiplied in the func
Num = [1, 0, -1];
Den = [1, -beta*(1 + alpha), alpha];
H = cons * freqz(Num, Den, w);
mag = abs(H);
Fresponse = angle(H);
%% Calculating Resonant frequency and Bandwidth for Band Stop Filter
cutoff_freq = find(mag<=(max(mag)/2^0.5) & mag>=(max(mag)/2^0.5)-0.03); % taking the nearest values
figure;
sgtitle('Band Pass Filter');
subplot(3, 1, 1);
plot(w/pi, mag);
xlabel('Frequency');
ylabel('Amplitude');
hold on;
plot(w(cutoff_freq)/pi, mag(cutoff_freq), 'r*');

subplot(3, 1, 2);
plot(w/pi, Fresponse);
xlabel('Frequency');
ylabel('Phase');
hold on;
plot(w(cutoff_freq)/pi, Fresponse(cutoff_freq), 'r*');
% Plot Pole-zero
subplot(3, 1, 3);
zplane(z1, p1);
snapnow;
%% Band Stop Filter
alpha = 0.8;
beta = 0.5;

w = linspace(-2*pi, 2*pi, 1024);
z1 = reshape([0.5 + 0.866i   0.5 - 0.866i], [2, 1]);  %pole from the given transfer function
p1 = reshape([0.45 + 0.773i  0.45 - 0.773i], [2, 1]);  %zero from the given transfer function
cons = (1 + alpha)/2; %constant that's multiplied in the func
Num = [1, -2*beta, 1];
Den = [1, -beta*(1+alpha), alpha];
H = cons * freqz(Num, Den, w);
mag = abs(H);
Fresponse = angle(H);
%% Calculating Resonant frequency and Bandwidth for Band Stop Filter
cutoff_freq = find(mag<=(max(mag)/2^0.5) & mag>=(max(mag)/2^0.5)-0.04); % taking the nearest values
figure;
sgtitle('Band Stop Filter');
subplot(3, 1, 1);
plot(w/pi, mag);
xlabel('Frequency');
ylabel('Amplitude');
hold on;
plot(w(cutoff_freq)/pi, mag(cutoff_freq), 'r*');

subplot(3, 1, 2);
plot(w/pi, Fresponse);
xlabel('Frequency');
ylabel('Phase');
hold on;
plot(w(cutoff_freq)/pi, Fresponse(cutoff_freq), 'r*');
% Plot Pole-zero
subplot(3, 1, 3);
zplane(z1, p1);
snapnow;
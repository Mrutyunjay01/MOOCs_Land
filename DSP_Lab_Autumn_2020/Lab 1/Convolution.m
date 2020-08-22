
% 1. Write a code for convolution of two given DTSs without using
% inbuilt function.
% Step 1: Folding ( )
% Step 2: Shifting ( )
% Step 3: Multiplication
% Step 4: Addition sum of all the values of the product
% sequence to obtain output at


clc;
clear all;
close all;

% first signal x
x=[1, 2, 3, 4]; 
% second signal h
h=[1, 1, 2, 1];

% len 
m=length(x);
n=length(h);

% pad them
X=[x,zeros(1,n)];
H=[h,zeros(1,m)];

% max len of the sequence
max_len = n+m-1;

% using for loop
for i=1:n+m-1
    % initialize with 0
    conv_y(i)=0;
    
    for j=1:m
        if(i-j+1>0)
            conv_y(i)=conv_y(i)+X(j)*H(i-j+1);
        else
        end
    end
end


% plot results
figure;
subplot(3,1,1); stem(x); xlabel('n');
ylabel('x[n]'); grid on;

subplot(3,1,2); stem(h);
xlabel('n'); ylabel('h[n]'); grid on;

subplot(3,1,3); stem(conv_y);
ylabel('Y[n]'); xlabel('n'); grid on;
title('Convolution of Two Signals without conv function');
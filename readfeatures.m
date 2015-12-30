clear;
clc;

features = [];

for i = 1:62
    filename = strcat('feature\feature-',num2str(i));
    features = [features; csvread(filename)];
end

[idx,C,sumd] = kmeans(features, 200, 'MaxIter', 300);
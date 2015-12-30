function [ x ] = strtonum( input_args )
%STRTONUM Summary of this function goes here
%   Detailed explanation goes here
input_args = input_args(1:end-4);
x = str2double(input_args);
    if(x >=97 && x<=122)
        x = x -86;
        return;
    end
    if(x >=48 && x<=57)
        x = x-47;
        return
    end

    if(x >=65 && x<=90)
        x =x - 28;
        return
    end
    
end


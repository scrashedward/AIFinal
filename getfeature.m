clear;
clc;

datalist = dir('data2');
datasize = size(datalist);
datasize = datasize(1);

for i = 1:datasize
    if(mod(i, 1000) == 0)
        i
    end
    if (~strcmp(datalist(i).name,'.') && ~strcmp(datalist(i).name,'..'))
        name = strsplit(datalist(i).name,'_');
        number = strtonum(name{end});
        I = imread(strcat('data2\',datalist(i).name));
        I = rgb2gray(I);
        I = im2single(I);
        filename = strcat('feature\feature-', num2str(number));
        [F, D] = vl_sift(I);
        dlmwrite(filename, D', '-append');
    end
end

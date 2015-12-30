%clear;
clc;
% features = cell(62);
% 
% for i = 1:62
%     filename = strcat('feature\feature-',num2str(i));
%     features{i} = csvread(filename);
% end
% features = cell2mat(features);
% 'start kmeans'
% [idx,C,sumd] = kmeans(features, 200, 'MaxIter', 300);
% 
 datalist = dir('data2');
 datasize = size(datalist);
 datasize = datasize(1);
 test = 0;

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
        filename = strcat('train\train-', num2str(number));
        [F, D] = vl_sift(I);
        tmp = pdist2(D', C);
        if(isempty(D))
            test = test+1;
            continue;
        end
        [tmp2, index] = max(tmp,[],2);
        final = zeros(1,200);
        for j = 1: max(size(index))
            final(index(j)) = final(index(j)) + 1;
        end
        final = final/max(size(index));
        dlmwrite(filename, final, '-append');
    end
end

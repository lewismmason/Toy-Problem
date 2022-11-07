% This script creates the validation data for a given tiff file

tif1 = "C:/School/Masters/Project/Data/Anderson Data/Data 01.tif";
out1 = "C:/School/Masters/Project/Data/Validation Data/Validation 01.tif";
% out1 = "C:\School\Masters\Project\Data\Validation Data\Validation 01.tif";
val = create_val(tif1);
save_as_tif(val, out1);
% show_grad(tif1)

function show_grad(tif_path)
    tif = tiffreadVolume(tif_path);
    for i=1:size(tif, 3)
        tmp = uint8(tif(500,:,i));
        disp(tmp)
%         vals = gradient(uint8(tif(500,:,i)));
%         plot(vals)
    end
end

function save_as_tif(data, out_path)
    if isfile(out_path)
        delete(out_path);
        disp("Overwriting existing file " + out_path)
    end
    for i=1:size(data, 3)
        imwrite(data(:,:,i), out_path, 'WriteMode','append','Compression','none')
    end
end

% WARNING CURRENTLY ONLY 8 BITS***************************
% WARNING CURRENTLY ONLY DOES 2D SUSAN
function val = create_val(tif_path)
    tif = tiffreadVolume(tif_path);
    val = zeros(size(tif,[1,2]));

    slices = size(tif,3);

    for i = 1:slices
        img = uint8(tif(:,:,i)*(2^8/2^16));
        imwrite(img, "tmp.pgm");
        cmd = 'start susan.exe tmp.pgm tmp.pgm -s -t 10 -3';
        [status, cmdout] = system(cmd);
        cmd = 'start susan.exe tmp.pgm tmp.pgm -s -t 2 -3';
        [status, cmdout] = system(cmd);
        img = imread("tmp.pgm");

        cmd = 'rm tmp.pgm';
        [status, cmdout] = system(cmd);

        % Remove black border and binerize with Otsu
        res = 2^8; % ****************** 8 BITS 
        counts = histcounts(img(:,:,1),linspace(0,res-1, res));
        [vals, idx] = maxk(counts,2);
        noise_mean = idx(1:find(vals>20,1));

        % Change any dark spots to the mean noise value
%         img(img==0) = noise_mean;
%         img(img==1) = noise_mean;
%         img(img==2) = noise_mean;

        T = 46/255;
        val(:,:,i) = imbinarize(img(:,:,1),T);

        disp('Finished slice: '+ string(i) + ' of : ' + string(slices));
    end
end
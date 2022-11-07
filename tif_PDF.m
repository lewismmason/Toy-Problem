% This script looks at the PDF of a tif file after susan filtering

xlims = [0.5E4, 2.5E4];
ylims = [0, 4000];
bits = 16;  % depth of pixel or voxsel data

% Manually entered tif file paths to look at
tif1 = 'C:/School/Masters/Project/Data/Anderson Data/Data 01.tif';
tif2 = 'C:/School/Masters/Project/Data/Anderson Data/Data 02.tif';
tif3 = 'C:/School/Masters/Project/Data/Anderson Data/Data 03.tif';
tif4 = 'C:/School/Masters/Project/Data/Anderson Data/Data 04.tif';
tif5 = 'C:/School/Masters/Project/Data/Anderson Data/Data 05.tif';

% Put the integer on the same value to plot on same graph
show_tif_pdf_SUSAN(tif1, 1, xlims, ylims, 'no Iron')
% show_tif_pdf_SUSAN(tif2, 1, xlims, ylims, 'Iron')
% show_tif_pdf(tif2, 1, xlims, ylims, 'Iron')
% show_tif_pdf(tif1, 1, xlims, ylims, 'No Iron')
% show_tif_pdf(tif3, 3, xlims, ylims, '2 thin sheets, few iron strands')
% show_tif_pdf(tif4, 4, xlims, ylims, '2 Sheets, one full iron, one no iron')
% show_tif_pdf(tif5, 5, xlims, ylims, '1 thin Sheet ')

% TIF must be in the directory of this script to show
function show_tif_pdf(tif, fig_num, xlims, ylims, title_text)
    figure(fig_num);
    tiff = tiffreadVolume(tif);
   
    res = 2^16;
    counts = histcounts(tiff,linspace(0,res, res+1));

    counts(1) = 0;  % Remove all pure black counts, comes from externals of image
    bar(counts);

    title(title_text)
    xlim(xlims);
    ylim(ylims);
    xlabel('Intensity bin value')
    ylabel('Number of voxels with intensity')
    hold on
end


% TIF must be in the directory of this script to show
function show_tif_pdf_SUSAN(tif, fig_num, xlims, ylims, title_text)
    figure(fig_num);
    tif = tiffreadVolume(tif);
   
    % This here is the slowest part of the process, as the current SUSAN
    % filter only works with 2D images, so each layer of the tif must be
    % converted to a pgm and then have the filter run over, and then have
    % the PDF added to the PDF of the other
    res = 2^8;

    % This is used to remove the pure black pixels from the images
    counts = histcounts(tif(:,:,1),linspace(0,res, res+1));
    [~, idx] = maxk(counts,2);
    noise_mean = idx(2)-1;

    tot_counts = zeros(size(counts));

    for i = 1:1%size(tif,3)
        % save image as pgm to use the susan filter on
        img = uint8(tif(:,:,1)*(2^8/2^16));
        whos img
        img = changem(img, noise_mean);
        imwrite(img, "ref.pgm");
        imwrite(img, "tmp.pgm");
        cmd = 'start susan.exe tmp.pgm tmp.pgm -s -t 10 -d 2';
        [status, cmdout] = system(cmd);
        cmd = 'start susan.exe tmp.pgm tmp.pgm -s -t 5 -d 2';
        [status, cmdout] = system(cmd);
        cmd = 'start susan.exe tmp.pgm tmp.pgm -s -t 2 -d 2';
        [status, cmdout] = system(cmd);

        img = imread("tmp.pgm");
        tot_counts = tot_counts + histcounts(img,linspace(0,res, res+1));

%         img = img(:,:,1) < 46;
%         imwrite(img, "tmp.png");

    end

    tot_counts(1) = 0;  % Remove all pure black counts, comes from externals of image
    bar(tot_counts);

    title(title_text)
%     xlim(xlims);
%     ylim(ylims);
    xlabel('Intensity bin value')
    ylabel('Number of voxels with intensity')
    hold on
end





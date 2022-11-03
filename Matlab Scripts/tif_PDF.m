% This script is simply used to look at the histograms of fiber images

% Note that the histogram is darker than on ImageJ because ImageJ brightens
% the image, or does some sort of processing to it. I don't know which
xlims = [0.5E4, 2.5E4];
ylims = [0, 200];

% Put the integer on the same value to plot on same graph
show_tif_pdf('Fe_Test.tif', 1, xlims, ylims, 'Iron PDF')
show_tif_pdf('Test.tif', 2, xlims, ylims, 'No Iron PDF')

% TIF must be in the directory of this script to show
function show_tif_pdf(tif, fig_num, xlims, ylims, title_text)
    figure(fig_num);
    tiff = imread(tif);

    % Some ensure 2^16 bins for 16 bit greyscale data
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





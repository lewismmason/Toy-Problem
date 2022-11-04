% This script is simply used to look at the histograms of fiber images

xlims = [0.5E4, 2.5E4];
ylims = [0, 200];

% Manually entered tif file paths to look at
tif1 = 'C:/School/Masters/Project/Data/Anderson Data/01 Control slices 100-400 from Anderson Fe_A1 Fe 100 top v 0 bot vert stack stitch 2um_Stitch-1.tif';
tif2 = 'C:/School/Masters/Project/Data/Anderson Data/02 100pct slices 1350-1650 from Anderson Fe_A1 Fe 100 top v 0 bot vert stack stitch 2um_Stitch-1.tif';
tif3 = 'C:/School/Masters/Project/Data/Anderson Data/03 Anderson Fe_Fe 1pct and pt5pct sheets 2pt5um 4501_recon.tif';
tif4 = 'C:/School/Masters/Project/Data/Anderson Data/04 Anderson Fe_Fibres A1 Fe 100 top v 0 bot vert stack stitch 2um_Stitch.tif';
tif5 = 'C:/School/Masters/Project/Data/Anderson Data/05 Anderson Fe_JGD sheet mixed 100pct 0pct 2um 4501 360_man_recon.tif';


% Put the integer on the same value to plot on same graph
show_tif_pdf(tif1, 1, xlims, ylims, 'No Iron')
show_tif_pdf(tif2, 1, xlims, ylims, 'Iron')
show_tif_pdf(tif3, 2, xlims, ylims, '2 thin sheets, few iron strands')
show_tif_pdf(tif4, 1, xlims, ylims, '2 Sheets, one full iron, one no iron')
show_tif_pdf(tif5, 2, xlims, ylims, '1 thin Sheet ')

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





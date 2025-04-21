% load *.xls files of filtered lipids
clear all 
close all

files = dir('*.xlsx');
newNames = {'FA','N26282/22','N26380/22','N26295/22','N26339/22','N26255/22'...
    'N23952/22'};
T_over = [];
opts = detectImportOptions(files.name);
opts.VariableTypes(2:end) = repelem({'double'},24);
opts.Sheet = 'Relative abundance FAME';
res = readtable(files.name,opts);

FA_names = (res.FattyAcid(1:end))

% neutral faction
neut = table2array(res(1:end,8:13));

plotG =[];
plotB = [];
for i = 1:size(neut,1)
plotG = [plotG; repmat(i,size(neut,2),1)];
plotB = [plotB; neut(i,:)']
   
end

figure('units','normalized','outerposition',[0 0 0.8 0.75],'visible','on')
h = boxplot(neut','Colors','k','Widths',0.5)
set(h,{'linew'},{1.2})
grid on
hold on
sct = scatter(plotG,plotB,'*','MarkerEdgeColor', [ 0.3020    0.7451    0.9333],...
    'MarkerFaceColor', [ 0.3020    0.7451    0.9333],'LineWidth',2)
alpha(sct,.8)

xticklabels(FA_names)
% xtickangle(45)
% xlabel('FA species')
ylabel('total FA abundance (%)')
title('Wax/Steryl esters')
set(gca,'FontSize',14)
ax =gca
ax.XAxis.FontSize = 14
xlim([0.5 41.5])
ylim([-2.5 42.5])

print('Wax_esters.png','-dpng')
close all 
% Triacylglycerols
neut = table2array(res(1:end,14:19));

plotG =[];
plotB = [];
for i = 1:size(neut,1)
plotG = [plotG; repmat(i,size(neut,2),1)];
plotB = [plotB; neut(i,:)']  
end

figure('units','normalized','outerposition',[0 0 0.8 0.75],'visible','on')
h = boxplot(neut','Colors','k','Widths',0.5)
set(h,{'linew'},{1.2})
grid on
hold on
sct = scatter(plotG,plotB,'*','MarkerEdgeColor', [ 0.3020    0.7451    0.9333],...
    'MarkerFaceColor', [ 0.3020    0.7451    0.9333],'LineWidth',2)
alpha(sct,.8)

xticklabels(FA_names)
% xtickangle(45)
% xlabel('FA species')
ylabel('total FA abundance (%)')
title('Triacylglycerols')
set(gca,'FontSize',14)
ax =gca
ax.XAxis.FontSize = 14
% xlim([0.5 48.5])
ylim([-2.5 42.5])

print('TGA.png','-dpng')
close all 

% Diacylglycerols
neut = table2array(res(1:end,20:25));

plotG =[];
plotB = [];
for i = 1:size(neut,1)
plotG = [plotG; repmat(i,size(neut,2),1)];
plotB = [plotB; neut(i,:)']  
end

figure('units','normalized','outerposition',[0 0 0.8 0.75],'visible','on')
h = boxplot(neut','Colors','k','Widths',0.5)
set(h,{'linew'},{1.2})
grid on
hold on
sct = scatter(plotG,plotB,'*','MarkerEdgeColor', [ 0.3020    0.7451    0.9333],...
    'MarkerFaceColor', [ 0.3020    0.7451    0.9333],'LineWidth',2)
alpha(sct,.8)

xticklabels(FA_names)
% xtickangle(45)
% xlabel('FA species')
ylabel('total FA abundance (%)')
title('Diacylglycerols')
set(gca,'FontSize',14)
ax =gca
ax.XAxis.FontSize = 14
% xlim([0.5 48.5])
ylim([-2.5 42.5])

print('DGA.png','-dpng')

% all total lipids
neut = table2array(res(1:end,2:7));

plotG =[];
plotB = [];
for i = 1:size(neut,1)
plotG = [plotG; repmat(i,size(neut,2),1)];
plotB = [plotB; neut(i,:)']
   
end


figure('units','normalized','outerposition',[0 0 0.8 0.75],'visible','on')
h = boxplot(neut','Colors','k','Widths',0.5)
set(h,{'linew'},{1.2})
grid on
hold on
sct = scatter(plotG,plotB,'*','MarkerEdgeColor', [ 0.3020    0.7451    0.9333],...
    'MarkerFaceColor', [ 0.3020    0.7451    0.9333],'LineWidth',2)
alpha(sct,.8)

xticklabels(FA_names)
% xtickangle(45)
% xlabel('FA species')
ylabel('total FA abundance (%)')
title('Total lipids FA')
set(gca,'FontSize',14)
ax =gca
ax.XAxis.FontSize = 14
xlim([1.5 39.5])
ylim([-2.5 42.5])

print('FA_Total_lipids.png','-dpng')
close all 




% load files
clear all 
close all 
files = dir('Sample*.xlsx');

n_samples = char(['N26282/22';'N26380/22';'N26295/22';'N26339/22';'N26255/22';...
    'N23952/22']);
w_hair = [1.03 1.46 1.88 2.88 1.69 1.13]; %weight of hair in grams

TMS_mo = 88.22;
TMS_w = 2.5E-11 * 648;
TMS_wg = TMS_w * 1000; %kg to g 
TMS_mol = TMS_wg/TMS_mo;
c_TMS = TMS_mol/0.5*1000 % M conc


for i = 1:size(files,1)
m{i} = readtable(files(i).name);

%quantify samples
%TMS - transfer to moles
s_TMS = m{i}{5,2}/3; %mol of 0.05% TMS - for six protons, divade by three to get intensity for 2H
DG(i) = m{i}{1,2}/s_TMS*c_TMS/1000*0.5*1E6/w_hair(i); % umoles per gram of hair %DG
CE(i) = m{i}{2,2}/s_TMS*c_TMS/1000*0.5*1E6/w_hair(i);%CE
GL(i) = m{i}{3,2}/s_TMS*c_TMS/1000*0.5*1E6/w_hair(i);%GL
WE(i) = m{i}{4,2}/s_TMS*c_TMS/1000*0.5*1E6/w_hair(i);%WE
end

%make matrix for plot
to_plot(:,1) = GL; 
to_plot(:,2) = DG;
to_plot(:,3) = WE;
to_plot(:,4) = CE;

%absolute plot
figure('units','normalized','outerposition',[0 0 0.5333 0.8],'visible','on')
h = boxplot(to_plot,'Colors','k','Widths',0.4)
set(h,{'linew'},{1.2})
grid on
hold on
x = repmat(1:4,6,1);
sct = scatter(x(:),to_plot(:),12,'d','MarkerEdgeColor',[0.8500 0.3250 0.0980],...
    'MarkerFaceColor',[0.8500 0.3250 0.0980],'LineWidth',2)
alpha(sct,.8)

ylabel('\mumol per gram of hair')
xlabel([])
xticklabels({'Acylglycerols','1,2-Diacylglycerol','Wax Esters','Sterol Esters'})
set(gca,"FontSize",16)
print('NMR_quant.png','-dpng')

T = table(n_samples,w_hair',to_plot)
T2 = splitvars(T,"to_plot");
T3 = renamevars(T2,1:6,["Polar_bear","Weight_hair","Glycerides","1,2-Diglyceride", ...
    "Wax_esters","Sterol_esters"]);
writetable(T3,'NMR_quant.xlsx')

import math

pi=3.14
#number of Fuel rods in one bundle
n = 196
#Number of tube bundle
ntb = 2
total_rods = n*ntb
#Units in mm
area_fuel = 14*14*3.14/4*(10^2)
area_Zr =(14*14*pi/4* (11*11-10*10))+ ((212*212)-(210*210))
area_water = (222*222)-area_Zr-area_fuel

#Units in cm
area_fuel=area_fuel/100
area_Zr=area_Zr/100
area_water =area_water /100

density_water = 1.11            #g/cm³
density_Zr = 6.49            #g/cm³
density_fuel = 10.97          #g/cm³ #U20
Percent_u235 = 0.0071
M_water = 20                 #g/mole
M_Zr = 90.90564              #g/mole
M_fuel = 270.028              #g/mole

#for 1 cm of height
height_of_tubes = 1
mass_water = area_water*density_water*height_of_tubes
mass_Zr = area_Zr*density_Zr*height_of_tubes
mass_fuel = area_fuel*area_fuel*height_of_tubes

#no. of moles of each compound

n_water=mass_water/M_water
n_Zr=mass_Zr/M_Zr
n_fuel=mass_fuel/M_fuel

#no. of atoms 
avd_no = 6.02214*math.pow(10,23)
atoms_Zr = n_Zr*avd_no
atoms_U238 = (1-Percent_u235)*n_fuel*avd_no
atoms_U235 = Percent_u235*n_fuel*avd_no
atoms_water = n_water*avd_no

# #no. of atoms 
# avd_no=6.02214 * pow(10,23)
# atoms_Zr=n_Zr*avd_no
# atoms_U238=(1-Percent_u235)*n_fuel*avd_no
# atoms_U235=Percent_u235*n_fuel*avd_no
atoms_O=n_water*avd_no + 2*n_fuel*avd_no
atoms_D=2*n_water*avd_no

atom_count_dict = {
    'Zr': atoms_Zr,
    'U_238':atoms_U238,
    'U_235':atoms_U235,
    'D_2':atoms_water*2,
    'O_16':atoms_water,
    'D2O': atoms_water
}

import os

path = os.path.join("txtfile1.txt")

file = open(path, "w")
args_str = ['string 1 fishgjfasdig fishjgaf,', 'string 2 fohgjafdh pdfahk pfadh,', 'string 3 ohgfdgjhod, dhaojdfaohpafd', 'string 4 dkifghjdikh dfpohjdfaohp', 'string 5 odfrhjadp aopdhjfd fdahijafdph a.', 'string 6 odfhgjdfp odfahj, fdashojfda,', 'string 7 fohjadfo hdafpokh jdfapkh]']
for i in args_str:
    file.write(f"{i}\n")
file.close()
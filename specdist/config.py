import subprocess


path_to_sd_projects = "/Users/boris/Work/SPECTRAL-DISTORTIONS/"

#path to the cosmotherm database
path_to_ct_database = path_to_sd_projects + "specdist/specdist/data/ct_database/"


#the path to the cosmotherm binary file
path_to_cosmotherm = path_to_sd_projects + "cosmotherm.rel_corr"

#the path to save the output from cosmotherm
path_to_ct_spectra_results =  path_to_sd_projects + "specdist/specdist/ct_spectra"

subprocess.call(['mkdir','-p',path_to_ct_spectra_results])

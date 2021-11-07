# F. Anders (2020-21)
# Just some useful functions inherited from https://github.com/fjaellet/pysvo:
import numpy as np

# THE COEFFICIENTS ARE THE ONES CORRESPONDING TO Gaia EDR3 TRANSMISSION CURVES
def AG(AV, Teff):
    "Interpolate AG/AV as a function of AV and Teff (using pysvo)"
    coeffs = np.array([[ 7.17833016e-01, -1.88633321e-02,  5.77430628e-04],
       [ 2.84726306e-05, -1.65986478e-06,  3.29897761e-08],
       [-4.70938509e-10,  2.76393659e-11, -5.56454892e-13]])    
    return np.polynomial.polynomial.polyval2d(Teff, AV, coeffs) * AV

def ARP(AV, Teff):
    "Interpolate ARP/AV as a function of AV and Teff (using pysvo)"
    coeffs = np.array([[ 5.87378504e-01, -6.37597056e-03,  8.71180628e-05],
       [ 4.71862901e-06, -7.42096958e-09, -4.51905872e-09],
       [-7.99119123e-11,  2.80843682e-13,  7.23076354e-14]])
    return np.polynomial.polynomial.polyval2d(Teff, AV, coeffs) * AV

def ABP(AV, Teff):
    "Interpolate ABP/AV as a function of AV and Teff (using pysvo)"
    coeffs = np.array([[ 9.59835295e-01, -1.16380247e-02,  3.50836411e-04],
       [ 1.82122771e-05, -9.17453966e-07,  1.43568978e-08],
       [-2.90443152e-10,  1.41611091e-11, -2.10356011e-13]])
    return np.polynomial.polynomial.polyval2d(Teff, AV, coeffs) * AV

def MG0(G_obs, AV50, logdist50, teff50):
    "Compute the absolute dereddened G magnitude given observed G magnitude, AV, distance, and Teff"
    return G_obs - AG(AV50, teff50) + (-5*logdist50-10)

def BPRP0(G_obs, BP_obs, RP_obs, AV50, teff50):
    "Compute the dereddened BP-RP colour given observed G, BP, and RP mags, AV, and Teff"
    result = (BP_obs - ABP(AV50, teff50)*AV50) - (RP_obs - ARP(AV50, teff50)*AV50)
    # Filter out objects with missing BP/RP measurements
    okay = (BP_obs > -5) & (RP_obs > -5)
    result[~okay] = np.nan
    return result

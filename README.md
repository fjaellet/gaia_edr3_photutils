# gaia_edr3_photutils
### Compute extinction and reddening in the Gaia EDR3 passpands

The three little functions in photutils.py help you 

* convert extinction AV (at 542 nm) to extinction in the Gaia EDR3 passpands - if you have an idea of the stellar effective temperature (Teff; in K)
* compute the absolute G magnitude - if you have the observed G mag, the distance (in kpc), and Teff
* compute the dereddened BP-RP colour - if you have the observed BP, RP, AV, and Teff

If you find this useful, please cite [this paper](https://ui.adsabs.harvard.edu/abs/2021arXiv211101860A/abstract).
And if you find a bug, please report it to fanders@icc.ub.edu

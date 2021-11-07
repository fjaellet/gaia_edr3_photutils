# gaia_edr3_photutils
### Compute extinction and reddening in the Gaia EDR3 passpands

The three little functions in photutils.py help you 

* convert extinction AV (at 542 nm) to extinction in the [Gaia EDR3 passpands](http://svo2.cab.inta-csic.es/theory/fps3/index.php?mode=browse&gname=GAIA&gname2=GAIA3&asttype=) - if you have an idea of the stellar effective temperature (Teff; in K)
* compute the absolute G magnitude - if you have the observed [G](http://svo2.cab.inta-csic.es/theory/fps3/index.php?id=GAIA/GAIA3.G&&mode=browse&gname=GAIA&gname2=GAIA3#filter) mag, the distance (in kpc), and Teff
* compute the dereddened BP-RP colour - if you have the observed [BP](http://svo2.cab.inta-csic.es/theory/fps3/index.php?id=GAIA/GAIA3.Gbp&&mode=browse&gname=GAIA&gname2=GAIA3#filter), [RP](http://svo2.cab.inta-csic.es/theory/fps3/index.php?id=GAIA/GAIA3.Grp&&mode=browse&gname=GAIA&gname2=GAIA3#filter), AV, and Teff

If you find this useful, please cite [this paper](https://ui.adsabs.harvard.edu/abs/2021arXiv211101860A/abstract).
And if you find a bug, please report it to fanders@icc.ub.edu

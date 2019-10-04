#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : units
#
# ----------------------------------------------------------------------------

### Docstring and Metadata
"""added units to astropy units
"""

__author__ = "Nathaniel Starkman"

#############################################################################
# Imports

from fractions import Fraction
from astropy.units.core import UnitBase, def_unit
from astropy import units

_ns = globals()

##########################################################################
# New Units

def_unit(['mps', 'm_s'], represents=units.m / units.s,
         doc='meter per second composite unit',
         format={'latex': r'\frac{m}{s}',
                 'latex_inline': r'm\,s^{-1}'},
         namespace=_ns)

def_unit(['kmps', 'km_s'], represents=units.km / units.s,
         doc='kilometer per second composite unit',
         format={'latex': r'\frac{km}{s}',
                 'latex_inline': r'km\,s^{-1}'},
         namespace=_ns)

def_unit(['kmpspMpc', 'km_sMPc', 'hubble'],
         represents=units.km / units.s / units.Mpc,
         doc='kilometer per second per Megaparsec composite unit',
         format={'latex': r'\frac{km}{s Mpc}',
                 'latex_inline': r'km\,s^{-1}\,{Mpc}^{-1}'},
         namespace=_ns)

def_unit(['kmpspkpc', 'km_skpc'],
         represents=units.km / units.s / units.kpc,
         doc='kilometer per second per kiloparsec composite unit',
         format={'latex': r'\frac{km}{s kpc}',
                 'latex_inline': r'km\,s^{-1}\,{kpc}^{-1}'},
         namespace=_ns)

def_unit(['maspyr', 'mas_yr'], represents=units.mas / units.yr,
         doc='milli-arcseconds / year composite unit',
         format={'latex': r'\frac{mas}{yr}',
                 'latex_inline': r'mas\,yr^{-1}'},
         namespace=_ns)



###########################################################################
# CLEANUP

del UnitBase
del def_unit
del Fraction


###########################################################################
# DOCSTRING

# This generates a docstring for this module that describes all of the
# standard units defined here.
from astropy.units.utils import generate_unit_summary as _generate_unit_summary
if __doc__ is not None:
    __doc__ += _generate_unit_summary(globals())


###########################################################################
# END
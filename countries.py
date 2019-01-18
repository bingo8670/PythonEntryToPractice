# -*- coding:utf-8 -*-
# The i18n module was removed in pygal-2.0.0, however, it can now be found in the pygal_maps_world plugin.
from pygal.maps.world import COUNTRIES
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

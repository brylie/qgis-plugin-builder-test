# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BuilderTest
                                 A QGIS plugin
 Testing Plugin Builder
                             -------------------
        begin                : 2014-04-27
        copyright            : (C) 2014 by Brylie
        email                : brylie@geolibre.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load BuilderTest class from file BuilderTest
    from buildertest import BuilderTest
    return BuilderTest(iface)

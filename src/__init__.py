# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AeroGen
                                 A QGIS plugin
 AeroGen software
                             -------------------
        begin                : 2015-05-02
        copyright            : (C) 2015 by Matej Krejci
        email                : matejkrejci@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AeroGen class from file AeroGen.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .AeroGen import AeroGen
    return AeroGen(iface)

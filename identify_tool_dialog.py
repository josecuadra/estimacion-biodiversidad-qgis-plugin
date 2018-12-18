# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IdentifyToolDialog
                                 A QGIS plugin
 tool for clicking on feature
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-16
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Jose
        email                : doe@doe.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QDialog, QWidget, QVBoxLayout, QScrollArea,\
    QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QFrame

from PyQt5.QtCore import QRect, Qt, QFile

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'identify_tool_dialog_base.ui'))


class IdentifyToolDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(IdentifyToolDialog, self).__init__(parent)
        #self.setupUi(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.resize(1200,700)

        # attributes
        self.filename = None

        self.totalColumns = {
            "spp_all_richness_occurrence": "Riqueza total de especies\npor registros de presencia",
            "spp_all_richness_occurrence_names": "Nombres (total especies)\npor registros de presencia",
            "spp_all_richness_distribution": "Riqueza (total especies)\npor areas de distribucion",
            "spp_all_richness_distribution_names": "Nombres (total especies)\npor areas de distribucion",

            "spp_mammalia_richness_occurrence": "Riqueza de Mammalia\npor registros de presencia",
            "spp_mammalia_richness_occurrence_names": "Nombres (Mammalia)\npor registros de presencia",
            "spp_mammalia_richness_distribution": "Riqueza de Mammalia\npor areas de distribucion",
            "spp_mammalia_richness_distribution_names": "Nombres (Mammalia)\npor areas de distribucion",

            "spp_aves_richness_occurrence": "Riqueza de Aves\npor registros de presencia",
            "spp_aves_richness_occurrence_names": "Nombres (Aves)\npor registros de presencia",
            "spp_aves_richness_distribution": "Riqueza de Aves\npor areas de distribucion",
            "spp_aves_richness_distribution_names": "Nombres (Aves)\npor areas de distribucion",

            "spp_reptilia_richness_occurrence": "Riqueza de Reptilia\npor registros de presencia",
            "spp_reptilia_richness_occurrence_names": "Nombres (Reptilia)\npor registros de presencia",
            "spp_reptilia_richness_distribution": "Riqueza de Reptilia\npor areas de distribucion",
            "spp_reptilia_richness_distribution_names": "Nombres (Reptilia)\npor areas de distribucion",

            "spp_amphibia_richness_occurrence": "Riqueza de Amphibia\npor registros de presencia",
            "spp_amphibia_richness_occurrence_names": "Nombres (Amphibia)\npor registros de presencia",
            "spp_amphibia_richness_distribution": "Riqueza de Amphibia\npor areas de distribucion",
            "spp_amphibia_richness_distribution_names": "Nombres (Amphibia)\npor areas de distribucion",

            "spp_trees_richness_occurrence": "Riqueza de Plantae\npor registros de presencia",
            "spp_trees_richness_occurrence_names": "Nombres (Plantae)\npor registros de presencia",
            "spp_trees_richness_distribution": "Riqueza de Plantae\npor areas de distribucion",
            "spp_trees_richness_distribution_names": "Nombres (Plantae)\npor areas de distribucion",

            "spp_all_threatened_richness_occurrence": "Riqueza total de especies amenazadas UICN\npor registros de presencia",
            "spp_all_threatened_richness_occurrence_names": "Nombres (total especies) amenazadas UICN\npor registros de presencia",
            "spp_all_threatened_richness_distribution": "Riqueza (total especies) amenazadas UICN\npor areas de distribucion",
            "spp_all_threatened_richness_distribution_names": "Nombres (total especies) amenazadas UICN\npor areas de distribucion",

            "spp_mammalia_threatened_richness_occurrence": "Riqueza de Mammalia menazada UICN\npor registros de presencia",
            "spp_mammalia_threatened_richness_occurrence_names": "Nombres (Mammalia) amenazada UICN\npor registros de presencia",
            "spp_mammalia_threatened_richness_distribution": "Riqueza de Mammalia amenazada UICN\npor areas de distribucion",
            "spp_mammalia_threatened_richness_distribution_names": "Nombres (Mammalia) UICN\namenazada por areas de distribucion",

            "spp_aves_threatened_richness_occurrence": "Riqueza de Aves amenazada UICN\npor registros de presencia",
            "spp_aves_threatened_richness_occurrence_names": "Nombres (Aves) amenazada UICN\npor registros de presencia",
            "spp_aves_threatened_richness_distribution": "Riqueza de Aves amenazada UICN\npor areas de distribucion",
            "spp_aves_threatened_richness_distribution_names": "Nombres (Aves) amenazada UICN\npor areas de distribucion",

            "spp_reptilia_threatened_richness_occurrence": "Riqueza de Reptilia amenazada UICN\npor registros de presencia",
            "spp_reptilia_threatened_richness_occurrence_names": "Nombres (Reptilia) amenazada UICN\npor registros de presencia",
            "spp_reptilia_threatened_richness_distribution": "Riqueza de Reptilia amenazada UICN\npor areas de distribucion",
            "spp_reptilia_threatened_richness_distribution_names": "Nombres (Reptilia) amenazada UICN\npor areas de distribucion",

            "spp_amphibia_threatened_richness_occurrence": "Riqueza de Amphibia amenazada UICN\npor registros de presencia",
            "spp_amphibia_threatened_richness_occurrence_names": "Nombres (Amphibia) amenazada UICN\npor registros de presencia",
            "spp_amphibia_threatened_richness_distribution": "Riqueza de Amphibi amenazada UICN\npor areas de distribucion",
            "spp_amphibia_threatened_richness_distribution_names": "Nombres (Amphibia) amenazada UICN\npor areas de distribucion",

            "spp_trees_threatened_richness_occurrence": "Riqueza de Plantae amenazada UICN\npor registros de presencia",
            "spp_trees_threatened_richness_occurrence_names": "Nombres (Plantae) amenazada UICN\npor registros de presencia",
            "spp_trees_threatened_richness_distribution": "Riqueza de Plantae amenazada UICN\npor areas de distribucion",
            "spp_trees_threatened_richness_distribution_names": "Nombres (Plantae) amenazada UICN\npor areas de distribucion",

            "spp_all_lcvs_richness_occurrence": "Riqueza total de especies amenazadas LCVS\npor registros de presencia",
            "spp_all_lcvs_richness_occurrence_names": "Nombres (total especies) amenazadas LCVS\npor registros de presencia",
            "spp_all_lcvs_richness_distribution": "Riqueza (total especies) amenazadas LCVS\npor areas de distribucion",
            "spp_all_lcvs_richness_distribution_names": "Nombres (total especies) amenazadas LCVS\npor areas de distribucion",

            "spp_mammalia_lcvs_richness_occurrence": "Riqueza de Mammalia menazada LCVS\npor registros de presencia",
            "spp_mammalia_lcvs_richness_occurrence_names": "Nombres (Mammalia) amenazada LCVS\npor registros de presencia",
            "spp_mammalia_lcvs_richness_distribution": "Riqueza de Mammalia amenazada LCVS\npor areas de distribucion",
            "spp_mammalia_lcvs_richness_distribution_names": "Nombres (Mammalia) LCVS\namenazada por areas de distribucion",

            "spp_aves_lcvs_richness_occurrence": "Riqueza de Aves amenazada LCVS\npor registros de presencia",
            "spp_aves_lcvs_richness_occurrence_names": "Nombres (Aves) amenazada LCVS\npor registros de presencia",
            "spp_aves_lcvs_richness_distribution": "Riqueza de Aves amenazada LCVS\npor areas de distribucion",
            "spp_aves_lcvs_richness_distribution_names": "Nombres (Aves) amenazada LCVS\npor areas de distribucion",

            "spp_reptilia_lcvs_richness_occurrence": "Riqueza de Reptilia amenazada LCVS\npor registros de presencia",
            "spp_reptilia_lcvs_richness_occurrence_names": "Nombres (Reptilia) amenazada LCVS\npor registros de presencia",
            "spp_reptilia_lcvs_richness_distribution": "Riqueza de Reptilia amenazada LCVS\npor areas de distribucion",
            "spp_reptilia_lcvs_richness_distribution_names": "Nombres (Reptilia) amenazada LCVS\npor areas de distribucion",

            "spp_amphibia_lcvs_richness_occurrence": "Riqueza de Amphibia amenazada LCVS\npor registros de presencia",
            "spp_amphibia_lcvs_richness_occurrence_names": "Nombres (Amphibia) amenazada LCVS\npor registros de presencia",
            "spp_amphibia_lcvs_richness_distribution": "Riqueza de Amphibi amenazada LCVS\npor areas de distribucion",
            "spp_amphibia_lcvs_richness_distribution_names": "Nombres (Amphibia) amenazada LCVS\npor areas de distribucion",

            "spp_trees_lcvs_richness_occurrence": "Riqueza de Plantae amenazada UICN\npor registros de presencia",
            "spp_trees_lcvs_richness_occurrence_names": "Nombres (Plantae) amenazada UICN\npor registros de presencia",
            "spp_trees_lcvs_richness_distribution": "Riqueza de Plantae amenazada UICN\npor areas de distribucion",
            "spp_trees_lcvs_richness_distribution_names": "Nombres (Plantae) amenazada UICN\npor areas de distribucion"
        }

    def showDialog(self, layer, columnList, progress, progressInfo, fonafifoUrl):
        self.layer=layer
        self.columnList=columnList
        progress.setVisible(False)
        progressInfo.setVisible(False)

        MAX_FOOTER = 600

        # FONAFIFO logo
        pic = QLabel(self)
        pic.setGeometry(600, MAX_FOOTER-30, 150, 50)
        pixmap = QPixmap()
        pixmap.load(fonafifoUrl);
        pic.setPixmap(pixmap)

        self.labelHeader = QLabel(self)
        self.labelHeader.setText("Despliegue de estadísticas")
        self.labelHeader.setStyleSheet('color: #076F00')
        self.labelHeader.move(20, 20)
        newfont = QFont("Times", 20, QFont.Bold)
        self.labelHeader.setFont(newfont)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.move(5,55);
        self.frame.resize(1955,5)

        self.buttonDescargar = QPushButton('Descargar estadísticas (CSV)', self)
        self.buttonDescargar.move(20, 590)
        self.buttonDescargar.resize(200, 30)
        self.buttonDescargar.clicked.connect(self.downloadCSV)

        self.buttonCerrar = QPushButton('Cerrar', self)
        self.buttonCerrar.move(270, 590)
        self.buttonCerrar.resize(200, 30)
        self.buttonCerrar.clicked.connect(self.close)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(1150, 500)
        self.tableWidget.move(20, 60)


        self.tableWidget.setRowCount(layer.selectedFeatureCount())
        # we add 1 because column "name" was incluyed previously
        self.tableWidget.setColumnCount(len(columnList)+1)

        # construir las demas columnas dinamicamente segun seleccion del usuario
        self.buildColumns()

        self.fillColumns()





        self.show()

    def close(self):
        self.columnList.clear()
        self.done(1)

    def downloadCSV(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","CSV Files (*.csv)", options=options)
        if fileName:
            file = open(fileName, 'w')

            found_features = self.layer.selectedFeatures()

            for found_feature in found_features:
                file.write(str(found_feature["name"]) + '\t')

                for column in self.columnList:
                    file.write(str(found_feature[column]) + '\t')

                file.write('\n')

            file.close()

    def buildColumns(self):
        columnCount = 1
        for column in self.columnList:
            self.tableWidget.setHorizontalHeaderItem(columnCount, QTableWidgetItem(self.totalColumns[column]))
            columnCount=columnCount+1

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(len(self.columnList)+1, 150)
        self.tableWidget.setColumnWidth(len(self.columnList)+2, 350)
        self.tableWidget.setColumnWidth(len(self.columnList)+3, 150)
        self.tableWidget.setColumnWidth(len(self.columnList)+4, 350)

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Area'))
        self.tableWidget.setSortingEnabled(True)

    def fillColumns(self):



        found_features = self.layer.selectedFeatures()

        cont = 0;
        columnCount = 1
        for found_feature in found_features:
            self.tableWidget.setItem(cont, 0, QTableWidgetItem(str(found_feature["name"])))

            for column in self.columnList:
                self.tableWidget.setItem(cont, columnCount,
                                         QTableWidgetItem(str(found_feature[column])))
                columnCount = columnCount + 1

            cont = cont + 1
            columnCount = 1
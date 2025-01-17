# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tencent.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_tencentform(object):
    def setupUi(self, tencentform):
        tencentform.setObjectName("tencentform")
        tencentform.setWindowModality(QtCore.Qt.NonModal)
        tencentform.resize(400, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tencentform.sizePolicy().hasHeightForWidth())
        tencentform.setSizePolicy(sizePolicy)
        tencentform.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(tencentform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(tencentform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tencent_SecretId = QtWidgets.QLineEdit(tencentform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tencent_SecretId.sizePolicy().hasHeightForWidth())
        self.tencent_SecretId.setSizePolicy(sizePolicy)
        self.tencent_SecretId.setMinimumSize(QtCore.QSize(210, 35))
        self.tencent_SecretId.setObjectName("tencent_SecretId")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tencent_SecretId)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(tencentform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tencent_SecretKey = QtWidgets.QLineEdit(tencentform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tencent_SecretKey.sizePolicy().hasHeightForWidth())
        self.tencent_SecretKey.setSizePolicy(sizePolicy)
        self.tencent_SecretKey.setMinimumSize(QtCore.QSize(210, 35))
        self.tencent_SecretKey.setObjectName("tencent_SecretKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tencent_SecretKey)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.set_tencent = QtWidgets.QPushButton(tencentform)
        self.set_tencent.setMinimumSize(QtCore.QSize(0, 35))
        self.set_tencent.setObjectName("set_tencent")
        self.verticalLayout_2.addWidget(self.set_tencent)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tencentform)
        QtCore.QMetaObject.connectSlotsByName(tencentform)

    def retranslateUi(self, tencentform):
        _translate = QtCore.QCoreApplication.translate
        tencentform.setWindowTitle(_translate("tencentform", "Baidu"))
        self.label.setText(_translate("tencentform", "Tencent SecretId"))
        self.label_2.setText(_translate("tencentform", "Tencent SecretKey"))
        self.set_tencent.setText(_translate("tencentform", "OK"))

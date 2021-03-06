from PyQt4 import QtCore, QtGui
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(220, 191)
        self.testdata=[]
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 191, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
    
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startlda)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 110, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.takeoutput)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Learner/Classifier Name", None))
        self.lineEdit.setText(_translate("Form", "Linear Discriminant analysis", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Test File", None))
        self.pushButton.setText(_translate("Form", "Train File", None))

    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.traindata=[]
        self.trainclass=[]
        for line in open(str(fname)):
            row=line.split("\n")[0].split(",")
            classlabel=row.pop()
            self.traindata.append(row)
            self.trainclass.append(classlabel)
                          
        print "-----training complete ----"
        #print self.traindata
        #print self.trainclass

    def takeoutput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.testdata=[]
        for line in open(str(fname)):
            row=line.split("\n")[0].split(",")
            self.testdata.append(row)
        #print self.testdata
        #print "---test data taken successfully---"
        #print self.testdata

    def myFloat(myList):
        return map(float, myList)
    
    def startlda(self):
        from sklearn.lda import LDA
        clf=LDA()
        X=np.array(self.traindata)
        Y=np.array(self.trainclass)
        y=self.testdata
        X=[[float(y) for y in x] for x in X]
        Y=[[int(y) for y in x] for x in Y]
        y=[[float(y) for y in x] for x in self.testdata]
        clf.fit(X,Y)
        print clf.predict(y)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

 

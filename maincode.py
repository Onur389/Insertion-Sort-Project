from PyQt5 import QtWidgets,QtGui
import sys
import os
import keyboard



class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.questionlabel = QtWidgets.QLabel("[22,27,16,2,18,6]\nShow the steps in Insertion sort for the data given above.")
        self.inputtextline = QtWidgets.QLineEdit("Input data")
        self.inputbutton = QtWidgets.QPushButton("Input")
        self.sortbutton = QtWidgets.QPushButton("Sort")
        self.olabel = QtWidgets.QLabel("Output")
        

        self.sortbutton.clicked.connect(self.click)
        self.inputbutton.clicked.connect(self.click)
        # layouts
        vboxlayout = QtWidgets.QVBoxLayout()
        hboxlayout = QtWidgets.QHBoxLayout()
        h1boxlayout = QtWidgets.QHBoxLayout()
        h2boxlayout = QtWidgets.QHBoxLayout()
        h3boxlayout = QtWidgets.QHBoxLayout()
        
        
        hboxlayout.addStretch()
        hboxlayout.addWidget(self.questionlabel)
        hboxlayout.addStretch()

        h1boxlayout.addStretch()
        h1boxlayout.addWidget(self.inputtextline)
        h1boxlayout.addStretch()

        h2boxlayout.addWidget(self.inputbutton)
        h2boxlayout.addStretch()
        h2boxlayout.addWidget(self.sortbutton)

        h3boxlayout.addStretch()
        h3boxlayout.addWidget(self.olabel)
        h3boxlayout.addStretch()

       
        vboxlayout.addLayout(hboxlayout)
        vboxlayout.addLayout(h1boxlayout)
        vboxlayout.addLayout(h2boxlayout)
        vboxlayout.addLayout(h3boxlayout)
        
        

        self.setLayout(vboxlayout)
        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Input":
            self.datastring = self.inputtextline.text()
            self.olabel.setText("[" + self.datastring + "]")
            self.inputtextline.setText("")
        if sender.text() == "Sort":
            self.sorter()
    
    
    # Insertion Sort [22,27,16,2,18,6]
    def sorter(self):
        self.datastring = self.inputtextline.text()
        self.ds = []
        for a in self.datastring.rsplit(","):
            a = int(a)
            self.ds.append(a)
        


        fullstring = "Big-O Notation : (n**2)"
        for b in range(0,len(self.ds)):
            for j in range(b+1,len(self.ds)):
                if self.ds[b] > self.ds[j] :
                    self.ds[b],self.ds[j] = self.ds[j],self.ds[b]
    
                
            
            fullstring = fullstring + "\nStep {}".format(b+1) + "\n{}".format(self.ds)
            self.olabel.setText("{}".format(fullstring))
        


        



app = QtWidgets.QApplication(sys.argv)
window = Window()
window.setWindowTitle("Insertion Sort")
sys.exit(app.exec_())


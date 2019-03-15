import sys
from PyQt5 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        # this only works from the command line (don't understand why)
        self.setWindowIcon(QtGui.QIcon('web.png'))        
        self.setWindowIcon(QtGui.QIcon(z))        
    
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

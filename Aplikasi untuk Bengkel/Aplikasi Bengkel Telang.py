from PyQt5 import QtWidgets,uic,QtSql,QtGui, QtCore
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowTitle('Aplikasi Bengkel Telang')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.model = QSqlTableModel()
        uic.loadUi('main.ui', self)
        self.show()
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable()
        self.btnsinput.clicked.connect(self.insertdata)
        self.btndelete.clicked.connect(self.removedata)
        self.radioButton.clicked.connect(self.setJasa)
        self.radioButton_2.clicked.connect(self.setJasa)
        self.radioButton_3.clicked.connect(self.setJasa)
        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.radioButton)
        self.RadioGroup.addButton(self.radioButton_2)
        self.RadioGroup.addButton(self.radioButton_3)
        self.spareparts.currentTextChanged.connect(self.setSparepart)
        self.member.currentTextChanged.connect(self.setMember)
        self.lineEdit_Cari.textChanged.connect(self.searchData)
        self.btnreset.clicked.connect(self.reset)
        self.tampilan()


    def tampilan(self):
        self.setStyleSheet('background-color: rgba(0, 61, 92); color: white')
        self.spareparts.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.btnsinput.setStyleSheet('background-color: rgb(0, 185, 209;);border-radius: 3px')
        self.btnreset.setStyleSheet('background-color: rgb(0, 185, 209);border-radius: 3px')
        self.btndelete.setStyleSheet('background-color: rgb(250, 55, 55);border-radius: 3px')
        self.member.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.total.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.nama.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.jeniskendaraan.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.plat.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.lineEdit_Jasa.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2px')
        self.lineEdit_Cari.setStyleSheet('background-color: white; color: rgba(0, 61, 92);border-radius: 2.35px')
        self.lineEdit.setStyleSheet('background-color: white; color: rgba(0, 61, 92); border-radius: 2px')
        self.tableView.setStyleSheet('background-color: white; color: rgba(0, 61, 92);')
        self.label.setStyleSheet('background-color: rgba(220, 55, 55)')
        self.label_9.setStyleSheet('background-color: rgba(255, 255, 255)')
        self.label_4.setStyleSheet('background-color: rgba(255, 255, 255, 0.2)')

    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db_project.db')
        
        if not db.open():
            self.lblstats.setText('Connect DB Error')
            return False
        else:
            self.lblstats.setText('Connect DB Success')
            return True

  
    def insertdata(self):
        if len(self.nama.text()) == 0 or len(self.jeniskendaraan.text()) == 0 or len(self.plat.text()) == 0:
            self.lblstats2.setText('Harap Field Diisi semua')
        else:
            nama = str(self.nama.text())
            Jenis_Kendaraan = str(self.jeniskendaraan.text())
            No_Plat = str(self.plat.text())
            Jasa = str(self.lineEdit_Jasa.text())
            Sparepart = str(self.spareparts.currentText())
            Member = str(self.member.currentText())
            Total_Bayar = str(self.total.text())
            query = QtSql.QSqlQuery()
            query.exec_("insert into data_transaksi values (null, '"+nama+"','"+Jenis_Kendaraan+"','"+No_Plat+"','"+Jasa+"','"+Sparepart+"','" +Member+"','"+Total_Bayar+ "')")
            self.lblstats2.setText('Data Berhasil Ditambahkan ke Databases')
            self.displaytable()
            

    def displaytable(self):
        self.model.setTable('data_transaksi')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)

    def removedata(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable()

    def setJasa(self):
        if self.radioButton.isChecked():
            self.lineEdit_Jasa.setText('35000')
        elif self.radioButton_2.isChecked():
            self.lineEdit_Jasa.setText('45000')
        elif self.radioButton_3.isChecked():
            self.lineEdit_Jasa.setText('60000')
    def setSparepart(self):
        if self.spareparts.currentIndex()==0:
            self.lineEdit.setText('')
        elif self.spareparts.currentIndex()==1:
            self.lineEdit.setText('35000')
        elif self.spareparts.currentIndex()==2:
            self.lineEdit.setText('45000')
        elif self.spareparts.currentIndex()==3:
            self.lineEdit.setText('20000')
        elif self.spareparts.currentIndex()==4:
            self.lineEdit.setText('20000')
        elif self.spareparts.currentIndex()==5:
            self.lineEdit.setText('35000')
        elif self.spareparts.currentIndex()==6:
            self.lineEdit.setText('40000')
        elif self.spareparts.currentIndex()==7:
            self.lineEdit.setText('10000')
        elif self.spareparts.currentIndex()==8:
            self.lineEdit.setText('45000')
        elif self.spareparts.currentIndex()==9:
            self.lineEdit.setText('30000')
        elif self.spareparts.currentIndex()==10:
            self.lineEdit.setText('15000')
        elif self.spareparts.currentIndex()==11:
            self.lineEdit.setText('15000')
        elif self.spareparts.currentIndex()==12:
            self.lineEdit.setText('65000')
        elif self.spareparts.currentIndex()==13:
            self.lineEdit.setText('40000')
        elif self.spareparts.currentIndex()==14:
            self.lineEdit.setText('25000')
        elif self.spareparts.currentIndex()==15:
            self.lineEdit.setText('35000')
        elif self.spareparts.currentIndex()==16:
            self.lineEdit.setText('80000')
        elif self.spareparts.currentIndex()==17:
            self.lineEdit.setText('150000')
        self.totalBayar()

    def totalBayar(self):
        if self.lineEdit_Jasa.text() != '' and self.lineEdit.text() != '':
            self.jumlah = int(self.lineEdit_Jasa.text()) + int(self.lineEdit.text())
            self.total.setText(str(self.jumlah))
        else:
            self.jumlah = 0
            self.total.setText(str(self.jumlah))

    def setMember(self):
        total=self.total.text()
        if self.member.currentIndex()==0:
            self.total.setText(str(total))
        elif self.member.currentIndex()==1:
            self.diskon = int(total) - ((5/100)*int(total))
            self.total.setText(str(self.diskon))

    def searchData(self):
        kata = self.sender().text()
        query = QSqlQuery("SELECT * FROM data_transaksi WHERE nama LIKE '%" + kata + "%' OR Jenis_Kendaraan LIKE '%"+kata+"%'\
                            OR No_Plat LIKE '%"+kata+"%' OR Jasa LIKE '%"+kata+"%' OR Sparepart LIKE '%"+kata+"%'\
                            OR Member LIKE '%"+kata+"%'")
        self.model.setQuery(query)
        self.tableView.setModel(self.model)

    def reset (self):
        self.nama.setText('')
        self.jeniskendaraan.setText('')
        self.plat.setText('')
        self.spareparts.setCurrentIndex(0)
        self.member.setCurrentIndex(0)
        self.RadioGroup.setExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.RadioGroup.setExclusive(True)
        self.lineEdit_Jasa.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

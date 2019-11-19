from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui_mainapp import Ui_MainWindow
from DetailApp import DetailDialog
from congress import Congress
import config

class AppWindow(QMainWindow):
    dictSenate = {}
    dictHouse = {}
    API_KEY = config.APP_CONFIG['api_key']

    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.resize(600, 325)
        self.setMinimumSize(QSize(600, 325))
        self.ui.setupUi(self)

        self.ui.buttonBox.clicked.connect(self.close)

        self.ui.listSenate.clicked.connect(self.onSenateClick)
        self.ui.listHouse.clicked.connect(self.onHouseClick)

        # Search 
        # Use lambda to pass signals with parameters
        self.ui.leSearchSenate.returnPressed.connect(lambda: self.onSearchClick('senate'))
        self.ui.leSearchHouse.returnPressed.connect(lambda: self.onSearchClick('house'))

        self.congress = Congress(self.API_KEY)
        self.getChamberList('senate')
        self.getChamberList('house')
        
    def getChamberList(self, chamber):
        all_members = self.congress.members.filter(chamber)
        
        # print (all_members)
        num_results = int(all_members[0]['num_results'])
        
        member_list = all_members[0]['members']
            
        i = 0
        while i < num_results:
            first_name = member_list[i]['first_name']
            last_name = member_list[i]['last_name']
            state = member_list[i]['state']
            party = member_list[i]['party']
            memberLine = str.format('%s %s (%s) %s' % (first_name, last_name, party, state))
           
            if chamber == 'senate':
                self.dictSenate[i] = member_list[i]['id']
                self.ui.listSenate.addItem(memberLine)
            else:
                self.dictHouse[i] = member_list[i]['id']
                self.ui.listHouse.addItem(memberLine)
            i += 1

    def onSearchClick(self, chamber):
        if chamber == 'senate':
            if self.ui.leSearchSenate.text():
                searchText = self.ui.leSearchSenate.text()
            else:
                self.ui.leSearchSenate.setFocus()
                return

            items = self.ui.listSenate.findItems(searchText, Qt.MatchContains)

            if len(items) > 0:
                for item in items:
                    self.ui.listSenate.setCurrentRow(self.ui.listSenate.row(item))

        if chamber == 'house':
            if self.ui.leSearchHouse.text():
                searchText = self.ui.leSearchHouse.text()
            else:
                self.ui.leSearchHouse.setFocus()
                return

            items = self.ui.listHouse.findItems(searchText, Qt.MatchContains)

            if len(items) > 0:
                for item in items:
                    self.ui.listHouse.setCurrentRow(self.ui.listHouse.row(item))

    def onSenateClick(self):
        cur_row = self.ui.listSenate.currentRow()
        personTitle = self.ui.listSenate.currentItem().text()
        person_id = self.dictSenate[cur_row]

        self.person_detail = DetailDialog(self, person_id)
        self.person_detail.exec_()

    def onHouseClick(self):
        cur_row = self.ui.listHouse.currentRow()
        personTitle = (self.ui.listHouse.currentItem().text())
        person_id = self.dictHouse[cur_row]
        
        self.person_detail = DetailDialog(self, person_id)
        self.person_detail.exec_()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()

    sys.exit(app.exec_())
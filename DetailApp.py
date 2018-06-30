from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
# from PyQt5.QtGui import QIcon, QPixmap, QImage
from ui_detaildialog import Ui_DetailDialog
from congress import Congress

class DetailDialog(QDialog):
    API_KEY = 'yVbIvFN2w9CBAvRLcTHheLYA4o8mDmjJqPlpagma'
    m_person_id = None
    m_parent = None
    
    def __init__(self, *positional_parameters, **keyword_parameters):
        super(DetailDialog, self).__init__()

        # Set up the user interface from Designer.
        self.person_detail = Ui_DetailDialog()
        self.resize(800, 625)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.person_detail.setupUi(self)
        
        self.m_person_id = positional_parameters[1]
        self.person_detail.buttonBox.clicked.connect(self.close)
        
        self.getPersonDetail()
        
        # Connect up the buttons and widgets
        # self.person_detail.buttonClose.clicked.connect(self.onCloseClick)
        # self.person_detail.buttonTrivia.clicked.connect(self.onTriviaClick)
        # self.person_detail.listMovies.clicked.connect(self.onMovieClick)

        # self.m_person_id = person_id
        # Use m_parent to call MovieDialog
        # self.m_parent = parent

        # self.getActorInfo()
        # self.getMovieInfo()

        # QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
        
    def getPersonDetail(self):
        self.congress = Congress(self.API_KEY)
        senator = self.congress.members.get(self.m_person_id)
        
        try:
            self.person_detail.textName.setText(str(senator["first_name"]) + " " + str(senator["last_name"]))
            self.person_detail.textState.setText(str(senator["roles"][0]["state"]))
            self.person_detail.textParty.setText(str(senator["roles"][0]["party"]))
            self.person_detail.textChamber.setText(str(senator["roles"][0]["chamber"]))
            self.person_detail.textBirthday.setText(str(senator["date_of_birth"]))
            self.person_detail.textPhone.setText(str(senator["roles"][0]["phone"]))
            self.person_detail.textAddress.setText(str(senator["roles"][0]["office"]))
            self.person_detail.textContact.setText(str(senator["roles"][0]["contact_form"]))
            self.person_detail.textWeb.setText(str(senator["url"]))
            
            if senator["govtrack_id"]:
                url_name = str(senator["first_name"]+ "_" + str(senator["last_name"]))
                url = "https://www.govtrack.us/congress/members/" + url_name + "/"
                self.person_detail.textGovTrack.setText(url + str(senator["govtrack_id"]))
            else:
                self.person_detail.textGovTrack.setText("None")
            
            if senator["votesmart_id"]:
                url = "https://votesmart.org/candidate/"
                self.person_detail.textVoteSmart.setText(url + str(senator["votesmart_id"]))
            else:
                self.person_detail.textVoteSmart.setText("None")
            
            if senator["crp_id"]:
                url = "https://www.opensecrets.org/members-of-congress/summary?cid="
                self.person_detail.textCrp.setText(url + str(senator["crp_id"]))
            else:
                self.person_detail.textCrp.setText("None")
            
        except KeyError:
            pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = DetailDialog()
    sys.exit(dialog.exec_())


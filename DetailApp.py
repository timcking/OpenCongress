from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui_detaildialog import Ui_DetailDialog
from congress import Congress
import urllib.request
import config

class DetailDialog(QDialog):
    API_KEY = config.APP_CONFIG['api_key']
    PHOTO_URL = config.APP_CONFIG['photo_url']

    m_person_id = None
    
    def __init__(self, *positional_parameters, **keyword_parameters):
        super(DetailDialog, self).__init__()

        # Set up the user interface from Designer.
        self.person_detail = Ui_DetailDialog()
        self.resize(550, 500)
        self.setMinimumSize(QSize(550, 500))
        self.person_detail.setupUi(self)
        
        self.m_person_id = positional_parameters[1]
        self.person_detail.buttonBox.clicked.connect(self.close)

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        self.getPersonDetail()
        
    def getPersonDetail(self):
        self.congress = Congress(self.API_KEY)
        senator = self.congress.members.get(self.m_person_id)
        
        # https://theunitedstates.io/images/congress/[size]/[bioguide].jpg
        # [size] can be one of:
        # original - As originally downloaded. Typically, 675x825, but it can vary.
        # 450x550
        # 225x275

        try:
            url = self.PHOTO_URL + self.m_person_id + '.jpg'
            img = QImage()
            data = urllib.request.urlopen(url).read()
            img.loadFromData(data)
        except Exception as e:
            pass

        self.person_detail.lblPhoto.setPixmap(QPixmap(img).scaledToWidth(100))

        try:
            self.person_detail.lblName.setText(str(senator['first_name']) + ' ' + str(senator['last_name']))
            self.person_detail.textState.setText(str(senator['roles'][0]['state']))
            self.person_detail.textParty.setText(str(senator['roles'][0]['party']))
            self.person_detail.textChamber.setText(str(senator['roles'][0]['chamber']))
            self.person_detail.textBirthday.setText(str(senator['date_of_birth']))
            self.person_detail.textPhone.setText(str(senator['roles'][0]['phone']))
            self.person_detail.textAddress.setText(str(senator['roles'][0]['office']))
            self.person_detail.textVotes.setText(str(senator['roles'][0]['missed_votes_pct']))

            if senator['roles'][0]['contact_form']:
                contact_url = senator['roles'][0]['contact_form']
                self.person_detail.lblContact.setText('<a href=' + contact_url + '>Contact</a>')
                self.person_detail.lblContact.setOpenExternalLinks(True)
            else:
                self.person_detail.lblContact.setText('Contact')

            if senator['url']:
                self.person_detail.lblWeb.setText('<a href=' + senator['url'] + '>Web</a>')
                self.person_detail.lblWeb.setOpenExternalLinks(True)
            else:
                self.person_detail.lblWeb.setText('Web')
            
            if senator['govtrack_id']:
                url_name = str(senator['first_name']+ '_' + str(senator['last_name']))
                url = 'https://www.govtrack.us/congress/members/' + url_name + '/'
                self.person_detail.lblGovTrack.setText('<a href=' + url + str(senator['govtrack_id']) + '>GovTrack</a>')
                self.person_detail.lblGovTrack.setOpenExternalLinks(True)
            else:
                self.person_detail.lblGovTrack.setText('GovTrack')
            
            if senator['votesmart_id']:
                url = 'https://votesmart.org/candidate/'
                self.person_detail.lblVoteSmart.setText('<a href=' + url + str(senator['votesmart_id']) + '>VoteSmart</a>')
                self.person_detail.lblVoteSmart.setOpenExternalLinks(True)
            else:
                self.person_detail.lblVoteSmart.setText('VoteSmart')
            
            if senator['crp_id']:
                # url = 'https://www.opensecrets.org/members-of-congress/summary?cid='
                # Need to escape the = sign with &#61;
                url = 'https://www.opensecrets.org/members-of-congress/summary?cid&#61;'
                crp_link = '<a href=' + url + str(senator['crp_id']) + '>CRP</a>'
                self.person_detail.lblCrp.setText(crp_link)
                self.person_detail.lblCrp.setOpenExternalLinks(True)
            else:
                self.person_detail.lblCrp.setText('CRP')
            
        except KeyError:
            pass

        QApplication.restoreOverrideCursor()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = DetailDialog()
    sys.exit(dialog.exec_())


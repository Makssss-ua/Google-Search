from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from googleapiclient.discovery import build

my_api_key = "AIzaSyC4fkC51DjHW9I4-6YchvbQYZ2uNcRVvYU" #Your google api
# create on https://console.developers.google.com/apis
my_cse_id = "973a8e6c0d7c568b0" #Your google search
# you can create on https://programmablesearchengine.google.com/

Form, Window = uic.loadUiType("program.ui")#way to ui file; example r"C:\Users\User\Desktop\Python\program.ui"

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def main():
    form.pushButton.clicked.connect(but_click)

def but_click():
    try:
        text = form.lineEdit.text()
        printext = []
        results = google_search(text, my_api_key, my_cse_id, num=10)
        for result in results:
            link = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"color:#000080;font-weight:600;\">"+result["link"]+"</span></p></body></html>"
            title = ("<span style=\"color:#000000;\">"+result["title"]+"</span>")
            printext.append(title+link)
        form.textBrowser.setText('\n'.join(printext))
        form.lineEdit.setText('')
    except:
        form.textBrowser.setText("<span style=\"color:#FF0000;\">Error!"
        "Please try again</span>")
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
main()
app.exec()
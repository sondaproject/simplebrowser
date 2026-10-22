import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QToolBar,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("SimpleBrowser")
    self.setGeometry(100, 100, 1200, 800)

    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://www.google.com"))
    self.setCentralWidget(self.browser)

    toolbar = QToolBar("Navigation")
    self.addToolBar(toolbar)

    back_btn = QPushButton("←")
    back_btn.clicked.connect(self.browser.back)
    toolbar.addWidget(back_btn)

    forward_btn = QPushButton("→")
    forward_btn.clicked.connect(self.browser.forward)
    toolbar.addWidget(forward_btn)

    reload_btn = QPushButton("⟳")
    reload_btn.clicked.connect(self.browser.reload)
    toolbar.addWidget(reload_btn)

    home_btn = QPushButton("🏠")
    home_btn.clicked.connect(self.navigate_home)
    toolbar.addWidget(home_btn)

    toolbar.addSeparator()

    self.url_bar = QLineEdit()
    self.url_bar.returnPressed.connect(self.navigate_to_url)
    toolbar.addWidget(self.url_bar)

    self.browser.urlChanged.connect(self.update_url_bar)

  def navigate_home(self):
    self.browser.setUrl(QUrl("https://www.google.com"))

  def navigate_to_url(self):
    text = self.url_bar.text().strip()
    if not text.startswith("http://") and not text.startswith("https://"):
      if "." in text and " " not in text:
        text = "https://" + text
      else:
        text = "https://www.google.com/search?q=" + text.replace(" ", "+")
    self.browser.setUrl(QUrl(text))

  def update_url_bar(self, q):
    self.url_bar.setText(q.toString())


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Browser()
  window.show()
  sys.exit(app.exec())

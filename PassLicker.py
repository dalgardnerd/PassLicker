# Form implementation generated from reading ui file '.\passlicker_pyqt5.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from settings import handle_defaults, load_defaults, write_defaults
from pw import get_passphrase, push_passphrase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(130, 210, 131, 23))
        self.save_button.setMinimumSize(QtCore.QSize(120, 0))
        self.save_button.setObjectName("save_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 140, 170, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gen_buttons = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.gen_buttons.setContentsMargins(0, 0, 0, 0)
        self.gen_buttons.setObjectName("gen_buttons")
        self.gen_push_button = QtWidgets.QPushButton(self.layoutWidget)
        self.gen_push_button.setObjectName("gen_push_button")
        self.gen_buttons.addWidget(self.gen_push_button)
        self.gen_button = QtWidgets.QPushButton(self.layoutWidget)
        self.gen_button.setObjectName("gen_button")
        self.gen_buttons.addWidget(self.gen_button)
        self.specific_buttons = QtWidgets.QGroupBox(self.centralwidget)
        self.specific_buttons.setGeometry(QtCore.QRect(410, 20, 167, 91))
        self.specific_buttons.setObjectName("specific_buttons")
        self.gridLayout = QtWidgets.QGridLayout(self.specific_buttons)
        self.gridLayout.setObjectName("gridLayout")
        self.push_specific_button = QtWidgets.QPushButton(
            self.specific_buttons)
        self.push_specific_button.setObjectName("push_specific_button")
        self.gridLayout.addWidget(self.push_specific_button, 0, 0, 1, 1)
        self.push_specific_box = QtWidgets.QLineEdit(self.specific_buttons)
        self.push_specific_box.setMaximumSize(QtCore.QSize(16777215, 20))
        self.push_specific_box.setObjectName("push_specific_box")
        self.gridLayout.addWidget(self.push_specific_box, 1, 0, 1, 1)
        self.output_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(15, 240, 571, 261))
        self.output_box.setObjectName("output_box")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 361, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.settings_grid = QtWidgets.QGridLayout(self.layoutWidget1)
        self.settings_grid.setContentsMargins(0, 0, 0, 0)
        self.settings_grid.setObjectName("settings_grid")
        self.link_opts = QtWidgets.QGroupBox(self.layoutWidget1)
        self.link_opts.setObjectName("link_opts")
        self.layoutWidget2 = QtWidgets.QWidget(self.link_opts)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 121, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.link_boxes = QtWidgets.QGridLayout(self.layoutWidget2)
        self.link_boxes.setContentsMargins(0, 0, 0, 0)
        self.link_boxes.setObjectName("link_boxes")
        self.expire_views_label = QtWidgets.QLabel(self.layoutWidget2)
        self.expire_views_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.expire_views_label.setObjectName("expire_views_label")
        self.link_boxes.addWidget(self.expire_views_label, 1, 0, 1, 1)
        self.expire_days_label = QtWidgets.QLabel(self.layoutWidget2)
        self.expire_days_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.expire_days_label.setObjectName("expire_days_label")
        self.link_boxes.addWidget(self.expire_days_label, 0, 0, 1, 1)
        self.expire_days_box = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.expire_days_box.sizePolicy().hasHeightForWidth())
        self.expire_days_box.setSizePolicy(sizePolicy)
        self.expire_days_box.setObjectName("expire_days_box")
        self.link_boxes.addWidget(self.expire_days_box, 0, 1, 1, 1)
        self.expire_views_box = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.expire_views_box.sizePolicy().hasHeightForWidth())
        self.expire_views_box.setSizePolicy(sizePolicy)
        self.expire_views_box.setObjectName("expire_views_box")
        self.link_boxes.addWidget(self.expire_views_box, 1, 1, 1, 1)
        self.settings_grid.addWidget(self.link_opts, 0, 1, 1, 1)
        self.pass_opts = QtWidgets.QGroupBox(self.layoutWidget1)
        self.pass_opts.setObjectName("pass_opts")
        self.layoutWidget3 = QtWidgets.QWidget(self.pass_opts)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 158, 151))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.pass_boxes = QtWidgets.QGridLayout(self.layoutWidget3)
        self.pass_boxes.setContentsMargins(0, 0, 0, 0)
        self.pass_boxes.setObjectName("pass_boxes")
        self.num_chars_label = QtWidgets.QLabel(self.layoutWidget3)
        self.num_chars_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.num_chars_label.setObjectName("num_chars_label")
        self.pass_boxes.addWidget(self.num_chars_label, 0, 0, 1, 1)
        self.num_chars_box = QtWidgets.QSpinBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.num_chars_box.sizePolicy().hasHeightForWidth())
        self.num_chars_box.setSizePolicy(sizePolicy)
        self.num_chars_box.setObjectName("num_chars_box")
        self.pass_boxes.addWidget(self.num_chars_box, 0, 1, 1, 1)
        self.word_separator_box = QtWidgets.QLineEdit(self.layoutWidget3)
        self.word_separator_box.setMaximumSize(QtCore.QSize(33, 16777215))
        self.word_separator_box.setObjectName("word_separator_box")
        self.pass_boxes.addWidget(self.word_separator_box, 2, 1, 1, 1)
        self.include_digits_label = QtWidgets.QLabel(self.layoutWidget3)
        self.include_digits_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.include_digits_label.setObjectName("include_digits_label")
        self.pass_boxes.addWidget(self.include_digits_label, 3, 0, 1, 1)
        self.total_words_box = QtWidgets.QSpinBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.total_words_box.sizePolicy().hasHeightForWidth())
        self.total_words_box.setSizePolicy(sizePolicy)
        self.total_words_box.setObjectName("total_words_box")
        self.pass_boxes.addWidget(self.total_words_box, 1, 1, 1, 1)
        self.include_digits_box = QtWidgets.QCheckBox(self.layoutWidget3)
        self.include_digits_box.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.include_digits_box.setAutoFillBackground(False)
        self.include_digits_box.setText("")
        self.include_digits_box.setObjectName("include_digits_box")
        self.pass_boxes.addWidget(self.include_digits_box, 3, 1, 1, 1)
        self.word_separator = QtWidgets.QLabel(self.layoutWidget3)
        self.word_separator.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.word_separator.setObjectName("word_separator")
        self.pass_boxes.addWidget(self.word_separator, 2, 0, 1, 1)
        self.total_word_label = QtWidgets.QLabel(self.layoutWidget3)
        self.total_word_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.total_word_label.setObjectName("total_word_label")
        self.pass_boxes.addWidget(self.total_word_label, 1, 0, 1, 1)
        self.settings_grid.addWidget(self.pass_opts, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect buttons
        self.gen_button.clicked.connect(lambda: self.clicked("gen_button"))
        self.gen_push_button.clicked.connect(
            lambda: self.clicked("gen_push_button"))
        self.push_specific_button.clicked.connect(
            lambda: self.clicked("push_specific_button"))
        self.save_button.clicked.connect(lambda: self.clicked("save_button"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassLicker"))
        self.save_button.setText(_translate("MainWindow", "Save Settings"))
        self.gen_push_button.setText(_translate(
            "MainWindow", "Generate and Push Passphrase"))
        self.gen_button.setText(_translate(
            "MainWindow", "Generate Passphrase"))
        self.specific_buttons.setTitle(
            _translate("MainWindow", "Specific Passphrase"))
        self.push_specific_button.setText(_translate(
            "MainWindow", "Push Specific Passphrase"))
        self.link_opts.setTitle(_translate("MainWindow", "Link Settings"))
        self.expire_views_label.setText(
            _translate("MainWindow", "Views to Expire"))
        self.expire_days_label.setText(
            _translate("MainWindow", "Days to Expire"))
        self.pass_opts.setTitle(_translate(
            "MainWindow", "Passphrase Settings:"))
        self.num_chars_label.setText(_translate(
            "MainWindow", "Number of Characters"))
        self.include_digits_label.setText(
            _translate("MainWindow", "Include Digits"))
        self.word_separator.setText(_translate("MainWindow", "Word Separator"))
        self.total_word_label.setText(_translate("MainWindow", "Total Words"))

    def save_defaults(self):
        num_chars = self.num_chars_box.value()
        total_words = self.total_words_box.value()
        word_separator = self.word_separator_box.text()
        include_digits = self.include_digits_box.isChecked()
        expire_days = self.expire_days_box.value()
        expire_views = self.expire_views_box.value()
        write_defaults(num_chars, total_words, word_separator,
                       include_digits, expire_days, expire_views)

    def read_defaults(self):
        settings = handle_defaults()
        self.num_chars_box.setValue(int(settings["num_chars"]))
        self.total_words_box.setValue(int(settings["total_words"]))
        self.word_separator_box.setText(settings["word_separator"])
        self.include_digits_box.setChecked(
            True if settings["include_digits"] == "True" else False)
        self.expire_days_box.setValue(int(settings["expire_days"]))
        self.expire_views_box.setValue(int(settings["expire_views"]))

        # if settings[]

    def get_box_values(self):
        num_chars = self.num_chars_box.value()
        total_words = self.total_words_box.value()
        word_separator = self.word_separator_box.text()
        include_digits = self.include_digits_box.isChecked()
        expire_days = self.expire_days_box.value()
        expire_views = self.expire_views_box.value()
        print("Include digits is " + str(include_digits))
        return [num_chars, total_words, word_separator, include_digits, expire_days, expire_views]

    def clicked(self, button_clicked):
        if button_clicked == "gen_button":
            box_values = self.get_box_values()
            passphrase = get_passphrase(
                box_values[0], box_values[1], box_values[2], box_values[3])
            current_text = self.output_box.toPlainText()
            self.output_box.setPlainText(passphrase)
            self.output_box.append("")
            self.output_box.append(current_text)
            self.output_box.verticalScrollBar().setValue(0)
        if button_clicked == "gen_push_button":
            box_values = self.get_box_values()
            passphrase = (get_passphrase(
                box_values[0], box_values[1], box_values[2], box_values[3]))
            link = push_passphrase(passphrase, box_values[4], box_values[5])
            current_text = self.output_box.toPlainText()
            self.output_box.setPlainText(passphrase)
            self.output_box.append(link)
            self.output_box.append("")
            self.output_box.append(current_text)
            self.output_box.verticalScrollBar().setValue(0)

        if button_clicked == "push_specific_button":
            passphrase = self.push_specific_box.text()
            link = push_passphrase(passphrase,
                                   self.expire_days_box.value(),
                                   self.expire_views_box.value())
            current_text = self.output_box.toPlainText()
            self.output_box.setPlainText(passphrase)
            self.output_box.append(link)
            self.output_box.append("")
            self.output_box.append(current_text)
            self.output_box.verticalScrollBar().setValue(0)
        if button_clicked == "save_button":
            self.save_defaults()
            current_text = self.output_box.toPlainText()
            self.output_box.setPlainText("Saving settings to defaults.json")
            self.output_box.append("")
            self.output_box.append(current_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('passlicker.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.setFixedSize(600, 510)
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.read_defaults()
    sys.exit(app.exec())

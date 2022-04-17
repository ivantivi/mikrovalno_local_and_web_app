from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from send_data import send_data
from datetime import datetime

temp_data = []
pres_data = []
humi_data = []
alti_data = []
number_of_points = 15
graph_status = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.serial_widget = QtWidgets.QWidget(self.centralwidget)
        self.serial_widget.setObjectName("serial_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.serial_widget)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.serial_frame = QtWidgets.QFrame(self.serial_widget)
        self.serial_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.serial_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.serial_frame.setObjectName("serial_frame")
        self.serial_line_edit = QtWidgets.QLineEdit(self.serial_frame)
        self.serial_line_edit.setGeometry(QtCore.QRect(20, 30, 281, 22))
        self.serial_line_edit.setObjectName("serial_line_edit")
        self.serial_label = QtWidgets.QLabel(self.serial_frame)
        self.serial_label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.serial_label.setObjectName("serial_label")
        self.connect_button = QtWidgets.QPushButton(self.serial_frame)
        self.connect_button.setGeometry(QtCore.QRect(330, 30, 93, 28))
        self.connect_button.setObjectName("connect_button")
        self.serial_label_2 = QtWidgets.QLabel(self.serial_frame)
        self.serial_label_2.setGeometry(QtCore.QRect(510, 10, 131, 16))
        self.serial_label_2.setObjectName("serial_label_2")
        self.serial_label_3 = QtWidgets.QLabel(self.serial_frame)
        self.serial_label_3.setGeometry(QtCore.QRect(980, 10, 111, 16))
        self.serial_label_3.setObjectName("serial_label_3")
        self.pause_button = QtWidgets.QPushButton(self.serial_frame)
        self.pause_button.setGeometry(QtCore.QRect(980, 30, 93, 28))
        self.pause_button.setObjectName("pause_button")
        self.continue_button = QtWidgets.QPushButton(self.serial_frame)
        self.continue_button.setGeometry(QtCore.QRect(1080, 30, 93, 28))
        self.continue_button.setObjectName("continue_button")
        self.grid_on_button = QtWidgets.QPushButton(self.serial_frame)
        self.grid_on_button.setGeometry(QtCore.QRect(1210, 30, 93, 28))
        self.grid_on_button.setObjectName("grid_on_button")
        self.grid_off_button = QtWidgets.QPushButton(self.serial_frame)
        self.grid_off_button.setGeometry(QtCore.QRect(1310, 30, 93, 28))
        self.grid_off_button.setObjectName("grid_off_button")
        self.enter_button = QtWidgets.QPushButton(self.serial_frame)
        self.enter_button.setGeometry(QtCore.QRect(820, 30, 93, 28))
        self.enter_button.setObjectName("enter_button")
        self.point_line_edit = QtWidgets.QLineEdit(self.serial_frame)
        self.point_line_edit.setGeometry(QtCore.QRect(510, 30, 281, 22))
        self.point_line_edit.setObjectName("point_line_edit")
        self.horizontalLayout_5.addWidget(self.serial_frame)
        self.verticalLayout.addWidget(self.serial_widget)
        self.graph_widget = QtWidgets.QWidget(self.centralwidget)
        self.graph_widget.setObjectName("graph_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.graph_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.temp_frame = QtWidgets.QFrame(self.graph_widget)
        self.temp_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp_frame.setObjectName("temp_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.temp_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temp_graph_widget = PlotWidget(self.temp_frame)
        self.temp_graph_widget.setObjectName("temp_graph_widget")
        self.horizontalLayout.addWidget(self.temp_graph_widget)
        self.gridLayout.addWidget(self.temp_frame, 0, 0, 1, 1)
        self.pres_frame = QtWidgets.QFrame(self.graph_widget)
        self.pres_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.pres_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pres_frame.setObjectName("pres_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pres_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pres_graph_widget = PlotWidget(self.pres_frame)
        self.pres_graph_widget.setObjectName("pres_graph_widget")
        self.horizontalLayout_2.addWidget(self.pres_graph_widget)
        self.gridLayout.addWidget(self.pres_frame, 0, 1, 1, 1)
        self.humi_frame = QtWidgets.QFrame(self.graph_widget)
        self.humi_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.humi_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.humi_frame.setObjectName("humi_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.humi_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.humi_graph_widget = PlotWidget(self.humi_frame)
        self.humi_graph_widget.setObjectName("humi_graph_widget")
        self.horizontalLayout_3.addWidget(self.humi_graph_widget)
        self.gridLayout.addWidget(self.humi_frame, 1, 0, 1, 1)
        self.alti_frame = QtWidgets.QFrame(self.graph_widget)
        self.alti_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.alti_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alti_frame.setObjectName("alti_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.alti_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.alti_graph_widget = PlotWidget(self.alti_frame)
        self.alti_graph_widget.setObjectName("alti_graph_widget")
        self.horizontalLayout_4.addWidget(self.alti_graph_widget)
        self.gridLayout.addWidget(self.alti_frame, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.graph_widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ######
        self.connect_button.clicked.connect(self.connect_serial)
        self.enter_button.clicked.connect(self.set_number_of_points)
        self.pause_button.clicked.connect(self.pause_graph)
        self.continue_button.clicked.connect(self.continue_graph)
        self.grid_on_button.clicked.connect(self.grid_on)
        self.grid_off_button.clicked.connect(self.grid_off)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        graph_pen = pg.mkPen(color=(255,255,255), width=2)
        axis_pen = pg.mkPen(color=(255,255,255), width=2)
        styles = {"color":"w", "font-size":"10pt"}

        self.temp_graph_widget.setLabel("left", "Temperature (°C)", **styles)
        #self.temp_graph_widget.setLabel("bottom", "Time", **styles)
        self.temp_graph_widget.getAxis("bottom").setPen(axis_pen)
        self.temp_graph_widget.getAxis("left").setPen(axis_pen)
        self.temp_graph_widget.setTitle("Temperature", color="w", size="15pt")
        self.temp_graph_data = self.temp_graph_widget.plot([], [], pen=graph_pen)

        self.pres_graph_widget.setLabel("left", "Pressure (hPa)", **styles)
        #self.pres_graph_widget.setLabel("bottom", "Time", **styles)
        self.pres_graph_widget.getAxis("bottom").setPen(axis_pen)
        self.pres_graph_widget.getAxis("left").setPen(axis_pen)
        self.pres_graph_widget.setTitle("Pressure", color="w", size="15pt")
        self.pres_graph_data = self.pres_graph_widget.plot([], [], pen=graph_pen)

        self.alti_graph_widget.setLabel("left", "Altitude (m)", **styles)
        #self.alti_graph_widget.setLabel("bottom", "Time", **styles)
        self.alti_graph_widget.getAxis("bottom").setPen(axis_pen)
        self.alti_graph_widget.getAxis("left").setPen(axis_pen)
        self.alti_graph_widget.setTitle("Altitude", color="w", size="15pt")
        self.alti_graph_data = self.alti_graph_widget.plot([], [], pen=graph_pen)

        self.humi_graph_widget.setLabel("left", "Humidity (%)", **styles)
        #self.humi_graph_widget.setLabel("bottom", "Time", **styles)
        self.humi_graph_widget.getAxis("bottom").setPen(axis_pen)
        self.humi_graph_widget.getAxis("left").setPen(axis_pen)
        self.humi_graph_widget.setTitle("Humidity", color="w", size="15pt")
        self.humi_graph_data = self.humi_graph_widget.plot([], [], pen=graph_pen)
    
    def update_temp_graph_plot(self, y):
        x_list = [*range(0, len(y))]
        self.temp_graph_data.setData(x_list, y)

    def update_pres_graph_plot(self, y):
        x_list = [*range(0, len(y))]
        self.pres_graph_data.setData(x_list, y)
    
    def update_alti_graph_plot(self, y):
        x_list = [*range(0, len(y))]
        self.alti_graph_data.setData(x_list, y)
    
    def update_humi_graph_plot(self, y):
        x_list = [*range(0, len(y))]
        self.humi_graph_data.setData(x_list, y)

    def connect_serial(self):
        port_name = self.serial_line_edit.text()
        self.serial_input = QtSerialPort.QSerialPort()
        self.serial_input.setPortName(port_name)
        if self.serial_input.open(QtCore.QIODevice.ReadWrite):
            self.serial_input.setBaudRate(9600)
            self.serial_input.readyRead.connect(self.on_serial_read)
    
    def on_serial_read(self):
        while self.serial_input.canReadLine():
            text_input = self.serial_input.readLine().data().decode()
            text_input = text_input.rstrip("\r\n")[1:-1]
            serial_data = [float(i) for i in text_input.split("|")]
            ##############SEND TO SQL DATABASE
            now = datetime.now()
            time_string = now.strftime("%H:%M:%S")
            send_data(serial_data, time_string)
            ##################################

            while(len(temp_data) > number_of_points):
                temp_data.pop(0)
                pres_data.pop(0)
                humi_data.pop(0)
                alti_data.pop(0)
            
            if(len(temp_data) <= number_of_points):
                temp_data.append(serial_data[0])
                pres_data.append(serial_data[1]) #hPa
                humi_data.append(serial_data[2])
                alti_data.append(serial_data[3])            
            else:
                temp_data.pop(0)
                pres_data.pop(0)
                humi_data.pop(0)
                alti_data.pop(0)
                temp_data.append(serial_data[0])
                pres_data.append(serial_data[1]/100) #hPa
                humi_data.append(serial_data[2])
                alti_data.append(serial_data[3]) 
            
            if(graph_status == True):
                self.update_temp_graph_plot(temp_data)
                self.update_pres_graph_plot(pres_data)
                self.update_humi_graph_plot(humi_data)
                self.update_alti_graph_plot(alti_data)
            else:
                pass

    def pause_graph(self):
        global graph_status
        graph_status = False
    
    def continue_graph(self):
        global graph_status
        graph_status = True
    
    def grid_on(self):
        self.temp_graph_widget.showGrid(x=True, y=True)
        self.pres_graph_widget.showGrid(x=True, y=True)
        self.humi_graph_widget.showGrid(x=True, y=True)
        self.alti_graph_widget.showGrid(x=True, y=True)

    def grid_off(self):
        self.temp_graph_widget.showGrid(x=False, y=False)
        self.pres_graph_widget.showGrid(x=False, y=False)
        self.humi_graph_widget.showGrid(x=False, y=False)
        self.alti_graph_widget.showGrid(x=False, y=False)

    def set_number_of_points(self):
        points = self.point_line_edit.text().upper().strip(" ")
        global number_of_points 
        number_of_points = int(points)

        ######
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataVisual"))
        self.serial_line_edit.setText(_translate("MainWindow", "COM3"))
        self.point_line_edit.setText(_translate("MainWindow", "15"))
        self.serial_label.setText(_translate("MainWindow", "SERIAL PORT"))
        self.connect_button.setText(_translate("MainWindow", "CONNECT"))
        self.serial_label_2.setText(_translate("MainWindow", "NUMBER OF POINTS"))
        self.enter_button.setText(_translate("MainWindow", "ENTER"))
        self.serial_label_3.setText(_translate("MainWindow", "GRAPH CONTROL"))
        self.pause_button.setText(_translate("MainWindow", "PAUSE"))
        self.continue_button.setText(_translate("MainWindow", "CONTINUE"))
        self.grid_on_button.setText(_translate("MainWindow", "GRID ON"))
        self.grid_off_button.setText(_translate("MainWindow", "GRID OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

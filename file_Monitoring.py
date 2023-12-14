import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QLabel, QTableWidget, QTableWidgetItem, QPushButton, QGridLayout,
    QSizePolicy
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor
from datetime import datetime

class FileAccessHandler(FileSystemEventHandler):
    def __init__(self, monitored_directory, log_signal):
        super().__init__()
        self.monitored_directory = monitored_directory
        self.log_signal = log_signal

    def on_modified(self, event):
        if event.is_directory or event.src_path.endswith('.tmp'):
            return
        log_entry = f"Modified: File {event.src_path} was modified."
        self.log_signal.emit(('Modified', log_entry))

    def on_created(self, event):
        if event.is_directory or event.src_path.endswith('.tmp'):
            return
        log_entry = f"Created: File {event.src_path} was created."
        self.log_signal.emit(('Created', log_entry))

    def on_deleted(self, event):
        if event.is_directory or event.src_path.endswith('.tmp'):
            return
        log_entry = f"Deleted: File {event.src_path} was deleted."
        self.log_signal.emit(('Deleted', log_entry))

class FileAccessMonitoringThread(QThread):
    log_signal = pyqtSignal(tuple)

    def __init__(self, monitored_directory):
        super().__init__()
        self.monitored_directory = monitored_directory

    def run(self):
        event_handler = FileAccessHandler(
            monitored_directory=self.monitored_directory, log_signal=self.log_signal)
        observer = Observer()
        observer.schedule(event_handler, path=self.monitored_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

class NetworkAnomalyDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Intrusion Detection System')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Add QTextEdit for displaying logs
        self.log_text = QTextEdit(self)
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

        # Add QTableWidgets for displaying file events
        self.deleted_files_table = QTableWidget(self)
        self.modified_files_table = QTableWidget(self)
        self.threat_files_table = QTableWidget(self)

        self.setup_table(self.deleted_files_table, 'Deleted Files')
        self.setup_table(self.modified_files_table, 'Modified Files')
        self.setup_table(self.threat_files_table, 'Threat Files', background_color='white', text_color='black')

        layout.addWidget(self.deleted_files_table)
        layout.addWidget(self.modified_files_table)
        layout.addWidget(self.threat_files_table)

        central_widget.setLayout(layout)

        # Create and start the file access monitoring thread
        self.file_access_monitor_thread = FileAccessMonitoringThread(monitored_directory=os.getcwd())
        self.file_access_monitor_thread.log_signal.connect(self.update_log)
        self.file_access_monitor_thread.start()

    def setup_table(self, table_widget, title, background_color=None, text_color=None):
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(['Event Type', 'File Path'])
        table_widget.verticalHeader().setVisible(False)
        table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        header = table_widget.horizontalHeader()
        header.setSectionResizeMode(1, header.Stretch)

        if background_color and text_color:
            table_widget.setStyleSheet(
                f"background-color: {background_color}; color: {text_color}; font-weight: bold;"
            )

        title_item = QTableWidgetItem(title)
        title_item.setBackground(QColor(53, 53, 53))
        title_item.setForeground(Qt.white)
        title_item.setFont(table_widget.font())
        title_item.setTextAlignment(Qt.AlignCenter)
        table_widget.setItem(0, 0, title_item)

    def update_log(self, log_entry):
        log_type, entry = log_entry
        log_type = log_type.strip()

        # Display logs in the QTextEdit
        self.log_text.append(entry)

        # Add the file event to the appropriate QTableWidget
        if log_type == 'Deleted':
            self.add_to_table(self.deleted_files_table, entry)
        elif log_type == 'Modified':
            self.add_to_table(self.modified_files_table, entry)
        elif log_type == 'Created':
            self.add_to_table(self.threat_files_table, entry)

    def add_to_table(self, table_widget, entry):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)
        table_widget.setItem(row_position, 0, QTableWidgetItem(entry.partition(':')[0].strip()))
        table_widget.setItem(row_position, 1, QTableWidgetItem(entry.partition(':')[2].strip()))

    def closeEvent(self, event):
        # Stop the file access monitoring thread before closing the application
        self.file_access_monitor_thread.terminate()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style for a modern look

    # Set a dark color palette for a cyber security theme
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

    mainWindow = NetworkAnomalyDetectionApp()
    mainWindow.show()
    sys.exit(app.exec_())

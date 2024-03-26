# Anomaly Detection Application uisng file monitoring

## Overview

The Network Anomaly Detection Application is a simple Python application that provides real-time monitoring of file system events in a specified directory. It uses the PyQt5 library for the graphical user interface (GUI) and the Watchdog library for monitoring file system changes.

### Features

- Monitors file system events such as file creation, modification, and deletion.
- Displays real-time information in tables for deleted, modified, and threat files.
- Dark color palette for a cyber security theme.
- Logs all file system events in a dedicated QTextEdit.
## Modules Used:
- **os**: Provides a portable way to use operating system-dependent functionality.
- **sys**: Provides access to some variables used or maintained by the Python interpreter.
- **time**: Provides various time-related functions.
- **watchdog**: A Python library that monitors file system events.
- **PyQt5**: A set of Python bindings for Qt application framework.
- **datetime**: Provides classes for manipulating dates and times.

## Classes:
### FileAccessHandler:
Subclass of `FileSystemEventHandler` that overrides methods for handling file system events such as file modifications, creations, and deletions. It emits a signal whenever an event occurs.

### FileAccessMonitoringThread:
Subclass of `QThread` responsible for monitoring file system events in a separate thread. It uses an instance of `FileAccessHandler` to handle the events.

### NetworkAnomalyDetectionApp:
Subclass of `QMainWindow` representing the main GUI application. It initializes the GUI components, sets up the layout, and starts the file access monitoring thread. It also handles updating logs and displaying file events in `QTableWidgets`.

## Methods:
- `initUI()`: Initializes the main UI components including `QTextEdit` for logs and `QTableWidgets` for displaying file events.
- `setup_table()`: Configures the appearance and properties of a `QTableWidget`.
- `update_log()`: Updates the log `QTextEdit` and adds file events to the appropriate `QTableWidget` based on the event type.
- `add_to_table()`: Adds a new row to a `QTableWidget` with event details.
- `closeEvent()`: Overrides the close event to properly terminate the file access monitoring thread before closing the application.

## Execution:
The `if __name__ == '__main__':` block initializes the PyQt5 application, sets its style to "Fusion" for a modern look, sets a dark color palette for a cyber security theme, creates an instance of `NetworkAnomalyDetectionApp`, and starts the PyQt5 event loop.

## Tracking File Access:
Whenever a file is created or modified within the monitored directory, the corresponding file path is recorded along with an increment to its access count in the `self.file_access_counts` dictionary.

-Displaying Access Counts: The access counts are displayed in a table (self.access_counts_table) within the application's user interface. This table provides a visual representation of the access patterns for each file.

-Anomaly Detection: While not explicitly implemented in this code, access counts can be used for anomaly detection. Unusual patterns, such as a sudden increase in access counts for a particular file or unexpected access to sensitive files, could indicate potential security incidents, unauthorized activity, or malware activity.

-Monitoring Behavior Over Time: By continuously updating access counts over time, the application can track changes in file access patterns. This historical data can be analyzed to identify trends, patterns, or anomalies that may require further investigation.

## Getting Started

### Prerequisites

- Python 3.x
- PyQt5
- Watchdog

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/network-anomaly-detection.git
    cd network-anomaly-detection
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. The application window will appear, showing tables for deleted, modified, and threat files, along with a log area for file system events.

3. File system events in the specified directory will be monitored and displayed in real-time.

### Customization

- Modify the monitored directory by updating the `monitored_directory` variable in the `main.py` file.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

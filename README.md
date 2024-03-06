# Network Anomaly Detection Application file monitoring

## Overview

The Network Anomaly Detection Application is a simple Python application that provides real-time monitoring of file system events in a specified directory. It uses the PyQt5 library for the graphical user interface (GUI) and the Watchdog library for monitoring file system changes.

### Features

- Monitors file system events such as file creation, modification, and deletion.
- Displays real-time information in tables for deleted, modified, and threat files.
- Dark color palette for a cyber security theme.
- Logs all file system events in a dedicated QTextEdit.

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

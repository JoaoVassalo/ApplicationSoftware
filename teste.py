from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel

app = QApplication([])

# Main Window
window = QWidget()
layout = QVBoxLayout()

# Tab Widget
tab_widget = QTabWidget()

# Creating Tabs
tab1 = QWidget()
tab1_layout = QVBoxLayout()
tab1_layout.addWidget(QLabel("Content of Tab 1"))
tab1.setLayout(tab1_layout)

tab2 = QWidget()
tab2_layout = QVBoxLayout()
tab2_layout.addWidget(QLabel("Content of Tab 2"))
tab2.setLayout(tab2_layout)

tab_widget.addTab(tab1, "Area Impact")
tab_widget.addTab(tab2, "Volume Impact")

# Apply Custom Stylesheet
tab_widget.setStyleSheet("""
    QTabWidget::pane { 
        border: 2px solid #4CAF50; 
        background: white; 
    }
    QTabWidget::tab-bar {
        alignment: left;
        margin-left: 20px; /* Moves the entire tab bar to the right */
    }
    QTabBar::tab {
        background: lightgray; 
        padding: 10px; 
        border: 1px solid gray; 
        border-top-left-radius: 5px; 
        border-top-right-radius: 5px;
    }
    QTabBar::tab:selected {
        background: #4CAF50; 
        color: white;
        font-weight: bold;
    }
""")

layout.addWidget(tab_widget)
window.setLayout(layout)
window.show()

app.exec()


"""Application-wide FreeCAD AI assistant startup."""

import FreeCADGui as Gui

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets


def show_ai_assistant():
    """Open the floating assistant on demand."""
    import assistant
    assistant.show()


def install_ai_interface():
    """Register AI menu and toolbar in FreeCAD."""
    main_window = Gui.getMainWindow()

    if main_window is None:
        return

    # Do not create duplicate menus.
    existing = main_window.findChild(
        QtWidgets.QMenu, "FreeCADAI_Menu"
    )
    if existing is not None:
        return

    ai_menu = QtWidgets.QMenu("AI Assistant", main_window)
    ai_menu.setObjectName("FreeCADAI_Menu")
    main_window.menuBar().addMenu(ai_menu)

    action = QtGui.QAction(
        "Open Floating AI Assistant", main_window
    )
    action.setObjectName("FreeCADAI_Open")
    action.triggered.connect(show_ai_assistant)
    ai_menu.addAction(action)

    toolbar = main_window.addToolBar("AI Assistant")
    toolbar.setObjectName("FreeCADAI_Toolbar")
    toolbar.addAction(action)


QtCore.QTimer.singleShot(0, install_ai_interface)

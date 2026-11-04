
"""Register the FreeCAD AI assistant in the application."""

import FreeCADGui as Gui
from PySide import QtCore, QtGui, QtWidgets

import assistant


def install_ai_menu():
    """Add an application-wide menu for the floating AI assistant."""
    main_window = Gui.getMainWindow()
    menu_bar = main_window.menuBar()

    ai_menu = next(
        (action.menu() for action in menu_bar.actions()
         if action.objectName() == "FreeCADAI_Menu"),
        None,
    )

    if ai_menu is None:
        ai_menu = QtWidgets.QMenu("AI Assistant", main_window)
        menu_action = menu_bar.addMenu(ai_menu)
        menu_action.setObjectName("FreeCADAI_Menu")

        open_action = QtGui.QAction(
            "Open Floating AI Assistant", main_window
        )
        open_action.triggered.connect(
            lambda checked=False: assistant.show()
        )
        ai_menu.addAction(open_action)


QtCore.QTimer.singleShot(0, install_ai_menu)

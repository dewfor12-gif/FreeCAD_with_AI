
"""Application-wide FreeCAD AI assistant startup."""


def show_ai_assistant():
    """Open the floating assistant."""
    import sys
    from pathlib import Path

    module_dir = str(Path(__file__).resolve().parent)

    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)

    import assistant
    assistant.show()


def install_ai_interface():
    """Register the AI menu and toolbar."""
    import FreeCADGui as Gui
    from PySide6 import QtGui, QtWidgets

    main_window = Gui.getMainWindow()
    if main_window is None:
        return

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

    # Bind the callback directly so it survives startup.
    action.triggered.connect(show_ai_assistant)

    ai_menu.addAction(action)

    toolbar = main_window.addToolBar("AI Assistant")
    toolbar.setObjectName("FreeCADAI_Toolbar")
    toolbar.addAction(action)


from PySide6 import QtCore
QtCore.QTimer.singleShot(0, install_ai_interface)

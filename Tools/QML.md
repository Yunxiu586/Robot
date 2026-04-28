# QML

+ **UI** (User Interface) encompasses all components and systems that enable interaction and communication between a human user and a machine or software.
  + **CLI** (Command Line Interface) is a text-based interaction method where users issue structured commands to the operating system or software via a console or terminal emulator.
  + **GUI** (Graphical User Interface) is a visual environment that allows users to manipulate software functions and system objects through direct manipulation of icons, windows, and menus rather than text commands.
+ **Qt** is a cross-platform C++ application development framework that enables the creation of high-performance GUIs and native applications for desktop, embedded, and mobile platforms.

+ **QML** (Qt Modeling Language) is a declarative, JavaScript-based user interface specification and programming language within the Qt framework.
  + **QML**: A language used for defining UIs.
  + **Qt Quick**: The standard library and toolkit for QML, providing all necessary functional components including visuals, interactions, animations, and more.

`demo.qml`

```javascript
// Import core QML modules for UI components and controls
import QtQuick 2.15
import QtQuick.Controls 2.15

// Main application window container
ApplicationWindow {
    visible: true               	// Make the window appear on screen
    width: 400                  	// Set window width in pixels
    height: 300                 	// Set window height in pixels
    title: "Hello QML"          	// Title displayed in the window frame

    // A clickable button control
    Button {
        text: "Click me"         	// Label shown on the button
        anchors.centerIn: parent	// Position the button at the center of the window

        // Event handler triggered when the button is pressed and released
        onClicked: {
            console.log("Button clicked")// Output a message to the application console
        }
    }
}
```


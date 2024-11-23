# CircuitPython WebSocket Client

A lightweight WebSocket client library for CircuitPython. This library allows you to connect to WebSocket servers, send and receive data, and handle WebSocket frames with ease.

⚠️ **Work in Progress**: Some features may be incomplete or subject to change.

## Installation

1. Download the `cpwebsockets` folder from this repository and copy it to the root of your CircuitPython device.
2. Install the required dependency:
   - [`adafruit_logging`](https://github.com/adafruit/Adafruit_CircuitPython_Logging): Copy the `adafruit_logging` library to the `lib` folder on your CircuitPython device.

### Folder Structure
Your CircuitPython device should look like this:
```
code.py or
example.py
lib/
└── adafruit_logging.mpy
cpwebsockets/
├── client.py
└── protocol.py
```
## Usage

A minimal example is provided in the `example.py` file, demonstrating how to:
- Connect to a WebSocket server (`wss://ws.postman-echo.com/raw`).
- Send and receive messages.
- Close the WebSocket connection gracefully.

Simply copy the `example.py` file to your CircuitPython device and modify it as needed for your project.

## Compatibility

This library is designed to work with CircuitPython devices that support:
- Wi-Fi connections (via `wifi.radio`).
- TLS/SSL (for secure WebSocket connections using `wss://`).

### Tested on:
- [Lolin ESP32-S2](https://circuitpython.org/board/lolin_s2_mini/)
- [Lolin ESP32-S3](https://circuitpython.org/board/lolin_s3_mini/)
- [Raspberry Pi Pico RP2040 W](https://circuitpython.org/board/raspberry_pi_pico_w/)

If you encounter compatibility issues on other devices, please create an issue in this repository.

## Features

- Support for both `ws://` and `wss://` WebSocket protocols.
- Frame handling compliant with [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455).
- Client masking for secure communications.
- Text and binary message support.
- Graceful connection close handling.

## Known Issues & Limitations

- Continuation frames (`_OP_CONT`) are not yet implemented.
- The library has not been tested extensively on low-memory devices.
- Minimal support for WebSocket extensions.

## Contributing

We welcome contributions! If you'd like to report a bug, suggest a feature, or submit a pull request, please open an issue in this repository. Ensure your contributions adhere to CircuitPython's design guidelines.

## License

This library is released under the MIT License.

## Acknowledgments

This library is a CircuitPython adaptation of [uwebsockets](https://github.com/danni/uwebsockets) by danni.

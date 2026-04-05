# Weather Station Project

## Overview

This project provides a smart farm using a Raspberry Pi Pico 2W. Below are instructions on how to use the Makefile targets, install stubs, and configure the application.

## Makefile Targets

The `Makefile` includes several targets to streamline development and deployment. Here are the key targets:

- **`make deploy`**: Deploys all files from the pico directory to the Pico and runs the main.py script.
- **`make hard-reset`**: Performs a hard reset of the Pico.
- **`make soft-reset`**: Performs a soft reset of the Pico.
- **`make repl`**: Connects to the interactive REPL on the Pico.
- **`make ls`**: Lists all files on the Pico.
- **`make mount`**: Mounts the pico directory to the Pico for live editing.
- **`make unmount`**: Unmounts the Pico.

To use a target, run:

```bash
make <target>
```

## Installing Stubs

Stubs are required for development to provide type hints and autocompletion. To install them execute the following command:

```bash
pip install -U micropython-rp2-rpi_pico2_w-stubs --no-user --target ./typings
```

## Configuring the Application

The project includes a `configuration/config_example.py` file as a template for configuration. To set up your own configuration:

1. Copy `config_example.py` to `config.py`:
   
   ```bash
   cp config_example.py config.py
   ```

2. Open `config.py` and replace the placeholder values with your actual configuration settings.
3. Save the file.

## Notes

- Ensure you have mpremote installed for interacting with the Pico, to do that install `pipx` if you do not have it:

  ```bash
  sudo apt install pipx
  ```

  Then instal `mpremote`:

  ```bash
  pipx install mpremote
  ```
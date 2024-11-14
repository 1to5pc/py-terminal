![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/1to5pc/py-terminal/python-app-lint.yml?style=for-the-badge&label=Code%20Linting)

![GitHub repo size](https://img.shields.io/github/repo-size/1to5pc/py-terminal?style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/1to5pc/py-terminal?style=for-the-badge)

# Terminalx 🖥️ 

A modern, lightweight terminal emulator built in Python with a sleek interface and useful features.

## 🚀 Features

- Interactive Python environment
- Colorful command-line interface
- Smooth animations and progress indicators
- Cross-platform compatibility
- User-friendly boot sequence
- Simple and intuitive commands

## 📋 Requirements

- Python 3.9+
- Required dependencies:
  ```bash
  pip install -U colorama google-generativeai
  ```

## 🛠️ Installation

1. Download the latest release from the [releases tab](https://github.com/1to5pc/py-terminal/releases)
2. Extract the ZIP file to your desired location
3. Run `terminalx.py` in the /src/ directory:
   ```bash
   python terminalx.py
   ```
4. Add Your Gemini API Key to Environment Variables
- On Linux/MacOS
   ```bash
   export GEMINI_APIKEY="######YOURAPIKEY######"
   ```
- On Windows (Command Prompt)
   ```cmd
   set GEMINI_APIKEY=######YOURAPIKEY######
   ```
- On Windows (Powershell)
   ```powershell
   $env:GEMINI_APIKEY="######YOURAPIKEY######"
   ```
   
> [!note]
> To get a Gemini API Key go to [Google AI Studio](https://aistudio.google.com/app/apikey)
## 💻 Available Commands

| Command | Description |
|---------|-------------|
| `py`    | Enter Python environment |
| `fwrite`| Write user input to a configurable file |
| `ls`  | List files in the working directory |
| `help`  | Show available commands |
| `clear` | Clear the terminal screen |
| `exit`  | Exit Terminalx |

> [!note]
> `fwrite` uses the Gemini API and due the nature of LLMs its output may be unreliable

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Colorama](https://pypi.org/project/colorama/) for cross-platform colored output
- Inspired by modern terminal emulators

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/senhas-rgb" target="_blank">SenhasD</a>
</p>


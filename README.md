# 🚉 RExCL - Railway Exchange Configuration Language Tool

**RExCL** is a Python-based utility designed for Indian Railways (IR) to simplify the deployment and management of open-source VoIP exchanges. It automates the modification of core Asterisk configuration files using simple, predefined codes tailored for railway communication needs.

## 📖 Overview
The Railway Board has adopted open-source **Asterisk** for Inter-Railway communication. RExCL acts as an automation layer that allows telecom engineers to:
* 🛠️ **Automate Accounts**: Quickly create and manage user accounts.
* 📞 **Configure Dialplans**: Generate IR-compliant dialplans without manual file editing.
* ⚡ **Standardize Configs**: Ensure uniform configuration across different railway exchanges using predefined codes.

## 🚀 Key Features
* **Automated File Modification**: Modifies `sip.conf` and `extensions.conf` automatically.
* **Railway-Specific Logic**: Built-in templates for Inter-Railway numbering and communication standards.
* **Simplified Interface**: No deep knowledge of Asterisk scripting required for basic exchange setup.

## 🛠️ Installation
To set up RExCL on your Asterisk server, place the project files in the specific system share directory:

1. Create the directory:
   ```bash
   sudo mkdir -p /usr/local/share/rexcl/
2. Move the Python source files (including main.py) into that folder.
3. Ensure the user running the script has permissions to read/write to the Asterisk configuration directory (usually /etc/asterisk/).

## 💻 Usage
The tool uses predefined codes to configure railway exchanges . 
* To process an input file and update your Asterisk configurations, use the following command:
  ```bash
  python3 /usr/local/share/rexcl/main.py <input.rexcl>
* Replace <input.rexcl> with the path to your specific configuration script.

## 👥 Contributors
* **Initial Work**: Railway Board / Project Development Team
* *Detailed contributor list to be added later.*

## 📄 License
This project is intended for use within Indian Railways. 
**.

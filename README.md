# SCP Transfer Script

A user-friendly Python script for managing SCP (Secure Copy Protocol) file transfers between local and remote systems. This script provides an interactive menu interface for configuring connection settings and transferring files/directories securely.

## Features

- Interactive menu-driven interface
- Persistent configuration storage
- Support for both single file and directory transfers
- Custom SSH port configuration
- Cross-platform compatibility
- Clear terminal interface
- Ability to cancel operations with 'back' command

## Prerequisites

- Python 3.x
- SSH access to the remote system
- SCP installed on both local and remote systems

## Installation

1. Clone this repository or download the script:
``git clone https://github.com/nplachkov/scp-python-script.git && cd scp-python-script``

2. Make the script executable:
``chmod +x scp_transfer.py``

3. Install required Python packages:
``pip3 install pathlib``

## Usage

1. Run the script:
``python3 scp_transfer.py``

2. First-time setup:
   - Select option 1 to configure settings
   - Enter remote IP address
   - Enter remote username
   - Enter SSH port (default: 22)

3. Available options:
   - Configure Settings: Set up connection details
   - Send File/Directory: Transfer files to remote system
   - Receive File/Directory: Download files from remote system
   - Show Current Settings: View configured settings
   - Exit: Close the application

## Navigation

- Use number keys (1-5) to select menu options
- Type 'back' during file/directory operations to return to the main menu
- Press Enter after messages to continue

## Configuration

The script stores configuration in `scp_config.json` in the same directory. This includes:
- Remote IP address
- Remote username
- SSH port

## Examples

### Sending a File
1. Select option 2 (Send File/Directory)
2. Enter local file path (e.g., `/path/to/local/file.txt`)
3. Enter remote destination path (e.g., `/path/to/remote/file.txt`)
4. Choose whether it's a directory (y/N)

### Receiving a File
1. Select option 3 (Receive File/Directory)
2. Enter remote file path (e.g., `/path/to/remote/file.txt`)
3. Enter local destination path (e.g., `/path/to/local/file.txt`)
4. Choose whether it's a directory (y/N)

## Error Handling

The script includes comprehensive error handling for:
- Invalid inputs
- Connection failures
- File access issues
- Configuration errors

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) - see the LICENSE file for details.

## Acknowledgments

- Built using Python's subprocess module for secure file transfers
- Utilizes SCP protocol for encrypted file transfers
- Inspired by the need for a user-friendly SCP interface

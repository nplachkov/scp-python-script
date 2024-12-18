#!/usr/bin/env python3

import os
import json
import subprocess
from pathlib import Path

class SCPTransfer:
    def __init__(self):
        self.config_file = Path(__file__).parent / 'scp_config.json'
        self.config = self.load_config()

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_config(self):
        """Load configuration from JSON file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
        return {
            'remote_ip': '',
            'remote_user': '',
            'ssh_port': '22'
        }

    def save_config(self):
        """Save configuration to JSON file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            print("Configuration saved successfully!")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"Error saving config: {e}")
            input("\nPress Enter to continue...")

    def configure_settings(self):
        """Configure connection settings."""
        self.clear_screen()
        print("\n=== Configure Settings ===")
        self.config['remote_ip'] = input(f"Enter remote IP [{self.config['remote_ip']}]: ").strip() or self.config['remote_ip']
        self.config['remote_user'] = input(f"Enter remote username [{self.config['remote_user']}]: ").strip() or self.config['remote_user']
        self.config['ssh_port'] = input(f"Enter SSH port [{self.config['ssh_port']}]: ").strip() or self.config['ssh_port']
        self.save_config()

    def validate_settings(self):
        """Check if required settings are configured."""
        if not all([self.config['remote_ip'], self.config['remote_user']]):
            print("Error: Remote IP and username must be configured first.")
            input("\nPress Enter to continue...")
            return False
        return True

    def execute_scp(self, source, destination, is_directory=False):
        """Execute SCP command with the given parameters."""
        try:
            cmd = ['scp']
            if is_directory:
                cmd.append('-r')
            cmd.extend([
                '-P', self.config['ssh_port'],
                source,
                destination
            ])
            
            print(f"\nExecuting command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("Transfer completed successfully!")
            else:
                print(f"Error during transfer: {result.stderr}")
            
            input("\nPress Enter to continue...")
            return result.returncode == 0
        except Exception as e:
            print(f"Error executing SCP: {e}")
            input("\nPress Enter to continue...")
            return False

    def send_file(self):
        """Send file/directory to remote host."""
        if not self.validate_settings():
            return

        self.clear_screen()
        print("\n=== Send File/Directory ===")
        print("(Type 'back' to return to main menu)")
        local_path = input("Enter local file/directory path: ").strip()
        
        if local_path.lower() == 'back':
            return
        
        if not local_path:
            print("Error: Local path cannot be empty")
            input("\nPress Enter to continue...")
            return

        remote_path = input("Enter remote destination path: ").strip()
        if remote_path.lower() == 'back':
            return
        
        if not remote_path:
            print("Error: Remote path cannot be empty")
            input("\nPress Enter to continue...")
            return

        is_directory = input("Is this a directory? (y/N): ").lower()
        if is_directory == 'back':
            return
        
        is_directory = is_directory.startswith('y')
        
        remote_destination = f"{self.config['remote_user']}@{self.config['remote_ip']}:{remote_path}"
        self.execute_scp(local_path, remote_destination, is_directory)

    def receive_file(self):
        """Receive file/directory from remote host."""
        if not self.validate_settings():
            return

        self.clear_screen()
        print("\n=== Receive File/Directory ===")
        print("(Type 'back' to return to main menu)")
        remote_path = input("Enter remote file/directory path: ").strip()
        
        if remote_path.lower() == 'back':
            return
        
        if not remote_path:
            print("Error: Remote path cannot be empty")
            input("\nPress Enter to continue...")
            return

        local_path = input("Enter local destination path: ").strip()
        if local_path.lower() == 'back':
            return
        
        if not local_path:
            print("Error: Local path cannot be empty")
            input("\nPress Enter to continue...")
            return

        is_directory = input("Is this a directory? (y/N): ").lower()
        if is_directory == 'back':
            return
        
        is_directory = is_directory.startswith('y')
        
        remote_source = f"{self.config['remote_user']}@{self.config['remote_ip']}:{remote_path}"
        self.execute_scp(remote_source, local_path, is_directory)

    def show_current_settings(self):
        """Display current settings."""
        self.clear_screen()
        print("\n=== Current Settings ===")
        print(f"Remote IP: {self.config['remote_ip']}")
        print(f"Remote User: {self.config['remote_user']}")
        print(f"SSH Port: {self.config['ssh_port']}")
        input("\nPress Enter to continue...")

    def show_menu(self):
        """Display the main menu."""
        while True:
            self.clear_screen()
            print("\n=== SCP File Transfer Tool ===")
            print("1. Configure Settings")
            print("2. Send File/Directory")
            print("3. Receive File/Directory")
            print("4. Show Current Settings")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.configure_settings()
            elif choice == '2':
                self.send_file()
            elif choice == '3':
                self.receive_file()
            elif choice == '4':
                self.show_current_settings()
            elif choice == '5':
                self.clear_screen()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")

def main():
    scp = SCPTransfer()
    scp.show_menu()

if __name__ == "__main__":
    main() 
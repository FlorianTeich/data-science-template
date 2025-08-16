#!/usr/bin/env python3
"""
Main script demonstrating the use of lib_a package
"""

from lib_a import hello_world

def main():
    """Main function"""
    message = hello_world()
    print(message)
    print("Hello from completely-new!")

if __name__ == "__main__":
    main()

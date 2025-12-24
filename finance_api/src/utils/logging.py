# utils/logging.py
from colorama import Fore, Back, Style
import logging

def LoggingOperations(type, message):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    if type == "info":
        logging.info(f"{Fore.BLUE}{message}{Style.RESET_ALL}")
        
    elif type == "error":
        logging.error(f"{Fore.RED}{message}{Style.RESET_ALL}")

    elif type == "warning":
        logging.warning(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

    elif type == "debug":
        logging.error(f"{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}")




import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging() -> None:
    '''
    Console + (optional) file logging.
    Safe to call once at startup.
    '''
    log_format = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Avoid duplicate handlers if reload/import happens
    if root_logger.handlers:
        return
    
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format))
    root_logger.addHandler(console_handler)
    
    
    # File handler (rotating)
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)
    
    
    file_handler = RotatingFileHandler(
        logs_dir / 'app.log',
        maxBytes=1_000_000,  # ~1MB
        backupCount=3,
        encoding='utf-8',
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    root_logger.addHandler(file_handler)
# src/logger.py
import logging
import os

# Create a logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename=os.path.join("logs", "project.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

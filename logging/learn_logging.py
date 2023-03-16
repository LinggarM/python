import logging

# Set up logging configuration
logging.basicConfig(
    filename='example.log',  # specify the name of the log file
    level=logging.INFO,  # set the level of logging to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # specify the format of the log messages
)

# Example function that will log messages
def divide(a, b):
    try:
        result = a / b
        logging.info(f"Result: {result}")  # log the result
    except Exception as e:
        logging.error(f"Error occurred: {e}")  # log the error

# Call the function with some test values
divide(10, 2)
divide(10, 0)
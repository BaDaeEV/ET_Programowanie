import logging
from components.timestamp import getCurrentDate

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def writeToLog(topic, data, isSucces):
    date = getCurrentDate()
    if isSucces == 0:
        logging.info("Wysłano %s do %s", data, topic)
    elif isSucces == 1:
        logging.info("Nie udało się wysłać %s do %s", data, topic)
    else:
        logging.info("Unexpected error with status: %s", isSucces)
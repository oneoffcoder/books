import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(levelname)s:%(message)s',
)

logging.info('file logger ready')
logging.warning('watch this condition')

import time

from celery import current_app
from loguru import logger


@current_app.task(queue='hello')
def ola_mundo():
    time.sleep(3)
    logger.success('log: olá mundo')
    return 'olá mundo'


@current_app.task(queue='matematica')
def vezes_quatro(x):
    time.sleep(1)
    resultado = x * 4
    logger.success(resultado)
    return resultado


@current_app.task(queue='matematica')
def mais_y(x,y):
    time.sleep(1)
    resultado = x + y
    logger.success(resultado)
    return resultado


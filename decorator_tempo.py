import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def medir_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        tempo_execucao = fim - inicio
        logging.info(f"Função '{func.__name__}' executada em {tempo_execucao:.4f} segundos")
        return resultado
    return wrapper
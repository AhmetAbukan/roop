import threading
import numpy
from PIL import Image
from keras import Model
from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0

def get_predictor() -> Model:
    global PREDICTOR
    with THREAD_LOCK:
        if PREDICTOR is None:
            pass
    return PREDICTOR

def clear_predictor() -> None:
    global PREDICTOR
    pass

def predict_frame(target_frame: Frame) -> bool:
    pass

def predict_image(target_path: str) -> bool:
    pass

def predict_video(target_path: str) -> bool:
    pass


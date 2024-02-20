from typing import Optional
import cv2

from roop.typing import Frame


def get_gif_frame(gif_path: str, frame_number: int = 0) -> Optional[Frame]:
    capture = cv2.gifCapture(gif_path)
    frame_total = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    capture.set(cv2.CAP_PROP_POS_FRAMES, min(frame_total, frame_number - 1))
    has_frame, frame = capture.read()
    capture.release()
    if has_frame:
        return frame
    return None


def get_gif_frame_total(gif_path: str) -> int:
    capture = cv2.gifCapture(gif_path)
    gif_frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    return gif_frame_total

import logging
import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)


class SteganographyImg(object):
    """Class for Steganography based on images"""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.img = Image.open(self.src, "r")
        self.array = np.array(list(self.img.getdata()))
        self.width, self.height = self.img.size
        self.img_chan_n = self.__get_mode()
        self.n_pixels = self.array.size // self.img_chan_n
        pass

    def __del__(self):
        self.img.close()

    def encryptLSBImgText(self, msg, delim="$T0p") -> bool:
        payload = msg + delim
        b_message = "".join([format(ord(i), "08b") for i in payload])
        req_pixels = len(b_message)
        array = self.array
        if req_pixels > self.n_pixels:
            raise Exception("ERROR:" + self.src +
                            "needs to be a larger file size")
        else:
            index = 0
            for p in range(self.n_pixels):
                for q in range(0, 3):
                    if index < req_pixels:
                        array[p][q] = int(
                            bin(array[p][q])[2:9] + b_message[index], 2)
                        index += 1
            array = array.reshape(self.height, self.width, self.img_chan_n)
            enc_img = Image.fromarray(array.astype("uint8"), self.img.mode)
            enc_img.save(self.dest)
        return True

    def decryptLSBImg2Text(self, delim="$T0p") -> str:
        array = self.array
        hidden_bits = ""
        for p in range(self.n_pixels):
            for q in range(0, 3):
                hidden_bits += bin(array[p][q])[2:][-1]

        hidden_bits = [hidden_bits[i: i + 8]
                       for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-4:] == delim:
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        logger.debug(message)
        if delim in message:
            return message[:-4]
        else:
            return "No Hidden Message Found"

    def __get_mode(self) -> int:
        if self.img.mode == "RGB":
            n = 3
        elif self.img.mode == "RGBA":
            n = 4
        return n


if __name__ == "__main__":
    print("attempting to call a module as a main")
    exit(1)

import datetime
import os
from pathlib import Path
from ..steganography.steganography import *


ENV_VAR_TEMPDIR = "TELEGRAM_BOT_TEMP_DIR"
tb_tempdir = Path(os.getenv(ENV_VAR_TEMPDIR, "./bot_tmp"))
testing_dir = (
    "test_" + datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
)
testing_path = tb_tempdir / testing_dir
os.makedirs(testing_path.resolve(), exist_ok=True)

def test_encryptLSBImgTextPNG():
    img_in_path=Path("./steganobot/tests/test_resources/teka_no_message.png")
    img_out_path= testing_path / "LSBmsg_can_encrypt.png"
    encrypt = SteganographyImg(img_in_path,img_out_path.resolve()).encryptLSBImgText("Wake up!")
    assert encrypt == True

def test_encrypt_correct_out_LSBImgTextPNG():
    img_in_path=Path("./steganobot/tests/test_resources/teka_no_message.png")
    img_out_path=testing_path / "LSBmsg_same_output.png"
    SteganographyImg(img_in_path,img_out_path).encryptLSBImgText("Wake up!")
    ref_img_path=Path("./steganobot/tests/test_resources/teka_wake_up_default_delim.png")
    ref_img = open(ref_img_path.resolve(),"rb")
    img_out = open(img_out_path.resolve(),"rb")
    ref_content = ref_img.read()
    out_content = img_out.read()
    assert ref_content == out_content

def test_encrypt_decrypt_out_LSBImgTextPNG():
    img_in_path=Path("./steganobot/tests/test_resources/teka_no_message.png")
    img_out_path=testing_path / "LSBmsg_decrypt_output.png"
    SteganographyImg(img_in_path,img_out_path).encryptLSBImgText("Wake up!")
    msg = SteganographyImg(img_out_path,img_out_path).decryptLSBImg2Text()
    assert msg == "Wake up!"

def test_encrypt_decrypt_LSBImgTextJPEG():
    img_in_path=Path("./steganobot/tests/test_resources/teka_JPEG.jpg")
    img_out_path=testing_path / "LSBmsg_decryptJPG_output.png"
    SteganographyImg(img_in_path,img_out_path).encryptLSBImgText("Wake up!")
    msg = SteganographyImg(img_out_path,img_out_path).decryptLSBImg2Text()
    assert msg == "Wake up!"
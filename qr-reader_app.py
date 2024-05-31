from PIL import ImageGrab
from cv2 import QRCodeDetector
import streamlit as st
import numpy as np

def main():
    st.set_page_config(
        page_title="QR from clipboard",
        page_icon=":clipboard:",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items={
            'About': "Made by takamasa272"
        }
    )
    # big font
    st.write("<style>p{font-size: 1.2rem;}</style>", unsafe_allow_html=True)

    # website contents below
    st.title('QR code reader from Clipboard :clipboard:')
    st.write('USAGE: Copy image (contains QR codes) and reload this page.')
    st.divider()

    # grab image from clipboard
    clipImg = ImageGrab.grabclipboard()
    
    if clipImg == None:
        raise TypeError("No image is detected on your clipboard!")
    
    # decode QR code
    decoded_data = QR_decode(np.array(clipImg))
    if decoded_data == []:
        raise ValueError('There is no QR code!')
    
    st.header("Contents")
    # output decoded data
    for i, content in enumerate(decoded_data):
        st.write(i, content)


def QR_decode(clipImg: np.ndarray) -> list:
    qrd = QRCodeDetector()
    decoded_data = []

    # decode QR
    retval, decoded_info, points, _straight_qrcode = qrd.detectAndDecodeMulti(clipImg)

    if retval:
        points = points.astype(np.int64)

        for info in decoded_info:
            if info == '':
                continue
            decoded_data.append(info)
    
    return decoded_data

if __name__ == "__main__":
    main()
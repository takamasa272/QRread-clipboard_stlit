from streamlit_paste_button import paste_image_button
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
    paste_result = paste_image_button(
        label="📋 Paste an image",
        background_color="#3DA4B5",
        hover_background_color="#EEEEEE",
        errors='raise'
    )

    if paste_result.image_data is not None:
        clipImg = paste_result.image_data

        # decode QR code
        decoded_data = QR_decode(np.array(clipImg))
        if decoded_data == []:
            st.error('**Error**: No QR code found in clipboard', icon=':📋:')

        else:
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
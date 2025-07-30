import streamlit as st
import streamlit.components.v1 as components
import base64
import re

st.set_page_config(layout='wide', page_title='Hamburger maker!')
st.title('This is Jia Webpage')

# --------------------
# 이미지 Base64 인라인 변환 함수
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def inline_images_in_html(html, base_path='./'):
    pattern = r'<img\s+[^>]*src="([^"]+)"'
    matches = re.findall(pattern, html)
    
    for img_src in matches:
        if not img_src.startswith('http') and not img_src.startswith('data:'):
            img_path = base_path + img_src
            try:
                b64_str = img_to_base64(img_path)
                ext = img_src.split('.')[-1].lower()
                mime_type = f"image/{ext if ext != 'jpg' else 'jpeg'}"
                data_uri = f"data:{mime_type};base64,{b64_str}"
                html = html.replace(f'src="{img_src}"', f'src="{data_uri}"')
            except Exception as e:
                st.warning(f"이미지 인코딩 실패: {img_src} ({e})")
    return html

# --------------------
# hamburger.html 읽기 (그대로 사용)
with open('./hamburger.html', 'r', encoding='utf-8') as f:
    html_hamburger = f.read()

# oreo.html 읽고 이미지 인라인 처리 (base_path는 이미지 폴더 기준 경로)
with open('./oreo.html', 'r', encoding='utf-8') as f:
    html_oreo = f.read()

html_oreo_inlined = inline_images_in_html(html_oreo, base_path='./')

# checklist.html 읽기 (그대로 사용)
with open('./checklist.html', 'r', encoding='utf-8') as f:
    html_checklist = f.read()

# test.html 읽기 (그대로 사용)
with open('./test.html', 'r', encoding='utf-8') as f:
    html_test = f.read()

# --------------------
# 레이아웃 구성
col1, col2 = st.columns((4,1))

with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content...')
        st.video(url)

    with st.expander('Image content...'):
        imgfilepath = './image/gpt.png'
        st.image(imgfilepath)

    with st.expander('Content #2...'):
        components.html(html_hamburger, height=700)

    with st.expander('Content #3...'):
        components.html(html_oreo_inlined, height=1200)

    with st.expander('Content #4...'):
        components.html(html_checklist, height=1000)
    
    with st.expander('Content #5...'):
        components.html(html_test, height=4500)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by jia', unsafe_allow_html=True)

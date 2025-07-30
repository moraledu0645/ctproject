import streamlit as st
import streamlit.components.v1 as components
import base64
import re

st.set_page_config(layout='wide', page_title='CT problem solving program')
st.markdown("<h1 style='text-align: center; color: black;'>Moraledu World!</h1>", unsafe_allow_html=True)

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

    with st.expander('hamburger maker!'):
        components.html(html_hamburger, height=700)

    with st.expander('Guess the next Oreo!'):
        components.html(html_oreo_inlined, height=1200)

    with st.expander('Information reliability checklist'):
        components.html(html_checklist, height=1000)
    
    with st.expander('What type am I?'):
        components.html(html_test, height=4500)

with col2:
    with st.expander('💡 컴퓨팅 사고(Computational Thinking)란?'):
        st.info("""
    **컴퓨팅 사고(Computational Thinking, CT)**는 컴퓨터 과학자뿐만 아니라 누구나 배워서 활용할 수 있는 보편적인 문제 해결 방식입니다. 복잡한 문제를 컴퓨터가 효과적으로 처리할 수 있도록 정의하고 해결하는 사고 과정 전반을 의미합니다.

    주요 구성 요소는 다음과 같습니다:

    * **분해 (Decomposition)**: 복잡한 문제를 작고 다루기 쉬운 부분으로 나눕니다.
    * **패턴 인식 (Pattern Recognition)**: 문제나 데이터에서 반복되는 규칙, 경향, 공통적인 특성을 찾아냅니다.
    * **추상화 (Abstraction)**: 불필요한 세부 사항을 제거하고 문제의 핵심적인 요소를 추출하여 단순화합니다.
    * **알고리즘 (Algorithms)**: 문제를 해결하기 위한 단계적이고 논리적인 절차를 설계합니다.

    이러한 컴퓨팅 사고는 디지털 시대에 필요한 사고력, 문제 해결 능력, 그리고 창의력을 기르는 데 중요한 역할을 합니다. 단순히 코딩 기술을 배우는 것을 넘어, 어떤 분야에서든 논리적이고 효율적으로 문제를 해결하는 데 활용될 수 있습니다.
    """)

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by jia', unsafe_allow_html=True)

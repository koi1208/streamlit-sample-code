import streamlit as st

st.title('様々なサンプルを載せたアプリ')

'まずはページナビゲーション機能を作ってみた'

st.page_link('pages/viewer1.py', label='ビューワ１')
st.page_link('pages/viewer2.py', label='ビューワ２')
st.page_link('pages/viewer3.py', label='ビューワ３')
st.page_link('pages/viewer4.py', label='ビューワ４')
st.page_link('pages/viewer5.py', label='ビューワ５')

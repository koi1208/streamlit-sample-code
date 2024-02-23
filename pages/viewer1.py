import streamlit as st

ss = st.session_state

# 定数==========================================================================
N = 5

# 状態変数======================================================================
PAGE = 'viewer1-'
VIEW = PAGE + 'view'
def reset():
    ss[VIEW] = 0
def countup(n:int=1):
    ss[VIEW] += n
def countdown(n:int=1):
    ss[VIEW] -= n
if VIEW not in ss:
    reset()

# アプリ本体====================================================================
st.write('### ビューワ１')
st.divider()
if   ss[VIEW] == 0:
    st.write('#### ページタイトル1')
    st.write('コンテンツ：' + 'あ'*500)
    n = 0
elif ss[VIEW] == 1:
    st.write('#### ページタイトル2')
    st.write('コンテンツ：' + 'か'*500)
    n = 1
elif ss[VIEW] == 2:
    st.write('#### ページタイトル3')
    st.write('コンテンツ：' + 'さ'*500)
    n = 2
elif ss[VIEW] == 3:
    st.write('#### ページタイトル4')
    st.write('コンテンツ：' + 'た'*500)
    n = 3
else:
    st.write('#### ページタイトル5')
    st.write('コンテンツ：' + 'な'*500)
    n = 4
st.divider()
lt, ct, dt, rt = st.columns(4)
lt.caption(f'ページ {n+1}/{N}')
ct.button('次へ進む', None, None, countup, disabled=n==N-1)
dt.button('前へ戻る', None, None, countdown, disabled=n==0)
rt.button('リセット', None, None, reset)

import streamlit as st

ss = st.session_state

# 定数==========================================================================
N = 30
PAGETITLE = [f'#### ページタイトル{n+1}' for n in range(N)]
CONTENT = (list('あいうえおかきくけこ') * 100)[:N]

# 状態変数======================================================================
PAGE = 'viewer3-'
VIEW = PAGE + 'view'
def reset():
    ss[VIEW] = 0
def countup(n:int=1):
    ss[VIEW] += n
def countdown(n:int=1):
    ss[VIEW] -= n
def jump(n:int):
    ss[VIEW] = n
if VIEW not in ss:
    reset()

# 関数==========================================================================
def buttons(n:int):
    lt, ct, dt, rt = st.columns(4)
    lt.caption(f'ページ {n+1}/{N}')
    ct.button('次へ進む', None, None, countup, disabled=n==N-1)
    dt.button('前へ戻る', None, None, countdown, disabled=n==0)
    rt.button('リセット', None, None, reset)
    lt, rt = st.columns(2)
    lt.number_input('番号', 1, N, 1, 1, key='xx', label_visibility='collapsed')
    rt.button(f'{ss.xx}ページへ', None, None, jump, (ss.xx-1,))

# アプリ本体====================================================================
st.write('### ビューワ３')
st.divider()
n = ss[VIEW]
st.write(PAGETITLE[n])
st.write('コンテンツ：' + CONTENT[n]*500)
st.divider()
buttons(n)

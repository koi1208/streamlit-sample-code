import streamlit as st
# from contents.contents import show_content0
from contents.contents import show_content1

ss = st.session_state

# 定数==========================================================================
N:int = 30
PAGETITLE:list[str] = [f'#### ページタイトル{n+1}' for n in range(N)]
CONTENT:list[str] = (list('あいうえおかきくけこ') * 100)[:N]

# 状態変数======================================================================
PAGE:str = 'viewer5-'
VIEW:str = PAGE + 'view'
JUMP:str = PAGE + 'jump'
def reset():
    ss[VIEW] = 0
def countup(n:int=1):
    ss[VIEW] += n
def countdown(n:int=1):
    ss[VIEW] -= n
def jump():
    ss[VIEW] = ss[JUMP] - 1
if VIEW not in ss:
    reset()

# 関数==========================================================================
def buttons(n:int):
    col = st.columns(5)
    col[0].caption(f'ページ {n+1}/{N}')
    col[1].button('前へ戻る', None, None, countdown, disabled=n==0, use_container_width=True)
    col[2].number_input('番号', 1, N, n+1, 1, key=JUMP, on_change=jump, label_visibility='collapsed')
    col[3].button('次へ進む', None, None, countup, disabled=n==N-1, use_container_width=True)
    col[4].button('リセット', None, None, reset, use_container_width=True)

# アプリ本体====================================================================
st.write('### ビューワ５：コンテンツ外出し版')
st.divider()
n = ss[VIEW]
# show_content0(n)
show_content1(n)
st.divider()
buttons(n)

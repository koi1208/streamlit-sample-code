import streamlit as st

ss = st.session_state

# 定数==========================================================================
N = 30
PAGETITLE = [f'#### ページタイトル{n+1}' for n in range(N)]
CONTENT = (list('あいうえおかきくけこ') * 100)[:N]

# 状態変数======================================================================
PAGE = 'viewer4-'
VIEW = PAGE + 'view'
JUMP = PAGE + 'jump'
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
st.write('### ビューワ４：完成版')
st.divider()
n = ss[VIEW]
st.write(PAGETITLE[n])
st.write('コンテンツ：' + CONTENT[n]*500)
st.divider()
buttons(n)

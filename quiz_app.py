import streamlit as st

st.title("簡単なクイズアプリ")

question = "Streamlitは何を作るためのフレームワークですか？"
options = ["デスクトップアプリ", "Webアプリ", "ゲームアプリ"]

answer = st.radio(question, options)

if st.button("回答する"):
    if answer == "Webアプリ":
        st.success("正解！")
    else:
        st.error("不正解です。")

questions = [
    {"question": "Pythonは何のための言語ですか？", "options": ["データ分析", "写真編集", "音楽作成"], "answer": "データ分析"},
    {"question": "Streamlitは何のためのフレームワークですか？", "options": ["デスクトップアプリ", "Webアプリ", "ゲームアプリ"], "answer": "Webアプリ"}
]

for q in questions:
    st.write(q["question"])
    selected_option = st.radio("", q["options"])
    if st.button("回答する", key=q["question"]):
        if selected_option == q["answer"]:
            st.success("正解！")
        else:
            st.error("不正解です。")

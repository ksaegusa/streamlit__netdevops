import re 

import streamlit as st

st.set_page_config(layout="wide")
st.title("Regex")

log_file = ""
log_upload = st.toggle("ログアップロード")

if log_upload:
    log_file = st.file_uploader("ログアップロード")
else:
    text = st.text_area("テキスト貼り付け")

if log_file:
    text = log_file.getvalue().decode("utf-8")
    container = st.container(border=True, height=400)
    container.code(text, language="log")

regex_string = st.text_input("正規表現", "\s+")
if st.button("抽出"):
    lines = text.splitlines()
    res_lines = list()
    for line in lines:
        if re.match(rf"{regex_string}", line):
            res_lines.append(line)
    st.write(f"Condition: {regex_string}")
    st.write(f"Result   : Hit {len(res_lines)} lines")
    res_container = st.container(border=True, height=250)
    res_container.code("\n".join(res_lines), language="log")

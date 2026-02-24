import streamlit as st
import json
from pptx import Presentation
from io import BytesIO

# --- 認証機能 ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if st.session_state["password_correct"]:
        return True

    # 埋め込み表示（iframe）でも見やすいシンプルな画面
    st.write("### 認証が必要です")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if pwd == st.secrets["password"]:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("パスワードが違います")
    return False

# --- メイン画面 ---
if check_password():
    st.title("PPT Generator")
    st.caption("HTMLツールからJSONを貼り付けてください")

    json_input = st.text_area("JSON Paste Area", height=250)

    if st.button("パワーポイントを生成"):
        if json_input:
            try:
                data = json.loads(json_input)
                
                # パワポ作成
                prs = Presentation()
                slide = prs.slides.add_slide(prs.slide_layouts[0])
                slide.shapes.title.text = "Creative Brief"
                
                # サンプル：JSONの「プロジェクト名」などを反映
                # data['projectName'] など、HTMLツールの出力に合わせて調整可能
                
                ppt_out = BytesIO()
                prs.save(ppt_out)
                ppt_out.seek(0)

                st.download_button(
                    label="📥 PPTをダウンロード",
                    data=ppt_out,
                    file_name="brief.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
            except Exception as e:
                st.error(f"JSON形式を確認してください: {e}")

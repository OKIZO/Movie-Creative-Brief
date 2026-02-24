import streamlit as st
import json
from pptx import Presentation
from io import BytesIO

st.title("PPT Generator")
st.caption("HTMLツールからJSONを貼り付けてください")

json_input = st.text_area("JSON Paste Area", height=250)

if st.button("パワーポイントを生成"):
    if json_input:
        try:
            data = json.loads(json_input)
            
            prs = Presentation()
            slide = prs.slides.add_slide(prs.slide_layouts[0])
            slide.shapes.title.text = "Creative Brief"
            
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

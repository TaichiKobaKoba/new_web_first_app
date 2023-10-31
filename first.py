import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目":[1, 2, 3, 4],
    "2列目":[10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=1), width=500, height=500)#writeの違いは大きさを指定できる

st.table(df.style.highlight_max(axis=1))#静的な表を作りたいとき

"""
# 章
## 節
### 項

```python(pythonのコードを書く：マジックコマンド)
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.write(df2)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df3)

st.write("Interactive Widgets")

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list (range(1, 10))
)

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ1に関する解答")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ2に関する解答")
expander = st.expander("問い合わせ3")
expander.write("問い合わせ3に関する解答")

"あなたの好きな数字は",option,"です"

text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味：",text

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション：",condition

st.write("プログレスバーの表示")
"start!"

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"Interation {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
"Done!!"
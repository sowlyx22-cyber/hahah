import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(layout="wide")

# index.html içeriğini buraya yapıştır
html_kodu = """
<!DOCTYPE html>
<html>
<head>
    </head>
<body>
   ...
</body>
</html>
"""

# HTML'i Streamlit içinde göster
components.html(html_kodu, height=800, scrolling=True)

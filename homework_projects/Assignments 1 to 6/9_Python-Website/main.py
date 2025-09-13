import streamlit as st

# Page config
st.set_page_config(page_title="My Python Website", page_icon="🌐", layout="wide")

# Custom Dark Mode CSS
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .main {
            background-color: #0e1117;
            color: #ffffff;
        }
        .card {
            background-color: #1e222a;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.4);
            margin: 10px;
            color: #f1f1f1;
        }
        h1, h2, h3, h4 {
            color: #ffffff;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }
        .stButton button:hover {
            background-color: #45a049;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu
menu = st.sidebar.radio("Navigate", ["🏠 Home", "ℹ️ About", "📬 Contact"])

# Home Page
if menu == "🏠 Home":
    st.title("🌐 Welcome to My Professional Website")
    st.write("This is a modern website built with **Streamlit (Dark Mode)**.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🚀 Fast</h3><p>Runs instantly in your browser.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>📱 Responsive</h3><p>Works on all devices.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>🔒 Secure</h3><p>Made with Python & Streamlit.</p></div>', unsafe_allow_html=True)

# About Page
elif menu == "ℹ️ About":
    st.header("ℹ️ About Us")
    st.write("""
    We build **professional Python web apps** using Streamlit.  
    Streamlit makes it easy to create dashboards, tools, and apps.  
    This website now supports **Dark Mode UI** ✨
    """)

# Contact Page
elif menu == "📬 Contact":
    st.header("📬 Contact Us")
    st.write("Fill out the form below:")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        if name and email and message:
            st.success(f"✅ Thanks {name}, we got your message!")
        else:
            st.error("❌ Please fill all fields.")

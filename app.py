# --- 2. CSS TÙY CHỈNH (ĐÃ FIX LỖI CHỮ TÀNG HÌNH) ---
st.markdown("""
    <style>
    /* Giao diện cơ bản (Gender-Neutral) */
    .stApp {
        background-color: #F7F9F9;
    }
    
    /* FIX LỖI: Ép màu chữ tối cho toàn bộ văn bản và câu hỏi (label) để không bị chìm vào nền sáng */
    p, label, span, div[data-testid="stMarkdownContainer"] p {
        color: #1E2022 !important;
    }
    
    .main-title {font-size: 32px; font-weight: 800; color: #2B6777 !important; text-align: center; margin-bottom: 5px;}
    .subtitle {font-size: 16px; color: #52AB98 !important; text-align: center; font-style: italic; margin-bottom: 25px;}
    
    /* CSS cho Tooltip (Hiển thị kiến thức Marketing khi hover) */
    .tooltip {
        position: relative;
        display: inline-block;
        font-size: 24px;
        font-weight: 700;
        color: #1E2022 !important;
        cursor: help;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 2px dashed #52AB98; 
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 340px;
        background-color: #2B6777;
        color: #FFFFFF !important;
        text-align: left;
        border-radius: 8px;
        padding: 15px;
        position: absolute;
        z-index: 1;
        bottom: 130%;
        left: 50%;
        margin-left: -170px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 14.5px;
        font-weight: 400;
        line-height: 1.5;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.15);
    }
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -6px;
        border-width: 6px;
        border-style: solid;
        border-color: #2B6777 transparent transparent transparent;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
""", unsafe_allow_html=True)

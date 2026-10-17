import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Gương Soi Kỹ Thuật Số ✨", 
    page_icon="🌿", 
    layout="centered"
)

# --- 2. CSS TÙY CHỈNH (GIAO DIỆN NEUTRAL & TOOLTIP LÝ THUYẾT) ---
st.markdown("""
    <style>
    /* Giao diện cơ bản (Gender-Neutral) */
    .stApp {background-color: #F7F9F9;}
    .main-title {font-size: 32px; font-weight: 800; color: #2B6777; text-align: center; margin-bottom: 5px;}
    .subtitle {font-size: 16px; color: #52AB98; text-align: center; font-style: italic; margin-bottom: 25px;}
    
    /* CSS cho Tooltip (Hiển thị kiến thức Marketing khi hover) */
    .tooltip {
        position: relative;
        display: inline-block;
        font-size: 24px;
        font-weight: 700;
        color: #1E2022;
        cursor: help;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 2px dashed #52AB98; 
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 340px;
        background-color: #2B6777;
        color: #FFFFFF;
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

# --- 3. BANNER HÌNH ẢNH & LỜI CHÀO ---
# Banner mang hơi hướng wellness, tinh khiết, phù hợp mọi giới tính
st.image("https://images.unsplash.com/photo-1555820598-c801a1408dbb?q=80&w=1200&auto=format&fit=crop", use_container_width=True)

# Lời chào cá nhân hóa (Bạn có thể đổi "Nhung" thành tên biến lấy từ hệ thống đăng nhập nếu có)
st.markdown('<p class="main-title">Chào Nhung! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Hãy để chiếc gương kỹ thuật số này thiết kế liệu trình dành riêng cho bạn hôm nay.</p>', unsafe_allow_html=True)
st.divider()

# --- 4. PHẦN 1: ỨNG DỤNG 5.2.1 - BẢN CHẤT XÁC ĐỊNH VẤN ĐỀ ---
st.markdown("""
    <div class="tooltip">1. Phân Tích Hiện Trạng & Mục Tiêu
        <span class="tooltiptext"><b>📚 Ứng dụng 5.2.1: Bản chất xác định vấn đề</b><br>Kích hoạt nhu cầu bằng cách cho khách hàng thấy sự chênh lệch giữa 'Trạng thái thực tế' (da hiện tại) và 'Trạng thái mong muốn' (mục tiêu).</span>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    thuc_te = st.selectbox("Hiện tại da bạn đang gặp tình trạng gì?", 
                           ["Đổ nhiều dầu, dễ nổi mụn", "Khô ráp, bong tróc", "Xỉn màu, mệt mỏi", "Bình thường"])
with col2:
    mong_muon = st.selectbox("Mục tiêu bạn hướng tới là gì?", 
                             ["Sạch mụn, kiểm soát dầu", "Cấp ẩm sâu, căng mọng", "Sáng khỏe, đều màu", "Duy trì phong độ"])

if st.button("Phân tích dữ liệu 🔍"):
    with st.spinner('Hệ thống đang đối chiếu trạng thái...'):
        time.sleep(1.5)
    st.info(f"📊 **Báo cáo:** Trạng thái da hiện tại của bạn đang cách mục tiêu '{mong_muon}' khoảng **40%**. Chúng ta cần tập trung vào việc cân bằng lại độ ẩm và bảo vệ hàng rào da!")

st.divider()

# --- 5. PHẦN 2: ỨNG DỤNG 5.2.3 & 5.2.4 - YẾU TỐ NGOẠI CẢNH & TÂM TRẠNG ---
st.markdown("""
    <div class="tooltip">2. Nhịp Sống & Cảm Xúc Hôm Nay
        <span class="tooltiptext"><b>📚 Ứng dụng 5.2.3 & 5.2.4:</b><br>- <b>Ngoại cảnh (Không kiểm soát):</b> Thời tiết, mùa thi cử, deadline.<br>- <b>Nghiên cứu cảm xúc:</b> Dựa vào Mood Tracker để đề xuất giải pháp chữa lành tinh thần thay vì chỉ bán sản phẩm vật lý.</span>
    </div>
""", unsafe_allow_html=True)

thoi_tiet = st.radio("Thời tiết khu vực của bạn hôm nay ra sao?", 
                     ["Nắng gắt / Khô hanh ☀️", "Mưa ẩm / Lạnh 🌧️", "Ngồi phòng máy lạnh ❄️"], 
                     horizontal=True)

hoat_dong = st.selectbox("Nhịp độ cuộc sống gần đây của bạn thế nào?", 
                         ["Đang chạy deadline / Sắp thi cuối kỳ 📚", "Di chuyển nhiều ngoài trời / Khói bụi 🛵", "Nhịp sống cân bằng, ổn định 🍵"])

mood = st.select_slider("Mức độ căng thẳng (Stress level) của bạn hiện tại?", 
                        options=["Rất mệt mỏi", "Áp lực", "Bình thường", "Thoải mái", "Tràn đầy năng lượng"], 
                        value="Áp lực")

if mood in ["Rất mệt mỏi", "Áp lực"] or "deadline" in hoat_dong.lower():
    st.success("🌿 **Góc Chữa Lành:** Trạng thái tinh thần ảnh hưởng trực tiếp đến làn da. Một chiếc mặt nạ làm dịu, chút tinh dầu tràm trà và một playlist Lofi sẽ giúp bạn lấy lại sự tập trung và giảm stress ngay lúc này!")

st.divider()

# --- 6. PHẦN 3: ỨNG DỤNG 5.2.2 - KÍCH HOẠT VẤN ĐỀ & GIẢI PHÁP ---
st.markdown("""
    <div class="tooltip">3. Phác Đồ Dành Riêng Cho Bạn
        <span class="tooltiptext"><b>📚 Ứng dụng 5.2.2: Các loại vấn đề</b><br>- <b>Vấn đề đã kích hoạt:</b> Đưa giải pháp trực tiếp (Sữa rửa mặt, mặt nạ).<br>- <b>Vấn đề chưa kích hoạt:</b> Dùng bài toán nhận thức (Tác hại ánh sáng xanh) để tạo nhu cầu cho sản phẩm mới.</span>
    </div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Giải pháp tức thì (Sản phẩm tối ưu)", "Góc khám phá (Góc nhìn mới)"])

with tab1:
    st.subheader("Gợi ý phù hợp nhất lúc này")
    if "dầu" in thuc_te.lower() or "bụi" in hoat_dong.lower():
        st.write("🎯 **Trọng tâm: Làm sạch sâu & Kiểm soát bã nhờn**")
        st.markdown("- **Bước 1:** Gel rửa mặt dịu nhẹ, cân bằng độ pH (VD: La Roche-Posay / Cerave).")
        st.markdown("- **Bước 2:** Toner chiết xuất thiên nhiên giúp kháng viêm.")
    else:
        st.write("🎯 **Trọng tâm: Phục hồi & Cấp ẩm**")
        st.markdown("- **Bước 1:** Kem dưỡng ẩm phục hồi chuyên sâu ban đêm.")
        st.markdown("- **Bước 2:** Mặt nạ cấp nước giúp làm dịu tức thì.")

with tab2:
    st.subheader("💡 Bạn có biết?")
    st.warning("💻 **Cảnh báo từ màn hình:** Việc thức khuya dùng điện thoại/laptop để chạy deadline phát ra lượng lớn ánh sáng xanh. Điều này không chỉ gây mỏi mắt mà còn kích thích sản sinh gốc tự do, làm da sạm đi 20% và lão hóa sớm!")
    st.markdown("Chỉ rửa mặt là **CHƯA ĐỦ**. Dù không ra đường, bạn vẫn cần áp dụng **Làm Sạch Kép (Double Cleansing)** để loại bỏ bã nhờn và lớp kem chống nắng.")
    st.button("Khám phá ngay: Dòng nước tẩy trang không cồn bảo vệ màng da ➔")

# --- FOOTER ---
st.markdown("<br><hr><center><small>Dự án Hành vi Người tiêu dùng - Thiết kế bởi Nhung ✨</small></center>", unsafe_allow_html=True)

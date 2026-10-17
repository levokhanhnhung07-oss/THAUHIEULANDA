import streamlit as st
import time

# ==========================================
# 1. CẤU HÌNH TRANG & GIAO DIỆN TỐI GIẢN (MINIMAL & ELEGANT)
# ==========================================
st.set_page_config(page_title="Skin & Lifestyle Quiz", page_icon="✨", layout="centered")

# CSS thiết kế tỉ mỉ: Bo góc mềm mại, font chữ thanh lịch, hiệu ứng hover, tooltip xịn xò
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Quicksand:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #2c3e50;
    }

    /* Tooltip xịn xò khi hover/ấn giữ nhẹ */
    .tooltip-container {
        position: relative;
        display: inline-block;
        border-bottom: 1px dashed #a3b1c6;
        cursor: pointer;
        color: #4a5568;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .tooltip-container .tooltip-text {
        visibility: hidden;
        width: 320px;
        background-color: #f7fafc;
        color: #2d3748;
        text-align: left;
        border-radius: 12px;
        padding: 15px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -160px;
        opacity: 0;
        transition: opacity 0.4s;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        font-size: 0.95rem;
        font-family: 'Quicksand', sans-serif;
        border: 1px solid #e2e8f0;
        font-weight: 400;
    }
    .tooltip-container:hover .tooltip-text, .tooltip-container:active .tooltip-text {
        visibility: visible;
        opacity: 1;
    }

    /* Tùy chỉnh nút bấm */
    div.stButton > button:first-child {
        background-color: #2c3e50;
        color: white;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s ease;
        font-weight: 600;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #a3b1c6;
        color: #2c3e50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Box thẩm mỹ */
    .product-box {
        background-color: #fcfcfc;
        border: 1px solid #f0f0f0;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. HỆ THỐNG ĐIỀU HƯỚNG TRANG (SESSION STATE)
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'nickname' not in st.session_state:
    st.session_state.nickname = ""

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# ==========================================
# TRANG 0: BẮT ĐẦU VÀ NHẬP BIỆT DANH
# ==========================================
if st.session_state.page == 0:
    st.markdown("<h1 style='text-align: center;'>✨ Chạm vào vẻ đẹp đích thực</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #718096;'>Hành trình thấu hiểu làn da và cảm xúc của riêng bạn.</p>", unsafe_allow_html=True)
    
    # Đoạn gắn hình ảnh thật xinh theo yêu cầu
    st.image("https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&q=80&w=1000", use_container_width=True)
    
    st.write("---")
    nickname_input = st.text_input("Hãy cho hệ thống biết biệt danh của bạn:", placeholder="Nhập tên gọi yêu thích của bạn...")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Bắt đầu khám phá ➔"):
            if nickname_input.strip():
                st.session_state.nickname = nickname_input
                next_page()
            else:
                st.warning("Vui lòng nhập tên để website có thể gọi bạn một cách thân thương nhất nhé!")

# ==========================================
# TRANG 1: 5.2.1 BẢN CHẤT CỦA XÁC ĐỊNH VẤN ĐỀ
# ==========================================
elif st.session_state.page == 1:
    st.markdown(f"## Chào {st.session_state.nickname}! 🤍")
    
    st.markdown('''
        <div class="tooltip-container">
            1. Gương Soi Kỹ Thuật Số (Skin & Lifestyle Quiz)
            <span class="tooltip-text">
                <b>Ứng dụng 5.2.1: Bản chất xác định vấn đề</b><br><br>
                Quá trình ra quyết định mua sắm diễn ra khi khách hàng nhận thức được sự chênh lệch đủ lớn giữa <b>Trạng thái thực tế</b> (VD: Da đổ dầu, stress) và <b>Trạng thái mong muốn</b> (VD: Da căng bóng, thư giãn).
            </span>
        </div>
    ''', unsafe_allow_html=True)

    st.write("Hãy để hệ thống chẩn đoán hiện trạng của bạn nhé:")
    
    col1, col2 = st.columns(2)
    with col1:
        thuc_te = st.selectbox("📍 Trạng thái thực tế của bạn:", 
                               ["Đang đổ dầu, nổi mụn", "Mệt mỏi, stress vì deadline", "Da khô ráp, thiếu sức sống"])
    with col2:
        mong_muon = st.selectbox("✨ Trạng thái mong muốn:", 
                                 ["Da căng bóng, sạch mụn", "Thư giãn tinh thần, tự tin", "Ẩm mượt, rạng rỡ"])

    if st.button("🔍 Quét tình trạng"):
        with st.spinner("Đang phân tích dữ liệu..."):
            time.sleep(1.5)
        st.write("---")
        st.markdown(f"### 📊 Báo cáo Nhận thức vấn đề của {st.session_state.nickname}")
        
        # Chỉ số mô phỏng sự chênh lệch
        col_metric1, col_metric2 = st.columns(2)
        col_metric1.metric(label="Mức độ đạt chuẩn hiện tại", value="60%", delta="-40% (Khoảng hụt)")
        
        st.error(f"**Cảnh báo:** Da và tinh thần của bạn đang **thiếu 40% độ ẩm và năng lượng** so với mức lý tưởng. Sự chênh lệch giữa việc '{thuc_te.lower()}' và mong muốn '{mong_muon.lower()}' đã kích hoạt quy trình ra quyết định mua sắm của bạn ngay lúc này!")

    st.write("---")
    st.button("Tiếp theo: Giải pháp ➔", on_click=next_page)

# ==========================================
# TRANG 2: 5.2.2 CÁC LOẠI VẤN ĐỀ CỦA NGƯỜI TIÊU DÙNG
# ==========================================
elif st.session_state.page == 2:
    st.markdown('''
        <div class="tooltip-container">
            2. Các Loại Vấn Đề Của Người Tiêu Dùng
            <span class="tooltip-text">
                <b>Ứng dụng 5.2.2: Phân loại vấn đề</b><br><br>
                - <b>Đã kích hoạt:</b> Khách đã biết mình cần gì (VD: Kem chống nắng, mặt nạ). Cần tối ưu SEO, bộ lọc để đưa sản phẩm tốt nhất lên đầu.<br>
                - <b>Chưa kích hoạt:</b> Khách không biết tác hại của ánh sáng xanh. Cần giáo dục, cảnh báo trước khi bán hàng.
            </span>
        </div>
    ''', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎯 Vấn đề ĐÃ kích hoạt", "🌙 Vấn đề CHƯA kích hoạt"])
    
    with tab1:
        st.write(f"Hệ thống nhận thấy {st.session_state.nickname} đang chủ động tìm kiếm các sản phẩm trị mụn & bảo vệ da.")
        st.markdown("🔍 *Bộ lọc đang được tối ưu hóa: Hiển thị Giải pháp làm dịu da mụn tốt nhất*")
        
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.markdown("<div class='product-box'>💧<br><b>La Roche-Posay</b><br><small>Sữa rửa mặt dịu nhẹ</small></div>", unsafe_allow_html=True)
        with col_p2:
            st.markdown("<div class='product-box'>☀️<br><b>Bioré</b><br><small>Kem chống nắng phổ rộng</small></div>", unsafe_allow_html=True)
        with col_p3:
            st.markdown("<div class='product-box'>🌿<br><b>Banobagi</b><br><small>Mặt nạ thạch trị mụn</small></div>", unsafe_allow_html=True)

    with tab2:
        st.markdown(f"### 🚨 Góc cảnh báo dành cho {st.session_state.nickname}")
        st.warning(f"**Bạn có biết?** Việc thức khuya chạy deadline và nhìn màn hình điện thoại liên tục phát ra ánh sáng xanh đang làm **da sạm đi 20%** và đẩy nhanh quá trình lão hóa.")
        st.info("👉 *Gợi ý sau khi nhận thức vấn đề:* Đã đến lúc bạn cần bổ sung **Dòng sản phẩm phục hồi ban đêm** vào chu trình skincare của mình.")

    st.write("---")
    c1, c2 = st.columns(2)
    c1.button("⬅ Quay lại", on_click=prev_page)
    c2.button("Tiếp theo: Yếu tố ngoại cảnh ➔", on_click=next_page)

# ==========================================
# TRANG 3: 5.2.3 KHÔNG KIỂM SOÁT GIỚI HẠN XÁC NHẬN VẤN ĐỀ
# ==========================================
elif st.session_state.page == 3:
    st.markdown('''
        <div class="tooltip-container">
            3. Yếu Tố Ngoại Cảnh (Phi Thị Trường)
            <span class="tooltip-text">
                <b>Ứng dụng 5.2.3: Yếu tố ngoại cảnh</b><br><br>
                Những thay đổi ngoài dự kiến như thời tiết chuyển mùa, chuyển nhà, nhập học hay mùa thi cử... làm thay đổi trạng thái thực tế, tạo ra vấn đề mới mà doanh nghiệp không trực tiếp tạo ra.
            </span>
        </div>
    ''', unsafe_allow_html=True)
    
    st.write("📍 **Tính năng Thời tiết & Nhịp sống**")
    st.caption("Hãy cập nhật biến động cuộc sống hiện tại để website đề xuất chính xác nhất nhé:")
    
    ngoai_canh = st.radio("Hiện tại bạn đang đối mặt với điều gì?", 
                          ["Sài Gòn đang vào mùa mưa lạnh / nắng gắt", 
                           "Vừa nhập học đại học, bắt đầu môi trường mới",
                           "Chuẩn bị bước vào mùa thi cử sát nút"])

    st.write("---")
    if ngoai_canh == "Chuẩn bị bước vào mùa thi cử sát nút":
        st.error(f"📚 **Hệ thống tự động đề xuất:** Mùa thi sát nút rồi {st.session_state.nickname} ơi! Sắm ngay **bộ mặt nạ thạch thư giãn** và **tinh dầu** để giảm stress nhé!")
    elif ngoai_canh == "Sài Gòn đang vào mùa mưa lạnh / nắng gắt":
        st.info(f"🌦️ **Hệ thống tự động đề xuất:** Thời tiết Sài Gòn đang làm da dễ kích ứng. {st.session_state.nickname} cần ngay một lớp màng bảo vệ và cấp ẩm chuyên sâu.")
    else:
        st.success(f"🎓 **Hệ thống tự động đề xuất:** Vừa nhập học là phải thật xinh đẹp! Cùng xây dựng một chu trình dưỡng da tối giản để luôn tỏa sáng tại trường nhé.")

    st.write("---")
    c1, c2 = st.columns(2)
    c1.button("⬅ Quay lại", on_click=prev_page)
    c2.button("Tiếp theo: Chiến lược Marketing ➔", on_click=next_page)

# ==========================================
# TRANG 4: 5.2.4 CHIẾN LƯỢC MARKETING
# ==========================================
elif st.session_state.page == 4:
    st.markdown('''
        <div class="tooltip-container">
            4. Chiến Lược Marketing & Nhận Thức
            <span class="tooltip-text">
                <b>Ứng dụng 5.2.4: Chiến lược Marketing</b><br><br>
                - <b>Phân tích hoạt động:</b> Tìm điểm đau (pain point) dựa trên hoạt động thường ngày.<br>
                - <b>Nghiên cứu cảm xúc:</b> Chữa lành tinh thần qua các yếu tố văn hóa phương Đông.<br>
                - <b>Nhận biết chung vs Chọn lọc:</b> Giáo dục vấn đề chung trước (cần tẩy trang), sau đó chốt sale bằng sản phẩm độc quyền.
            </span>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 🏃‍♀️ 1. Skincare theo hoàn cảnh (Hoạt động)")
    hoat_dong = st.selectbox(f"{st.session_state.nickname} thường xuyên làm gì nhất?", 
                             ["Thường xuyên đi xe máy đường bụi", "Hay ngồi điều hòa 8 tiếng/ngày"])
    if hoat_dong == "Thường xuyên đi xe máy đường bụi":
        st.success("🛵 **Điểm đau (Pain point):** Bụi mịn bít tắc lỗ chân lông. \n\n👉 **Combo giải quyết:** Sữa tắm làm sạch sâu & Xịt khoáng bảo vệ màng da.")
    else:
        st.success("❄️ **Điểm đau (Pain point):** Hút hết độ ẩm của da. \n\n👉 **Combo giải quyết:** Kem dưỡng khóa ẩm sâu & Xịt khoáng cấp nước 2h/lần.")

    st.write("---")
    st.markdown("### 🧘‍♀️ 2. Theo dõi tâm trạng (Mood Tracker)")
    mood = st.select_slider("Cảm xúc hôm nay của bạn thế nào?", options=["Rất căng thẳng", "Mệt mỏi", "Bình yên", "Tích cực"])
    
    if mood in ["Rất căng thẳng", "Mệt mỏi"]:
        st.markdown(f"""
        <div style="background-color: #fcebeb; padding: 20px; border-radius: 15px; border-left: 5px solid #ff6b6b;">
            <b>🔮 Góc Chữa Lành Tâm Hồn:</b><br>
            Hôm nay {st.session_state.nickname} đã vất vả rồi. Trang web không chỉ bán mỹ phẩm cho bạn đâu. 
            Hệ thống gợi ý bạn một set <b>Nến thơm & Trà thảo mộc</b>. Đặc biệt, chúng mình vừa mở khóa góc nhỏ <b>Xem năng lượng các chòm sao (Astrology/Zodiac)</b> để giúp bạn tìm lại sự cân bằng tinh thần đó!
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"Thật tuyệt vời {st.session_state.nickname}! Năng lượng tích cực sẽ giúp da bạn đẹp lên mỗi ngày.")

    st.write("---")
    st.markdown("### 💡 3. Nhận biết Chung & Chọn lọc")
    with st.expander("Giai đoạn 1: Giáo dục Nhận biết chung (Mở để xem)", expanded=True):
        st.write("🧼 **Chiến dịch Double Cleansing:** Bạn có biết rửa mặt bằng sữa rửa mặt thôi là CHƯA ĐỦ để sạch sâu?")
    
    with st.expander("Giai đoạn 2: Kích hoạt Nhận biết chọn lọc (Mở để xem)", expanded=True):
        st.write("🌿 Khi bạn đã hiểu tầm quan trọng của việc tẩy trang, Website giới thiệu ngay: **Dòng nước tẩy trang ĐỘC QUYỀN của nền tảng - Cam kết Không Cồn, An Toàn Tuyệt Đối.**")

    st.write("---")
    c1, c2 = st.columns(2)
    c1.button("⬅ Quay lại", on_click=prev_page)
    c2.button("🔄 Hoàn thành & Trải nghiệm lại", on_click=lambda: st.session_state.update(page=0, nickname=""))

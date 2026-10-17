import streamlit as st
import time

# 1. CẤU HÌNH TRANG & GIAO DIỆN TỐI GIẢN (MINIMAL, ELEGANT)
st.set_page_config(page_title="Gương Soi Kỹ Thuật Số", page_icon="✨", layout="centered")

# CSS tùy chỉnh để làm đẹp UI, ẩn các đường viền cứng, tạo cảm giác bo tròn, thanh lịch
st.markdown("""
    <style>
    .tooltip-header {
        border-bottom: 2px dotted #b0c4de;
        display: inline-block;
        cursor: help;
        color: #2c3e50;
    }
    div.stButton > button:first-child {
        border-radius: 20px;
        background-color: #f7f9fa;
        border: 1px solid #dcdcdc;
        color: #2c3e50;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #e3e8ec;
        border-color: #b0c4de;
    }
    </style>
""", unsafe_allow_html=True)

# 2. KHỞI TẠO SESSION STATE ĐỂ CHUYỂN TRANG
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'nickname' not in st.session_state:
    st.session_state.nickname = ""

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# ==========================================
# TRANG 0: NHẬP BIỆT DANH TRƯỚC KHI BẮT ĐẦU
# ==========================================
if st.session_state.page == 0:
    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>✨ Chạm để khám phá bản thân</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
        <p style='text-align: center;'>Trước khi bắt đầu hành trình, hãy cho hệ thống biết tên gọi yêu thích của bạn nhé.</p>
    """, unsafe_allow_html=True)
    
    nickname_input = st.text_input("Biệt danh xinh đẹp của bạn là:", placeholder="Ví dụ: Nhung...")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Bắt đầu trải nghiệm ➔", use_container_width=True):
            if nickname_input.strip():
                st.session_state.nickname = nickname_input
                next_page()
            else:
                st.warning("Vui lòng nhập tên để tiếp tục nha!")

# ==========================================
# TRANG 1: 5.2.1 BẢN CHẤT CỦA XÁC ĐỊNH VẤN ĐỀ
# ==========================================
elif st.session_state.page == 1:
    st.markdown(f"## Chào {st.session_state.nickname}! 🌸")
    
    # Khu vực chèn ảnh xinh
    st.image("https://images.unsplash.com/photo-1512496015851-a1c8dcbc7d43?auto=format&fit=crop&q=80&w=800", caption="Vẻ đẹp rạng rỡ từ sự thấu hiểu bản thân", use_container_width=True)
    
    st.write("---")
    # Tiêu đề có Tooltip (Ấn giữ/Hover để đọc lý thuyết)
    st.markdown('''
        <h3 class="tooltip-header" title="LÝ THUYẾT 5.2.1: Quá trình ra quyết định mua sắm bắt đầu khi khách hàng nhận ra sự chênh lệch đủ lớn giữa trạng thái thực tế (hiện tại) và trạng thái mong muốn (lý tưởng).">
        1. Gương Soi Kỹ Thuật Số (Skin & Lifestyle Quiz)
        </h3>
    ''', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        thuc_te = st.selectbox("Trạng thái thực tế:", ["Đang đổ dầu, nổi mụn", "Khô ráp, thiếu ẩm", "Mệt mỏi, stress vì deadline"])
    with col2:
        mong_muon = st.selectbox("Trạng thái mong muốn:", ["Da căng bóng, sạch sẽ", "Ẩm mượt, rạng rỡ", "Thư giãn tinh thần, tự tin"])

    if st.button("🔍 Phân tích ngay"):
        with st.spinner("Hệ thống đang so sánh trạng thái..."):
            time.sleep(1)
        st.success(f"**Báo cáo:** {st.session_state.nickname} thân mến, trạng thái của bạn đang có sự chênh lệch. Bạn đang ưu tiên giải quyết vấn đề '{thuc_te.lower()}' để đạt được cảm giác '{mong_muon.lower()}'. Da/Tinh thần của bạn đang thiếu 40% năng lượng so với mức lý tưởng. Hãy để hệ thống thiết kế giải pháp cho bạn nhé!")

    st.write("---")
    st.button("Tiếp theo ➔", on_click=next_page, key="btn_next_1")

# ==========================================
# TRANG 2: 5.2.2 CÁC LOẠI VẤN ĐỀ
# ==========================================
elif st.session_state.page == 2:
    st.markdown('''
        <h3 class="tooltip-header" title="LÝ THUYẾT 5.2.2: Vấn đề kích hoạt (KH đã nhận thức được nhu cầu và chủ động tìm kiếm). Vấn đề chưa kích hoạt (KH không biết mình có vấn đề, Marketer cần giáo dục và cảnh báo).">
        2. Giải mã vấn đề của bạn
        </h3>
    ''', unsafe_allow_html=True)
    st.write("---")

    tab1, tab2 = st.tabs(["💡 Vấn đề đã kích hoạt", "🌙 Vấn đề chưa kích hoạt"])
    
    with tab1:
        st.write("Bạn đã biết mình cần gì! Dưới đây là các giải pháp ưu việt được đưa lên hàng đầu:")
        st.info("**Giải pháp làm dịu da mụn & cấp ẩm:** \n\n✨ Gợi ý cho bạn các dòng sản phẩm chất lượng từ La Roche-Posay, Bioré, và mặt nạ Banobagi.")
        
    with tab2:
        st.write("Góc cảnh báo sức khỏe làn da:")
        st.warning(f"**{st.session_state.nickname} có biết?** Thức khuya dùng điện thoại phát ra ánh sáng xanh có thể làm da sạm đi 20% và đẩy nhanh lão hóa. \n\n👉 *Đề xuất:* Đã đến lúc bổ sung dòng sản phẩm phục hồi ban đêm vào chu trình skincare của bạn!")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Quay lại", on_click=prev_page)
    with col2:
        st.button("Tiếp theo ➔", on_click=next_page, key="btn_next_2")

# ==========================================
# TRANG 3: 5.2.3 YẾU TỐ NGOẠI CẢNH
# ==========================================
elif st.session_state.page == 3:
    st.markdown('''
        <h3 class="tooltip-header" title="LÝ THUYẾT 5.2.3: Các yếu tố phi thị trường (như thời tiết, sự kiện cá nhân đột xuất) làm thay đổi trạng thái thực tế một cách thụ động, từ đó kích hoạt nhu cầu mới mà doanh nghiệp không trực tiếp kiểm soát được.">
        3. Thời tiết & Nhịp sống
        </h3>
    ''', unsafe_allow_html=True)
    st.write("---")

    ngoai_canh = st.radio("Cập nhật nhịp sống hiện tại của bạn:", 
                          ["Thời tiết Sài Gòn đang thay đổi thất thường", 
                           "Đang bước vào mùa thi cử căng thẳng", 
                           "Vừa nhập học/Bắt đầu môi trường mới"])

    if ngoai_canh == "Đang bước vào mùa thi cử căng thẳng":
        st.error(f"📚 Mùa thi sát nút rồi {st.session_state.nickname} ơi! Sắm ngay bộ mặt nạ thạch thư giãn và chút tinh dầu để giảm stress nhé!")
    elif ngoai_canh == "Thời tiết Sài Gòn đang thay đổi thất thường":
        st.info("🌧️ Nắng mưa thất thường làm da dễ nhạy cảm. Hãy chú trọng khâu làm sạch và bảo vệ da tuyệt đối!")
    else:
        st.success("🌟 Môi trường mới, năng lượng mới! Hãy tự tin tỏa sáng với phong thái rạng rỡ nhất.")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Quay lại", on_click=prev_page)
    with col2:
        st.button("Tiếp theo ➔", on_click=next_page, key="btn_next_3")

# ==========================================
# TRANG 4: 5.2.4 CHIẾN LƯỢC MARKETING
# ==========================================
elif st.session_state.page == 4:
    st.markdown('''
        <h3 class="tooltip-header" title="LÝ THUYẾT 5.2.4: Marketer chủ động phát hiện vấn đề qua phân tích hoạt động, nghiên cứu cảm xúc, và tạo ra sự nhận biết chung (kích thích nhu cầu cơ bản) hoặc nhận biết chọn lọc (kích thích mua thương hiệu cụ thể).">
        4. Trải nghiệm & Chữa lành
        </h3>
    ''', unsafe_allow_html=True)
    st.write("---")

    st.write("**Khám phá qua Hoạt động:**")
    hoat_dong = st.selectbox("Tùy chỉnh skincare theo hoàn cảnh:", ["Thường xuyên đi xe máy đường bụi", "Hay ngồi điều hòa 8 tiếng/ngày"])
    if hoat_dong == "Thường xuyên đi xe máy đường bụi":
        st.caption("👉 *Gợi ý:* Một combo sữa tắm làm sạch sâu và gel tẩy trang bụi mịn là chân ái của bạn.")
    
    st.write("---")
    st.write("**Nghiên cứu Cảm xúc (Mood Tracker):**")
    mood = st.select_slider("Tâm trạng hôm nay của bạn?", options=["Rất áp lực", "Mệt mỏi", "Bình thường", "Tràn đầy năng lượng"])
    if mood in ["Rất áp lực", "Mệt mỏi"]:
        st.success(f"🔮 Góc chữa lành: {st.session_state.nickname} hãy thắp một ngọn nến thơm, pha trà thảo mộc. Hệ thống đã mở khóa thêm một góc nhỏ để bạn xem bản đồ sao (Astrology) và đường chỉ tay để tìm lại sự bình yên hôm nay nhé. 🌙")
    else:
        st.success(f"Thật tuyệt vời, {st.session_state.nickname}! Hãy duy trì năng lượng tích cực này nhé. ✨")

    st.write("---")
    st.write("**Giáo dục khách hàng (Nhận biết chung & Chọn lọc):**")
    st.info("💧 **Chiến dịch Double Cleansing:** Chỉ dùng sữa rửa mặt là chưa đủ! Website hiện đang có ưu đãi cho dòng nước tẩy trang độc quyền, không cồn, an toàn tuyệt đối. Thử ngay!")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Quay lại", on_click=prev_page)
    with col2:
        st.button("🔄 Bắt đầu lại hành trình", on_click=lambda: st.session_state.update(page=0, nickname=""))

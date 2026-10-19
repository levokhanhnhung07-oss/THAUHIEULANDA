
import os
import json
import streamlit as st

# ===== GIAO DIỆN L'AURA =====
st.set_page_config(
    page_title="L'Aura - Consumer Insight Dashboard",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>
/* Nền chính */
.stApp {
    background-color: #FFF8FA;
    color: #40333A;
}

/* Thanh menu bên trái */
[data-testid="stSidebar"] {
    background-color: #F6E8EF;
}

/* Tiêu đề */
h1, h2, h3 {
    color: #8F456A !important;
}

/* Nút bấm */
.stButton > button {
    background-color: #C879A0;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 18px;
    font-weight: 600;
}

/* Khi rê chuột vào nút */
.stButton > button:hover {
    background-color: #A95881;
    color: white;
    border: none;
}

/* Ô nhập liệu */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background-color: #FFFFFF;
    color: #40333A;
    border: 1px solid #E4B8CD;
    border-radius: 8px;
}

/* Khung thông tin */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #F0D7E2;
    padding: 16px;
    border-radius: 12px;
}

/* Đường phân cách */
hr {
    border-color: #EBD4DF;
}

/* Thông báo */
[data-testid="stAlert"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

import pandas as pd
from datetime import datetime
from openai import OpenAI

st.set_page_config(
    page_title="L'AURA DIGITAL",
    page_icon="🪞",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #FDFCF7;
    color: #202020;
}
h1, h2, h3 {
    font-family: Georgia, serif;
    color: #25251F;
}
[data-testid="stSidebar"] {
    background-color: #F0EEE6;
}
.insight-card {
    background: white;
    border: 1px solid #E5E0D5;
    border-radius: 12px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# KHỞI TẠO DỮ LIỆU
# -----------------------------
if "profile" not in st.session_state:
    st.session_state.profile = {}

if "report" not in st.session_state:
    st.session_state.report = None

if "events" not in st.session_state:
    st.session_state.events = []

def log_event(event):
    st.session_state.events.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "event": event
    })

def analyze_customer(data):
    gap = data["desired"] - data["actual"]

    active = data["problem_status"] == "Đã nhận ra vấn đề"

    if active:
        strategy = "Hỗ trợ tìm kiếm và so sánh giải pháp"
        content = (
            "Cung cấp bộ lọc sản phẩm, thông tin thành phần, "
            "giá cả và hướng dẫn lựa chọn."
        )
    else:
        strategy = "Giáo dục và hỗ trợ nhận biết vấn đề"
        content = (
            "Cung cấp nội dung giải thích dễ hiểu, "
            "thông tin cân bằng và checklist tự đánh giá."
        )

    recommendations = {
        "Da dầu": [
            "Làm sạch dịu nhẹ",
            "Dưỡng ẩm phù hợp",
            "Tìm hiểu sản phẩm chống nắng"
        ],
        "Da khô": [
            "Làm sạch không gây khô căng",
            "Tìm hiểu sản phẩm dưỡng ẩm",
            "Theo dõi phản ứng của da"
        ],
        "Da có mụn": [
            "Chăm sóc da nhẹ nhàng",
            "Tìm hiểu thành phần sản phẩm",
            "Cân nhắc tư vấn bác sĩ da liễu nếu mụn nặng hoặc kéo dài"
        ],
        "Chưa xác định": [
            "Xác định nhu cầu ưu tiên",
            "So sánh thông tin sản phẩm",
            "Lựa chọn theo ngân sách"
        ]
    }

    return {
        "gap": gap,
        "strategy": strategy,
        "content": content,
        "recommendations": recommendations[data["skin_type"]],
        "persona": (
            f"Người dùng quan tâm {data['skin_type']}, "
            f"ngân sách {data['budget']}, "
            f"đang ở giai đoạn {data['stage']}."
        )
    }

def personalize_with_ai(data, report):
    api_key = st.secrets.get(
        "OPENAI_API_KEY",
        os.getenv("OPENAI_API_KEY", "")
    )

    if not api_key:
        return None

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        messages=[
            {
                "role": "system",
                "content": """
                Bạn là chuyên gia Consumer Insight và Marketing.
                Trả lời bằng tiếng Việt.
                Phân tích hành vi khách hàng dựa trên dữ liệu được cung cấp.
                Không chẩn đoán bệnh, không bịa số liệu,
                không phóng đại rủi ro để thúc đẩy mua hàng.
                Hãy đề xuất insight, ý tưởng nội dung và CTA phù hợp.
                """
            },
            {
                "role": "user",
                "content": json.dumps({
                    "customer_data": data,
                    "rule_based_analysis": report
                }, ensure_ascii=False)
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content

# -----------------------------
# MENU
# -----------------------------
st.sidebar.title("L'AURA DIGITAL")

page = st.sidebar.radio(
    "Điều hướng",
    [
        "Trang chủ",
        "1. Nhận biết vấn đề",
        "2. Phân loại vấn đề",
        "3. Yếu tố bối cảnh",
        "4. Hồ sơ khách hàng",
        "5. Đo lường Marketing"
    ]
)

# -----------------------------
# TRANG CHỦ
# -----------------------------
if page == "Trang chủ":
    st.markdown("### CONSUMER INSIGHT · PERSONALIZED MARKETING")
    st.title("L'AURA DIGITAL")
    st.subheader("Hiểu nhu cầu trước khi đề xuất giải pháp.")

    st.write("""
    Website mô phỏng cách thương hiệu mỹ phẩm ứng dụng
    kiến thức Hành vi khách hàng để nhận diện vấn đề,
    cá nhân hóa thông tin và hỗ trợ quyết định mua sắm.
    """)

    st.info(
        "Trải nghiệm 5 bước: nhận biết vấn đề → phân loại vấn đề "
        "→ phân tích bối cảnh → đề xuất giải pháp → đo lường."
    )

    if st.button("Bắt đầu khám phá", type="primary"):
        log_event("journey_started")
        st.success("Hãy chọn mục 1 ở thanh điều hướng bên trái.")

# -----------------------------
# 1. NHẬN BIẾT VẤN ĐỀ
# -----------------------------
elif page == "1. Nhận biết vấn đề":
    st.title("1. Nhận biết vấn đề")
    st.write(
        "So sánh trạng thái thực tế với trạng thái mong muốn."
    )

    with st.form("customer_form"):
        skin_type = st.selectbox(
            "Mối quan tâm chính",
            ["Da dầu", "Da khô", "Da có mụn", "Chưa xác định"]
        )

        actual = st.slider(
            "Mức độ hài lòng hiện tại", 1, 10, 5
        )

        desired = st.slider(
            "Mức độ mong muốn", 1, 10, 9
        )

        problem_status = st.radio(
            "Bạn đã nhận ra vấn đề chưa?",
            [
                "Đã nhận ra vấn đề",
                "Chưa nhận thức rõ vấn đề"
            ]
        )

        budget = st.selectbox(
            "Ngân sách dự kiến",
            [
                "Dưới 200.000đ",
                "200.000–500.000đ",
                "500.000–1.000.000đ",
                "Trên 1.000.000đ",
                "Chưa xác định"
            ]
        )

        stage = st.selectbox(
            "Giai đoạn mua hàng",
            [
                "Đang tìm hiểu",
                "Đang so sánh",
                "Sẵn sàng cân nhắc mua",
                "Chỉ tham khảo"
            ]
        )

        submitted = st.form_submit_button(
            "Phân tích hồ sơ",
            type="primary"
        )

    if submitted:
        st.session_state.profile = {
            "skin_type": skin_type,
            "actual": actual,
            "desired": desired,
            "problem_status": problem_status,
            "budget": budget,
            "stage": stage
        }

        st.session_state.report = None
        gap = desired - actual

        st.metric("Khoảng cách minh họa", f"{gap:+d} điểm")

        st.info(
            "Khoảng cách này chỉ giúp minh họa sự khác biệt "
            "giữa trạng thái thực tế và mong muốn. "
            "Nó không chứng minh khách hàng chắc chắn sẽ mua."
        )

        log_event("problem_recognition_completed")

# -----------------------------
# 2. PHÂN LOẠI VẤN ĐỀ
# -----------------------------
elif page == "2. Phân loại vấn đề":
    st.title("2. Phân loại vấn đề")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Vấn đề đã kích hoạt")
        st.write("""
        Khách hàng nhận ra vấn đề và chủ động tìm giải pháp.
        """)
        st.markdown("""
        **Marketing ứng dụng**
        - Bộ lọc tìm kiếm
        - So sánh sản phẩm
        - Thông tin thành phần
        - Hướng dẫn lựa chọn
        """)

    with col2:
        st.markdown("#### Vấn đề chưa kích hoạt")
        st.write("""
        Khách hàng chưa nhận thức rõ vấn đề hoặc chưa ưu tiên giải quyết.
        """)
        st.markdown("""
        **Marketing ứng dụng**
        - Nội dung giáo dục
        - Checklist tự đánh giá
        - Giải thích kiến thức
        - Thông tin có nguồn xác thực
        """)

    if st.session_state.profile:
        st.info(
            "Phân loại theo câu trả lời: "
            + st.session_state.profile["problem_status"]
        )
    else:
        st.warning("Hãy hoàn thành mục 1 trước.")

    log_event("problem_types_viewed")

# -----------------------------
# 3. YẾU TỐ BỐI CẢNH
# -----------------------------
elif page == "3. Yếu tố bối cảnh":
    st.title("3. Yếu tố bối cảnh")

    context = st.multiselect(
        "Những yếu tố ảnh hưởng đến thói quen của bạn",
        [
            "Thường xuyên đi ngoài trời",
            "Làm việc trong phòng máy lạnh",
            "Lịch học/làm việc bận rộn",
            "Ngân sách cần kiểm soát",
            "Môi trường nóng ẩm"
        ]
    )

    preferences = st.multiselect(
        "Ưu tiên khi chọn sản phẩm",
        [
            "Giá hợp lý",
            "Ít bước sử dụng",
            "Thông tin thành phần rõ ràng",
            "Thương hiệu quen thuộc",
            "Bao bì thân thiện môi trường"
        ]
    )

    if st.button("Lưu bối cảnh"):
        st.session_state.profile["context"] = context
        st.session_state.profile["preferences"] = preferences
        st.success("Đã lưu bối cảnh.")
        log_event("context_saved")

    st.info(
        "Bối cảnh giúp điều chỉnh nội dung và tiêu chí lựa chọn, "
        "nhưng không đủ để chẩn đoán tình trạng da."
    )

# -----------------------------
# 4. HỒ SƠ VÀ ĐỀ XUẤT
# -----------------------------
elif page == "4. Hồ sơ khách hàng":
    st.title("4. Hồ sơ khách hàng & đề xuất")

    if not st.session_state.profile:
        st.warning("Hãy hoàn thành mục 1 trước.")
    else:
        data = st.session_state.profile

        if st.button("Tạo báo cáo insight", type="primary"):
            report = analyze_customer(data)
            st.session_state.report = report
            log_event("report_created")

            try:
                ai_result = personalize_with_ai(data, report)
                st.session_state.ai_result = ai_result
            except Exception as e:
                st.session_state.ai_result = None
                st.warning(
                    "AI chưa phản hồi. Vẫn có thể sử dụng "
                    "báo cáo dựa trên quy tắc."
                )

        report = st.session_state.report

        if report:
            st.subheader("Chân dung khách hàng")
            st.write(report["persona"])

            st.subheader("Chiến lược Marketing")
            st.write(report["strategy"])
            st.write(report["content"])

            st.subheader("Gợi ý giải pháp")
            for item in report["recommendations"]:
                st.markdown(f"- {item}")

            ai_result = st.session_state.get("ai_result")
            if ai_result:
                st.subheader("Phân tích cá nhân hóa bằng AI")
                st.write(ai_result)
            else:
                st.caption(
                    "Đang sử dụng phân tích dựa trên quy tắc "
                    "hoặc chưa cấu hình AI API."
                )

            st.download_button(
                "Tải báo cáo JSON",
                data=json.dumps(
                    {"profile": data, "report": report},
                    ensure_ascii=False,
                    indent=2
                ),
                file_name="laura_report.json",
                mime="application/json"
            )

            st.caption(
                "Đây là thông tin Marketing mang tính tham khảo, "
                "không phải chẩn đoán y tế."
            )

# -----------------------------
# 5. ĐO LƯỜNG
# -----------------------------
elif page == "5. Đo lường Marketing":
    st.title("5. Đo lường Marketing")

    st.write("Các chỉ số nên theo dõi khi triển khai thực tế:")

    st.markdown("""
    - Completion rate: tỷ lệ hoàn thành bảng hỏi.
    - Click-through rate: tỷ lệ nhấp CTA.
    - Recommendation engagement: mức độ tương tác với đề xuất.
    - Return rate: tỷ lệ người dùng quay lại.
    - Feedback helpfulness: mức độ hữu ích do người dùng đánh giá.
    """)

    if st.session_state.events:
        df = pd.DataFrame(st.session_state.events)
        st.dataframe(df, use_container_width=True)

        st.download_button(
            "Tải log CSV",
            data=df.to_csv(index=False).encode("utf-8-sig"),
            file_name="laura_events.csv",
            mime="text/csv"
        )
    else:
        st.info("Chưa có sự kiện trong phiên này.")

st.sidebar.markdown("---")
st.sidebar.caption("L'AURA DIGITAL · MVP")
st.sidebar.caption("Consumer Insight & Ethical Marketing")

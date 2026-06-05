import streamlit as st

# 앱 제목 설정
st.title("🍿 영화관 세트메뉴 구성기")
st.markdown("현재 주문 가능한 모든 팝콘과 음료의 조합입니다.")

# 기존 데이터 옵션
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 1. 모든 세트메뉴 조합 출력하기 (기존 for문 구조 100% 활용)
st.subheader("📋 전체 세트메뉴 라인업")

# 결과를 담을 리스트
all_menus = []

# 기존의 이중 for문을 그대로 활용하여 스트림릿 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        menu_name = f"✨ 세트메뉴: {popcorn} 팝콘 + {drink}"
        all_menus.append(menu_name)
        # 화면에 한 줄씩 출력
        st.write(menu_name)

st.divider()

# 2. [추가 기능] 사용자가 직접 선택할 수 있는 주문 selectbox
st.subheader("🛒 내 맘대로 주문하기")
selected_menu = st.selectbox("원하는 세트메뉴를 선택하세요:", all_menus)

if selected_menu:
    st.success(f"慶 **{selected_menu}**이(가) 선택되었습니다! 주문을 진행합니다. 慶")

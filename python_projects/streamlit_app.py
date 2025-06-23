import streamlit as st
from typing import List, Tuple, Dict
from dataclasses import dataclass

# =========================
# 데이터 클래스 및 분석기
# =========================
@dataclass
class StudentQuizScore:
    student_id: str
    quiz_id: str
    score: int

class ScoreAnalyzer:
    def __init__(self, data: List[Tuple[str, str, int]]):
        self.data = [StudentQuizScore(student_id, quiz_id, score) 
                     for student_id, quiz_id, score in data]

    def calculate_student_averages(self) -> Dict[str, float]:
        student_scores: Dict[str, List[int]] = {}
        for record in self.data:
            student_scores.setdefault(record.student_id, []).append(record.score)
        return {
            student_id: sum(scores) / len(scores)
            for student_id, scores in student_scores.items()
        }

    def calculate_quiz_averages(self) -> Dict[str, float]:
        quiz_scores: Dict[str, List[int]] = {}
        for record in self.data:
            quiz_scores.setdefault(record.quiz_id, []).append(record.score)
        return {
            quiz_id: sum(scores) / len(scores)
            for quiz_id, scores in quiz_scores.items()
        }

    def find_low_performing_students(self, threshold: float = 70.0) -> List[str]:
        student_averages = self.calculate_student_averages()
        return [student_id for student_id, avg in student_averages.items() if avg < threshold]

    def find_top_scorers_per_quiz(self) -> Dict[str, List[str]]:
        quiz_scores: Dict[str, Dict[str, int]] = {}
        for record in self.data:
            quiz_scores.setdefault(record.quiz_id, {})[record.student_id] = record.score
        result = {}
        for quiz_id, scores in quiz_scores.items():
            max_score = max(scores.values())
            top_students = [student_id for student_id, score in scores.items() if score == max_score]
            result[quiz_id] = top_students
        return result

# =========================
# 점수 관리 매니저
# =========================
class ScoreManager:
    def __init__(self):
        self.data: List[Tuple[str, str, int]] = []
        self.analyzer = ScoreAnalyzer(self.data)

    def add_score(self, student_id: str, quiz_id: str, score: int) -> None:
        self.data.append((student_id, quiz_id, score))
        self.analyzer = ScoreAnalyzer(self.data)

    def remove_score(self, student_id: str, quiz_id: str) -> bool:
        before = len(self.data)
        self.data = [entry for entry in self.data if not (entry[0] == student_id and entry[1] == quiz_id)]
        self.analyzer = ScoreAnalyzer(self.data)
        return len(self.data) < before

    def update_score(self, student_id: str, quiz_id: str, new_score: int) -> bool:
        updated = False
        for i, (s, q, _) in enumerate(self.data):
            if s == student_id and q == quiz_id:
                self.data[i] = (s, q, new_score)
                updated = True
                break
        self.analyzer = ScoreAnalyzer(self.data)
        return updated

# =========================
# Streamlit 대시보드 시작
# =========================

st.set_page_config(page_title="학생 성적 관리 대시보드", page_icon="📊")
st.title("📊 학생 성적 관리 대시보드")

# 상태 저장
if "manager" not in st.session_state:
    st.session_state.manager = ScoreManager()
    # 초기 샘플 데이터
    for s, q, sc in [
        ("A001", "Q1", 40),
        ("A002", "Q1", 30),
        ("A003", "Q1", 50),
        ("A001", "Q2", 50),
        ("A002", "Q2", 50),
        ("A003", "Q2", 50),
    ]:
        st.session_state.manager.add_score(s, q, sc)

manager = st.session_state.manager

# ===== 점수 등록 =====
st.header("➕ 점수 등록")
col1, col2, col3 = st.columns(3)
with col1:
    student_id = st.text_input("학생 ID")
with col2:
    quiz_id = st.text_input("퀴즈 ID")
with col3:
    score = st.number_input("점수 (0~100)", min_value=0, max_value=100, value=50)

if st.button("등록"):
    if student_id and quiz_id:
        manager.add_score(student_id, quiz_id, score)
        st.success(f"{student_id}의 {quiz_id} 점수 {score}점 등록 완료")
    else:
        st.warning("학생 ID와 퀴즈 ID를 모두 입력해주세요.")

# ===== 점수 수정 =====
st.header("✏️ 점수 수정")
col1, col2, col3 = st.columns(3)
with col1:
    update_student_id = st.text_input("수정할 학생 ID")
with col2:
    update_quiz_id = st.text_input("수정할 퀴즈 ID")
with col3:
    update_score = st.number_input("새 점수", min_value=0, max_value=100, value=70, key="update_score")

if st.button("수정"):
    if manager.update_score(update_student_id, update_quiz_id, update_score):
        st.success(f"{update_student_id}의 {update_quiz_id} 점수를 {update_score}점으로 수정 완료")
    else:
        st.warning("해당 학생과 퀴즈 정보를 찾을 수 없습니다.")

# ===== 점수 삭제 =====
st.header("🗑️ 점수 삭제")
col1, col2 = st.columns(2)
with col1:
    delete_student_id = st.text_input("삭제할 학생 ID")
with col2:
    delete_quiz_id = st.text_input("삭제할 퀴즈 ID")

if st.button("삭제"):
    if manager.remove_score(delete_student_id, delete_quiz_id):
        st.success(f"{delete_student_id}의 {delete_quiz_id} 점수 삭제 완료")
    else:
        st.warning("해당 학생과 퀴즈 정보를 찾을 수 없습니다.")

# ===== 전체 데이터 테이블 =====
st.header("📋 전체 점수 테이블")
st.dataframe(manager.data, use_container_width=True)

# ===== 분석 결과 =====
st.header("📈 분석 결과")

if st.button("1️⃣ 학생별 평균 점수"):
    st.write(manager.analyzer.calculate_student_averages())

if st.button("2️⃣ 퀴즈별 평균 점수"):
    st.write(manager.analyzer.calculate_quiz_averages())

if st.button("3️⃣ 평균 70점 미만 학생"):
    st.write(manager.analyzer.find_low_performing_students())

if st.button("4️⃣ 퀴즈별 최고 점수자"):
    st.write(manager.analyzer.find_top_scorers_per_quiz())

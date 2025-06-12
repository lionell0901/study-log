# 학생 성적 관리 및 분석 시스템
# 기능:
# 1. 학생별 평균 점수 계산
# 2. 퀴즈별 평균 점수 계산
# 3. 평균 점수가 70점 미만인 학생 ID 추출
# 4. 각 퀴즈별 최고 점수를 받은 학생 ID 추출

from typing import List, Tuple, Dict  # 타입 힌팅을 위한 임포트
from dataclasses import dataclass     # 데이터 클래스 데코레이터 임포트

# 샘플 데이터: (학생ID, 퀴즈ID, 점수) 형식의 튜플 리스트
data = [
    ("A001", "Q1", 40),
    ("A002", "Q1", 30),
    ("A003", "Q1", 50),
    ("A001", "Q2", 50),
    ("A002", "Q2", 50),
    ("A003", "Q2", 50),
]

@dataclass
class Student:
    """학생 정보를 저장하는 데이터 클래스"""
    id: str       # 학생 ID
    quiz: str     # 퀴즈 ID
    score: int    # 점수

@dataclass
class Quiz:
    """퀴즈 정보를 저장하는 데이터 클래스"""
    id: str       # 퀴즈 ID
    score: int    # 점수

@dataclass
class StudentQuizScore:
    """학생의 퀴즈 점수 정보를 저장하는 데이터 클래스"""
    student_id: str   # 학생 ID
    quiz_id: str      # 퀴즈 ID
    score: int        # 점수

class ScoreAnalyzer:
    """점수 분석을 위한 클래스"""
    
    def __init__(self, data: List[Tuple[str, str, int]]):
        """
        데이터를 받아 StudentQuizScore 객체 리스트로 변환
        Args:
            data: (학생ID, 퀴즈ID, 점수) 형식의 튜플 리스트
        """
        self.data = [StudentQuizScore(student_id, quiz_id, score) 
                    for student_id, quiz_id, score in data]

    def calculate_student_averages(self) -> Dict[str, float]:
        """
        학생별 평균 점수 계산
        Returns:
            Dict[str, float]: 학생ID를 키로 하고 평균 점수를 값으로 하는 딕셔너리
        """
        student_scores: Dict[str, List[int]] = {}
        
        for record in self.data:
            if record.student_id not in student_scores:
                student_scores[record.student_id] = []
            student_scores[record.student_id].append(record.score)
        
        return {
            student_id: sum(scores) / len(scores)
            for student_id, scores in student_scores.items()
        }

    def calculate_quiz_averages(self) -> Dict[str, float]:
        """
        퀴즈별 평균 점수 계산
        Returns:
            Dict[str, float]: 퀴즈ID를 키로 하고 평균 점수를 값으로 하는 딕셔너리
        """
        quiz_scores: Dict[str, List[int]] = {}
        
        for record in self.data:
            if record.quiz_id not in quiz_scores:
                quiz_scores[record.quiz_id] = []
            quiz_scores[record.quiz_id].append(record.score)
        
        return {
            quiz_id: sum(scores) / len(scores)
            for quiz_id, scores in quiz_scores.items()
        }

    def find_low_performing_students(self, threshold: float = 70.0) -> List[str]:
        """
        평균 점수가 기준점 미만인 학생 찾기
        Args:
            threshold: 기준 점수 (기본값: 70.0)
        Returns:
            List[str]: 기준 미달 학생들의 ID 리스트
        """
        student_averages = self.calculate_student_averages()
        return [
            student_id
            for student_id, average in student_averages.items()
            if average < threshold
        ]

    def find_top_scorers_per_quiz(self) -> Dict[str, List[str]]:
        """
        각 퀴즈별 최고 점수를 받은 학생들 찾기
        Returns:
            Dict[str, List[str]]: 퀴즈ID를 키로 하고 최고 점수 학생들의 ID 리스트를 값으로 하는 딕셔너리
        """
        quiz_top_scores: Dict[str, Dict[str, int]] = {}
        
        # 퀴즈별로 학생들의 점수를 수집
        for record in self.data:
            if record.quiz_id not in quiz_top_scores:
                quiz_top_scores[record.quiz_id] = {}
            quiz_top_scores[record.quiz_id][record.student_id] = record.score
        
        # 각 퀴즈에서 최고 점수를 받은 학생들을 찾음
        result = {}
        for quiz_id, scores in quiz_top_scores.items():
            max_score = max(scores.values())
            top_students = [
                student_id
                for student_id, score in scores.items()
                if score == max_score
            ]
            result[quiz_id] = top_students
            
        return result

class ScoreManager:
    """점수 관리를 위한 클래스"""
    
    def __init__(self):
        """초기화: 빈 데이터 리스트와 분석기 생성"""
        self.data = []
        self.analyzer = ScoreAnalyzer(self.data)

    def add_score(self, student_id: str, quiz_id: str, score: int) -> None:
        """
        새로운 점수 추가
        Args:
            student_id: 학생 ID
            quiz_id: 퀴즈 ID
            score: 점수 (0-100)
        """
        if not (0 <= score <= 100):
            print("점수는 0에서 100 사이여야 합니다.")
            return
        self.data.append((student_id, quiz_id, score))
        self.analyzer = ScoreAnalyzer(self.data)
        print(f"학생 {student_id}의 퀴즈 {quiz_id} 점수 {score}점이 추가되었습니다.")

    def remove_score(self, student_id: str, quiz_id: str) -> None:
        """
        점수 삭제
        Args:
            student_id: 학생 ID
            quiz_id: 퀴즈 ID
        """
        before_length = len(self.data)
        self.data = [(s, q, sc) for s, q, sc in self.data if not (s == student_id and q == quiz_id)]
        if len(self.data) == before_length:
            print(f"학생 {student_id}의 퀴즈 {quiz_id} 기록을 찾을 수 없습니다.")
        else:
            self.analyzer = ScoreAnalyzer(self.data)
            print(f"학생 {student_id}의 퀴즈 {quiz_id} 기록이 삭제되었습니다.")

    def update_score(self, student_id: str, quiz_id: str, new_score: int) -> None:
        """
        점수 수정
        Args:
            student_id: 학생 ID
            quiz_id: 퀴즈 ID
            new_score: 새로운 점수 (0-100)
        """
        if not (0 <= new_score <= 100):
            print("점수는 0에서 100 사이여야 합니다.")
            return
        
        found = False
        for i, (s, q, _) in enumerate(self.data):
            if s == student_id and q == quiz_id:
                self.data[i] = (student_id, quiz_id, new_score)
                found = True
                break
        
        if found:
            self.analyzer = ScoreAnalyzer(self.data)
            print(f"학생 {student_id}의 퀴즈 {quiz_id} 점수가 {new_score}점으로 수정되었습니다.")
        else:
            print(f"학생 {student_id}의 퀴즈 {quiz_id} 기록을 찾을 수 없습니다.")

    def show_all_scores(self) -> None:
        """현재 등록된 모든 점수를 테이블 형식으로 출력"""
        if not self.data:
            print("등록된 점수가 없습니다.")
            return
        
        print("\n현재 등록된 모든 점수:")
        print("학생ID\t퀴즈ID\t점수")
        print("-" * 30)
        for student_id, quiz_id, score in sorted(self.data):
            print(f"{student_id}\t{quiz_id}\t{score}")

def print_menu() -> None:
    """메인 메뉴 출력"""
    print("\n=== 학생 성적 관리 시스템 ===")
    print("1. 점수 등록")
    print("2. 점수 삭제")
    print("3. 점수 수정")
    print("4. 전체 점수 조회")
    print("5. 분석 결과 보기")
    print("6. 종료")
    print("========================")

def get_student_quiz_info(prompt: str = "") -> Tuple[str, str]:
    """
    학생ID와 퀴즈ID 입력 받기
    Args:
        prompt: 출력할 프롬프트 메시지
    Returns:
        Tuple[str, str]: (학생ID, 퀴즈ID) 튜플
    """
    if prompt:
        print(prompt)
    student_id = input("학생 ID를 입력하세요 (예: A001): ").strip()
    quiz_id = input("퀴즈 ID를 입력하세요 (예: Q1): ").strip()
    return student_id, quiz_id

def print_results(analyzer: ScoreAnalyzer) -> None:
    """
    모든 분석 결과 출력
    Args:
        analyzer: ScoreAnalyzer 인스턴스
    """
    # 1. 학생별 평균 점수
    student_averages = analyzer.calculate_student_averages()
    print("\n1. 학생별 평균 점수:")
    for student_id, average in student_averages.items():
        print(f"학생 {student_id}: {average:.2f}점")
    
    # 2. 퀴즈별 평균 점수
    quiz_averages = analyzer.calculate_quiz_averages()
    print("\n2. 퀴즈별 평균 점수:")
    for quiz_id, average in quiz_averages.items():
        print(f"퀴즈 {quiz_id}: {average:.2f}점")
    
    # 3. 평균 70점 미만 학생
    low_performing = analyzer.find_low_performing_students()
    print("\n3. 평균 70점 미만 학생:")
    if low_performing:
        for student_id in low_performing:
            print(f"학생 {student_id}: {student_averages[student_id]:.2f}점")
    else:
        print("해당하는 학생이 없습니다.")
    
    # 4. 퀴즈별 최고 점수자
    top_scorers = analyzer.find_top_scorers_per_quiz()
    print("\n4. 퀴즈별 최고 점수자:")
    for quiz_id, students in top_scorers.items():
        print(f"퀴즈 {quiz_id}: {', '.join(students)}")

def main():
    """메인 프로그램 실행"""
    manager = ScoreManager()
    
    # 초기 데이터 로드 (선택사항)
    for student_id, quiz_id, score in data:
        manager.add_score(student_id, quiz_id, score)
    
    while True:
        print_menu()
        choice = input("원하는 작업의 번호를 입력하세요: ").strip()
        
        try:
            if choice == "1":  # 점수 등록
                student_id, quiz_id = get_student_quiz_info("=== 점수 등록 ===")
                score = int(input("점수를 입력하세요 (0-100): "))
                manager.add_score(student_id, quiz_id, score)
                
            elif choice == "2":  # 점수 삭제
                student_id, quiz_id = get_student_quiz_info("=== 점수 삭제 ===")
                manager.remove_score(student_id, quiz_id)
                
            elif choice == "3":  # 점수 수정
                student_id, quiz_id = get_student_quiz_info("=== 점수 수정 ===")
                new_score = int(input("새로운 점수를 입력하세요 (0-100): "))
                manager.update_score(student_id, quiz_id, new_score)
                
            elif choice == "4":  # 전체 점수 조회
                manager.show_all_scores()
                
            elif choice == "5":  # 분석 결과
                print_results(manager.analyzer)
                
            elif choice == "6":  # 종료
                print("프로그램을 종료합니다.")
                break
                
            else:
                print("잘못된 선택입니다. 1-6 사이의 숫자를 입력해주세요.")
                
        except ValueError as e:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            print("다시 시도해주세요.")
        
        input("\n계속하려면 Enter를 누르세요...")

if __name__ == "__main__":
    main()
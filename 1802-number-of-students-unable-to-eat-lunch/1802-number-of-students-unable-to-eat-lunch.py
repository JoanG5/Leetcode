class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        round = square = 0

        for student in students:
            if student == 0:
                square += 1
            else:
                round += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if square == 0:
                    break
                else:
                    square -= 1
            elif sandwich == 1:
                if round == 0:
                    break
                else:
                    round -= 1
        
        return round + square
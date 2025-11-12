m_question = "What is 27 * 34? "
c_question = "What color do you get when you mix red and blue? "
a_question = "What animal hibernates in winter and loves salmon? "

m_response = input(m_question)

c_response = input(c_question)

a_response = input(a_question)

m_answer = "918"
c_answer = "PURPLE"
a_answer = "BEAR"

score = 0

if m_response == m_answer:
    score += 1
if c_response.upper() == c_answer:
    score += 1
if a_response.upper() == a_answer:
    score += 1

print(f"{score} / 3")

if score == 0:
    print("No answers correct!")
elif score == 1:
    print("Keep practicing!")
elif score == 2:
    print("Good try!")
else:
    print("Perfect!")


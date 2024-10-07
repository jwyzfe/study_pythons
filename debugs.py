
list_question = [
        "상품의 품질에 대해 어떻게 생각하시나요?",
        "상품의 가격에 대해 어떻게 생각하시나요?",
        "상품의 디자인에 대해 어떻게 생각하시나요?",
        "상품에 대한 전반적인 만족도는 어떠신가요?"
    ]
    
list_answer = ["1. 좋음", "2. 중간", "3. 좋아지길"]

def survey():
    
    results = []

    for question in list_question:
        print(question)
        for answer in list_answer:
            print(answer)
        result = input("입력 ")
        results.append(result)
        print('----------')

    return result

survey_result = survey()
print(survey_result)




pass



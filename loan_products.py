loan_products = [
    {"company": "신한은행", "product_name": "신한주택대출(아파트)", "base_rate": 3.42, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "우리은행", "product_name": "우리 WON 갈아타기 직장인대출", "base_rate": 3.97, "additional_rate": 2.60, "preferred_rate": 1.40},
    {"company": "BNK", "product_name": "BNK모바일주택담보대출", "base_rate": 3.14, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "신한은행", "product_name": "신한 MY CAR 신차 대출", "base_rate": 3.41, "additional_rate": 2.60, "preferred_rate": 0.60},
    {"company": "국민은행", "product_name": "KB 스타 아파트 담보대출 혼합금리(주택자금)", "base_rate": 3.15, "additional_rate": 2.24, "preferred_rate": 1.40},
    {"company": "주식회사 카카오뱅크", "product_name": "일반신용대출", "base_rate": 3.32, "additional_rate": 1.53, "preferred_rate": 0.60},
    {"company": "신한은행", "product_name": "신한은행 쏠편한 직장인대출S I", "base_rate": 4.87, "additional_rate": 1.30, "preferred_rate": 1.40},
]

money = 1000000  # 대출 금액
months = 24      # 상환 기간

def total_payment(product_info, amount):
    monthly_pay = amount / months
    total_payment = 0
    
    # 이자율 계산
    interest_rate = product_info["base_rate"] + product_info["additional_rate"] - product_info["preferred_rate"]
    monthly_rate = interest_rate / 100 / 12  # 월 이자율 계산

    for month in range(1, months + 1):  
        remain = amount - (monthly_pay * (month - 1))  # 잔여 원금
        monthly_interest = remain * monthly_rate  # 월 이자 계산
        monthly_payment = monthly_pay + monthly_interest  # 월 상환액
        total_payment += monthly_payment  # 총액에 추가
        
    return total_payment

total_payments = []

for product in loan_products:
    total = total_payment(product, money)  
    total_payments.append((product, total))  
    print(f"{product['company']} - {product['product_name']}: 총액 = {total:.2f} 원")  # 총액 출력

# 총액이 가장 적은 상품 찾기
lowest_product = min(total_payments, key=lambda x: x[1])

best_product, best_total = lowest_product
print(f"가장 유리한 상품: {best_product['company']} - {best_product['product_name']}: {best_total:.2f} 원")

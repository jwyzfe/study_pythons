loan_products = [
    {"company": "신한은행", "product": "신한주택대출(아파트)", "base_rate": 3.42, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "우리은행", "product": "우리 WON 갈아타기 직장인대출", "base_rate": 3.97, "additional_rate": 2.60, "preferred_rate": 1.40},
    {"company": "BNK", "product": "BNK모바일주택담보대출", "base_rate": 3.14, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "신한은행", "product": "신한 MY CAR 신차 대출", "base_rate": 3.41, "additional_rate": 2.60, "preferred_rate": 0.60},
    {"company": "국민은행", "product": "KB 스타 아파트 담보대출 혼합금리(주택자금)", "base_rate": 3.15, "additional_rate": 2.24, "preferred_rate": 1.40},
    {"company": "주식회사 카카오뱅크", "product": "일반신용대출", "base_rate": 3.32, "additional_rate": 1.53, "preferred_rate": 0.60},
    {"company": "신한은행", "product": "신한은행 쏠편한 직장인대출S I", "base_rate": 4.87, "additional_rate": 1.30, "preferred_rate": 1.40},
]

money = 1000000
months = 24

def total_payment(product, money):
    monthly_pay = money / months
    total_payment = 0
    
    # Calculate the interest rate
    interest_rate = product["base_rate"] + product["additional_rate"] - product["preferred_rate"]
    monthly_rate = interest_rate / 100 / 12  

    for month in range(1, months + 1):  
        remain = money - (monthly_pay * (month - 1)) 
        monthly_interest = remain * monthly_rate
        monthly_payment = monthly_pay + monthly_interest
        total_payment += monthly_payment
        
    return total_payment


total_payments = []

for product in loan_products:
    total = total_payment(product, money)  
    total_payments.append((product, total))  
    print(f"{product['company']} - {product['product']}: 총액 = {total:.2f} 원")


lowest_product = min(total_payments, key=lambda x: x[1])


best_product, best_total = lowest_product
print(f"가장 유리한 상품: {best_product['company']} - {best_product['product']}: {best_total:.2f} 원")


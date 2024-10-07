deposit_my_list = 450000 #원금
bank_rate_year = [0.024, 0.036] #연이자율
bank_tax_interest_rate= [0, 0.154] #세금


# def (bank):
# for i in range(1,34,3):
#     return bank
        
# print(return)




for i in range(1,34,3):
    for r in bank_rate_year:
        print(deposit_my_list * bank_rate_year * i )
    
    
    
    # for rate in bank_rate_year:
    #     deposit_my_list * 
    #     for  tax in bank_tax_interest_rate:
        
    
        
  
  
  
  
  
  
  
  
  
 

months = 32  # 예금 기간 (32개월)
compound_period = 3  # 복리 계산 주기 (3개월마다)

# range(1, 34, 3)을 사용하여 계산 및 출력
for annual_rate in interest_rates:
    for tax in tax_rates:
        total_amount = principal
        # 1개월부터 32개월까지 3씩 증가하며 복리 계산
        for month in range(1, months + 1, compound_period):  
            monthly_rate = annual_rate / 12
            total_amount *= (1 + monthly_rate * compound_period)  # 3개월마다 복리 계산
        after_tax_amount = total_amount * (1 - tax)  # 세금 적용 후 금액 계산
        print(f"이자율 {annual_rate*100}%, 세금율 {tax*100}%: {after_tax_amount:.2f} 원")
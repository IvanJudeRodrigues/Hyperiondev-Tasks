import math
print ("investment - to calculate the amount of interest you will earn on your investment")
print ("bond - to calculate the amount you will have to pay a month on the home loan")
# does user want to invest or borrow a home loan bond
investment_choice = input("investment or bond").lower()
# if the user wants to invest
if investment_choice == "investment":
      # ask the user how much they want to invest
      P=int(input("How much do you want to invest to the nearest 1,000"))
      # ask user how much they want
      r=float(input("What interest rate do you want from 5%.We offer 8% annually"))
      # ask how long do they want to invest
      t=int(input("How many years do you want to invest."))
      # do they want simple or compound interet
      interest_type=input("Do you want simple or Compound.").lower()
      # tell user how much simple interest they will earn if they choose simple
      if interest_type=="simple":
        # use the formula to calculate simple interest
        simple_interest=P*((1+r/100*t))
        # print the simple interest they will earn
        print(f"The amount you will earn will be float{simple_interest}")
       # if user chooses Compound interest
      elif interest_type=="compound":
         # use the formula to calcularte compound interest
         Compound_interest=P*math.pow((1+r/100),t)
         # print the compound interest
         print(Compound_interest)
         # if user chooses mortgage bond
else:
    monthly_repayment=0
    # ask user the value of the house they want to purchase
    P=int(input("What is the value of the house you want to purchase"))
    # how much interest do you want
    int_rate=int(input("What interest rate"))
    i=float(int_rate/100/12)
    # in how many months do they want to repay the mortgage
    n=int(input("How many months would you like to repay this loan."))
    # use the formula to calculate how much they will have to pay a month
 
    monthly_repayment==float(P[i(1+i)**n]/[(1+i)**(n-1)])
    # print this monthly repayment
    print(f"The amount you will have to pay a month is{monthly_repayment}")
menu = """

========== OPÇÕES ==========

[1] - Depósito
[2] - Sacar
[3] - Extrato
[0] - Sair

============================
"""
saldo = 2000
limite = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == '1':
       valor = float(input("Informe o valor do depósito: "))
       
       if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"
          
       else:
         print("Falha na operação! O valor informado não é válido. Tente novamente!")
                   
      
    
    elif opcao == '2':
       valor = float(input("Informe o valor do saque: "))
       
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saques = saques_realizados >= LIMITE_SAQUES
       
       if excedeu_saldo:
          print("Você não tem saldo suficiente para realizar essa operação!")
          
       elif excedeu_limite:
          print("O valor informado excedeu o limite!")
       
       elif excedeu_saques:
         print("Número máximo de saques excedido!")
         
       elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           saques_realizados += 1
           
       else:
           print("Você não tem saldo suficiente para realizar essa operação!")             
    
    elif opcao == '3':
       print("\n ========== EXTRATO ==========")
       print("Não foram realizados movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("================================")       
    elif opcao == '0':
       break        
else:
       print("Operação inválida. Por favor selecione novamente uma opção")
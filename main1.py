print("Welcome to VAT calculator machine.")
amount_Of_Vat = 0
VAT = 0
total_price = 0

price = float(input("Please enter a number that you want to remove or add VAT to. (In Decimals) : "))
amount_Of_Vat = float(input("How much VAT do you want to add/remove?(in Decimals) : "))
add_or_remove_VAT = input('Do you want to add VAT to your price or remove VAT from your price (type "add" or "remove") : ')

if add_or_remove_VAT == "add":

    VAT = price * amount_Of_Vat
    round_VAT = round(VAT, 2)
    total_price = round_VAT + price
    print("VAT is €", round_VAT)
    print("Total cost is €", total_price, ".")

if add_or_remove_VAT == "remove":
    
    remove_total_price = price / (1 + amount_Of_Vat)
    rounded_total_price = round(remove_total_price, 2)
    VAT = price - remove_total_price
    round_VAT = round(VAT, 2)
    print('VAT removed €', round_VAT)
    print('The price before VAT was €', rounded_total_price, '.')
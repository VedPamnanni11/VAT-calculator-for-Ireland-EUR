print("Welcome to VAT calculator machine for Ireland (EUR)")
product_VAT = 0.23
service_VAT = 0.13
VAT = 0
total_price = 0

price = float(input("Please enter a price for a service or a product (In Decimals) : "))
VAT_type = input("Is that price for service or product : ")
add_or_remove_VAT = input('Do you want to add VAT to your price or remove VAT from your price (type "add" or "remove") : ')

if add_or_remove_VAT == "add":
    if VAT_type == "service" or "product":
        if VAT_type == "service":
            VAT = price * service_VAT
            round_VAT = round(VAT, 2)
            total_price = round_VAT + price
            print("VAT is €", round_VAT)
            print("Total cost is €", total_price, "for your service.")

        elif VAT_type == "product":
            VAT = price * product_VAT
            round_VAT = round(VAT, 2)
            total_price = round_VAT + price
            print("VAT is €", round_VAT)
            print("Total cost is €", total_price, "for your product.")

if add_or_remove_VAT == "remove":
    if VAT_type == "service":
        remove_total_price = price / (1 + service_VAT)
        rounded_total_price = round(remove_total_price, 2)
        VAT = price - remove_total_price
        round_VAT = round(VAT, 2)
        print('VAT removed €', round_VAT)
        print('The price before VAT was €', rounded_total_price, 'for your service.')
    elif VAT_type == "product":
        remove_total_price = price / (1 + product_VAT)
        rounded_total_price = round(remove_total_price, 2)
        VAT = price - remove_total_price
        round_VAT = round(VAT, 2)
        print('VAT removed €', round_VAT)
        print('The price before VAT was €', rounded_total_price, 'for your product.')
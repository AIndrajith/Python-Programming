#Challenge 2_4

#tax_precentage = Base_price*0.25
#lisence_percentage = Base_price*0.15
#destination_charge per mile 20$

base_price = float(input("Enter the Base prise of car in dollars: "))
destination= float(input("Enter the distance in miles: "))

tax_amount = base_price * 0.25
lisence_amo= base_price * 0.15

deeler_prep= 250
destination_charge = destination * 20

total = base_price + tax_amount + lisence_amo + deeler_prep + destination_charge

print("\nActual Prise of the car: ",total)

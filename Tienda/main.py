from clasesocupadas import *

prod1 = Producto("Maruchan",16,100)
rod1 = Producto("Maruchan", 16, 100)
prod2 = Producto("Coca Cola", 25, 150)
prod3 = Producto("Pan Blanco", 35, 80)
prod4 = Producto("Leche", 22, 120)
prod5 = Producto("Huevos", 45, 60)
prod6 = Producto("Arroz", 28, 200)
prod7 = Producto("Frijoles", 30, 90)
prod8 = Producto("Aceite", 40, 75)
prod9 = Producto("Azúcar", 32, 110)
prod10 = Producto("Sal", 12, 140)
prod11 = Producto("Café", 55, 85)
prod12 = Producto("Atún", 18, 95)
prod13 = Producto("Galletas", 20, 130)
prod14 = Producto("Chocolate", 15, 105)
prod15 = Producto("Jugo", 23, 88)
prod16 = Producto("Papel Higiénico", 50, 70)
prod17 = Producto("Jabón", 14, 160)
prod18 = Producto("Pasta Dental", 38, 92)
prod19 = Producto("Shampoo", 65, 65)
prod20 = Producto("Cereal", 48, 78)

cat1=Categoria("Alimentos")
list1=[prod3, prod4, prod5,prod6, prod7, prod8]
for a in list1:
cat1.agregar_producto(prod4)
print(cat1.lista)

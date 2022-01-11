carrinho = [("Produto 1", 20),
            ("Produto 2", 20),
            ("Produto 3", 20),
            ("Produto 4", 20),
            ("Produto 5", 20),
            ("Produto 6", 10),
            ("Produto 7", 10),
            ("Produto 8", 20)]

print(carrinho)
print(sum([preco for _, preco in carrinho if preco < 20]))

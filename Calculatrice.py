class Calculatrice :

    def add(nb1 : float, nb2: float) -> float :
        return nb1 + nb2

    def substract(nb1 : float, nb2:float) -> float :
        return nb1-nb2

    def multiply (nb1,nb2) :
        return nb1 * nb2

    def division(nb1,nb2):
        if nb2 == 0 :
            raise ValueError('Division by 0 impossible !')
        return nb1/nb2
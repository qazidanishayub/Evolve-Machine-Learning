from Matrics import *

def main():

    x = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # for dot multiplication of Two Matrics

    object_dotProduct = Matrix(x, y)
    object_dotProduct.dot_product()


    my_matrix = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    size = int(input("Enter order : "))
    object_Identity = Identity(size)
    print (my_matrix," comparison ", object_Identity.identity())

    # matrix to test if it is identity or not.
    object_Identity.testmatch(my_matrix)

if __name__ == "__main__":
    main()
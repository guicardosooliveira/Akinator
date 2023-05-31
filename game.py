import random
from tree import Tree
from node import Node

# verificar loops dos metodos make_question e make_guess
# continuar do metodo make_guess
from type_enum import TypeEnum


class Game_controler:
    def __init__(self):
        self.__tree = Tree()
        self.build_tree()
        self.start_menu()

    def start_menu(self):
        print("---INÍCIO---")
        print("")
        print("1 -> Começar novo Jogo")
        print("2 -> Continuar jogo anterior")
        option = input("Digite a opção escolhida (1 ou 2):")
        if option == "1":
            self.start_new_game()
        elif option == "2":
            print("Zerando minha memória")
        else:
            print("Opção errada")

    def start_new_game(self):
        print("Pense em um PAÍS!")
        self.go_through_tree(self.__tree.root)

    def build_tree(self):
        self.__tree.insert_question_and_answers("Você está pensando em um país da Europa? (s/n)",
                                                "Espanha", "Argentina")

    def make_question(self, node):
        answer = input(node.value)
        while answer.lower() != "s" and answer.lower() != "n":
            answer = input("Digite uma resposta válida (s/n):")
        return answer

    def make_guess(self, node: Node):
        is_right = input(f'O país que você está pensando é {node.value}? (s/n)')
        while is_right.lower() != "s" and is_right.lower() != "n":
            is_right = input("Digite uma resposta válida (s/n):")

        if is_right == "s":
            right_guessed_answers = ["Acertei! Eu sou demais!",
                                     "Uau, sou bom nisso! Adivinhei corretamente!",
                                     "Bingo! Mais uma vitória para mim!",
                                     "Eba! Mais uma vez acertei em cheio!",
                                     "Eu sabia! Minhas habilidades de adivinhação são incríveis!"]
            print(right_guessed_answers[random.randint(0, len(right_guessed_answers) - 1)])
            self.start_menu()

        elif is_right == "n":
            right_guess = input("Qual país você pensou?")
            new_question = input(f"Me diga uma pergunta de SIM ou NÃO que diferencie a/o {node.value} do(a) \n"
                                 f"{right_guess}, sendo Sim para o {right_guess} e não para {node.value}")
            self.__tree.insert_question_and_answers(new_question, right_guess, node.value, node)
            self.start_new_game()

    def go_through_tree(self, root):
        if root.type == TypeEnum.QUESTION:
            answer = self.make_question(root)
            if answer == "s":
                self.go_through_tree(root.left_node)
            else:
                self.go_through_tree(root.right_node)
        elif root.type == TypeEnum.ANSWER:
            self.make_guess(root)


controller = Game_controler()

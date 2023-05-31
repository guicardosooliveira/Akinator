import pickle
import random
from tree import Tree
from node import Node
from type_enum import TypeEnum


class GameController:
    def __init__(self):
        self.__tree = None
        self.start_menu()

    def start_menu(self):
        print("---INÍCIO---")
        print("")
        print("1 -> Começar novo Jogo")
        print("2 -> Continuar progresso anterior")
        print("3 -> Sair do Jogo")
        option = input("Digite a opção escolhida (1, 2 ou 3):")
        while option.lower() != "1" and option.lower() != "2" and option.lower() != "3":
            option = input("Digite uma resposta válida (1, 2 ou 3): ")

        if option == "1":
            self.start_new_game()
        elif option == "2":
            self.restart_game()
        else:
            print("Até a próxima!")

    def start_new_game(self):
        self.restart_tree()
        self.build_tree()
        print("Pense em um PAÍS!")
        self.go_through_tree(self.__tree.root)

    def restart_game(self):
        self.__tree = self.load_saved_progress()
        print("Continuando o progresso anterior...")
        print("Pense em um PAÍS!")
        self.go_through_tree(self.__tree.root)

    def build_tree(self):
        self.__tree = Tree()
        self.__tree.insert_question_and_answers("Você está pensando em um país da Europa?",
                                                "Espanha", "Argentina")
        self.save_progress(self.__tree)

    def make_question(self, node):
        answer = input(f'{node.value} (s/n)')
        while answer.lower() != "s" and answer.lower() != "n":
            answer = input("Digite uma resposta válida (s/n): ")
        return answer

    def make_guess(self, node: Node):
        is_right = input(f'O país que você está pensando é {node.value}? (s/n) ')
        while is_right.lower() != "s" and is_right.lower() != "n":
            is_right = input("Digite uma resposta válida (s/n): ")

        if is_right == "s":
            right_guessed_answers = ["Acertei! Eu sou demais!",
                                     "Uau, sou bom nisso! Adivinhei corretamente!",
                                     "Bingo! Mais uma vitória para mim!",
                                     "Eba! Mais uma vez acertei em cheio!",
                                     "Eu sabia! Minhas habilidades de adivinhação são incríveis!"]
            print("---------------------------------")
            print(right_guessed_answers[random.randint(0, len(right_guessed_answers) - 1)])
            print("---------------------------------")
            self.start_menu()

        elif is_right == "n":
            right_guess = input("Qual país você pensou?")
            new_question = input(f"Me diga uma pergunta de SIM ou NÃO que diferencie a/o {node.value} do(a) \n"
                                 f"{right_guess}, sendo Sim para o {right_guess} e não para {node.value}: ")
            self.__tree.insert_question_and_answers(new_question, right_guess, node.value, node)
            self.save_progress(self.__tree)
            self.restart_game()

    def go_through_tree(self, root):
        if root.type == TypeEnum.QUESTION:
            answer = self.make_question(root)
            if answer == "s":
                self.go_through_tree(root.left_node)
            else:
                self.go_through_tree(root.right_node)
        elif root.type == TypeEnum.ANSWER:
            self.make_guess(root)

    def save_progress(self, arvore):
        with open("memory.pkl", "wb") as f:
            pickle.dump(arvore, f)

    def load_saved_progress(self):
        with open("memory.pkl", "rb") as f:
            arvore = pickle.load(f)
        return arvore

    def restart_tree(self):
        with open("memory.pkl", "wb") as f:
            f.truncate(0)

controller = GameController()

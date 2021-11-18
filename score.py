import os


if __name__ == '__main__':
    building = input("Input building: ")
    case = input("Input case: ")

    command = f"java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 data/Ex1_input/Ex1_Buildings/B{building}.json out/Ex1_B{building}_case_{case}.csv logs/Ex1_B{building}_case_{case}.log"
    os.system(command)

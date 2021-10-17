'''This file contains the algorythm of choices for the Inspector A.I'''

from Brice_src.Inspector_stateInfo import StateInfo

stateInfo = StateInfo()

class MinMax:

    def __init__(self):
        self.currentChar = ""

    def calculateBestChoiceCharacter(self, state, characters):
        pos = 0
        for player in characters:
            if (player['color'] == "red"):
                self.currentChar = "red"
                return (pos)
            else:
                if (stateInfo.isCharSuspect(player, state)):
                    self.currentChar = player["color"]
                    return pos
            pos += 1
        self.currentChar = characters[0]['color']
        return 0

    def calculateBestPosition(self, state, positions):
        ratios = []
        p_pos = -1
        for player in state['characters']:
                p_pos =+ 1
                if player['color'] == self.currentChar:
                    break
        for new_pos in positions:
            state['characters'][p_pos]['position'] = new_pos
            ratios.append(stateInfo.getSuspectSeparation(state))
        return stateInfo.findBestConfiguration(ratios)
    
    def calculateBestPower(self, state, question):
        if (question == "activate white power"):
            return 1
        return 0
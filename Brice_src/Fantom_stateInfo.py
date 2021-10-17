'''This file contains everything about the state of the game and how its treated by the Fantom A.I'''

class StateInfo:
    
    def getSuspectSeparation(self, state):
        playersSolo = []
        playersGroup = []
        suspectNb = 0
        fantom_color = state['fantom']

        for player in state['characters']:
            if (player['suspect']):
                suspectNb += 1
        position = -1
        fantom_state = 'solo'
        while (len(playersGroup) + len(playersSolo) != suspectNb):
            position += 1
            playersInPos = []
            for player in state['characters']:
                if (player['position'] == position):
                    playersInPos.append(player)
            if (len(playersInPos) > 1):
                for char in playersInPos:
                    if (char['suspect']):
                        if (char['color'] == fantom_color):
                            fantom_state = 'group'
                        playersGroup.append(char)
            elif (len(playersInPos) == 1):
                if (playersInPos[0]['suspect']):
                    if (playersInPos[0]['color'] == fantom_color):
                        fantom_state = 'solo'
                    playersSolo.append(playersInPos)

        suspectsRatio = {
            'solo': len(playersSolo),
            'group': len(playersGroup),
            'fantom': fantom_state
        }
        return (suspectsRatio)
    
    def findBestConfiguration(self, ratios):
        index = 0
        for config in ratios:
            if (config['group'] == 0):
                return index
            index += 1
        
        index = 0
        for config in ratios:
            if (config['solo'] == 0):
                return index
            index += 1
        
        index = 0
        fantom_best = []
        for config in ratios:
            if (config['fantom'] == 'group'):
                if (config['group'] >= config['solo']):
                    fantom_best.append(['group', config['group'], index])    
                else:
                    fantom_best.append(['solo', config['solo'], index])
            else:
                if (config['solo'] >= config['group']):
                    fantom_best.append(['solo', config['solo'], index])
                else:
                    fantom_best.append(['group', config['group'], index])
            index += 1
        return fantom_best[0][2]

    def isCharSuspect(self, char, state):
        for player in state['characters']:
            if (player['suspect'] and player['color'] == char['color']):
                return True
        return False

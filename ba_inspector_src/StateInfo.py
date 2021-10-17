class StateInfo:
    
    def getSuspectSeparation(self, state):
        playersSolo = []
        playersGroup = []
        suspectNb = 0

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
                        playersGroup.append(char)
            elif (len(playersInPos) == 1):
                if (playersInPos[0]['suspect']):
                    playersSolo.append(playersInPos)

        suspectsRatio = {
            'solo': len(playersSolo),
            'group': len(playersGroup)
        }
        return (suspectsRatio)
    
    def findBestConfiguration(self, ratios):
        index = 0
        inspector_best = []
        for config in ratios:
            inspector_best.append(config['group'] - config['solo'])
            if (inspector_best[index] < 0):
                inspector_best[index] = 0 - inspector_best[index]
            index += 1
        index = 0
        best_pos = 0
        for value in inspector_best:
            if (value < inspector_best[best_pos]):
                best_pos = index
            index += 1
        return best_pos

    def isCharSuspect(self, char, state):
        for player in state['characters']:
            if (player['suspect'] and player['color'] == char['color']):
                return True
        return False

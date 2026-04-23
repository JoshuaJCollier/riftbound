import os

def deck_converter(directory, save_name):
    with open(directory) as f:
        deck_list = f.read()
        lines = deck_list.split('\n')
        
        lines.insert(7, '\nMain Deck:')
        lines.insert(5, '\nRune Pool:')
        lines.insert(2, '\nBattlefields:')
        lines.insert(1, '\nChampion:')
        lines.insert(0, 'Legend:')

        for i, line in enumerate(lines):
            if line == 'Sideboard:':
                lines[i] = '\nSideboard:'
        
        updated_deck_list = '\n'.join(lines)

    with open(save_name, "w") as file:
        file.write(updated_deck_list)

    print(updated_deck_list)
    return updated_deck_list

#arena_to_uvs('c:/Users/josh/Downloads/', 'deck_list_tcg_arena.txt')
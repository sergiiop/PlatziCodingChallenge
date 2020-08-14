def game(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    jugando = True
    contador_player1 = 0
    contador_player2 = 0
    while jugando:
        if (player1 == 'paper' and player2 == 'rock') or (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper'):
            print('The player 1 wins the round!')
            contador_player1 += 1
        elif player1 == player2:
            print('you tied the round, please choose again')
        else:
            print('The player 1 wins the round!')
            contador_player2 += 1
        if contador_player1 == 3 or contador_player2 == 3:
            jugando = False
            break
        print('The Player 1 has '+str(contador_player1) +
              ' Points and the Player 2 has '+str(contador_player2)+' Points')
        player1 = input('Player 1 Choose another Option: ').lower()
        player2 = input('Player 2 Choose another Option: ').lower()
    if contador_player1 > contador_player2:
        print('The Player 1 ended with '+str(contador_player1) +
              ' Points and the Player 2 ended with '+str(contador_player2)+' Points')
        print('Player 1 wins the Game!')
    else:
        print('The Player 1 ended with ' + str(contador_player1) +
              ' Points and the Player 2 ended with '+str(contador_player2)+' Points')
        print('Player 2 wins the Game!')


def run():
    menu = """
    Welcome to Paper Rock Scissors

    The rules are as follows: 
    Each player must wait his turn to choose one of the three options
    - 📄  Paper 
    - 👊  Rock
    - ✂  Scissors
    The best of 3 will win
    🌟 Good Lucky 🌟
    """
    print(menu)
    player1 = input('Player 1 Choose one Option: ')
    player2 = input('Player 2 Choose one Option: ')
    game(player1, player2)


if __name__ == "__main__":
    run()

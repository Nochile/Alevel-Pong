
    #Player1(left)
    if key[pygame.K_w]:
        player_1.moveUp()
    if key[pygame.K_s]:
        player_1.moveDown()


    #Player2(right)
    if key[pygame.K_i]:
        player_2.moveUp()
    if key[pygame.K_k]:
        player_2.moveDown()

    paddle_group.draw(window)

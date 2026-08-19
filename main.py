    winner = choose_final_character(user_id)

    # ============================================================
    # SHOW FINAL WINNER
    # ============================================================

    if winner:

        bot.send_message(
            call.message.chat.id,
            f"🎉 Your final match is {winner}!\n\n"
            f"Your strongest connection is with {winner}."
        )

    else:

        bot.send_message(
            call.message.chat.id,
            "No character qualified based on the final "
            "score requirements."
        )


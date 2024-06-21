import emoji

# Dicionário de emojis disponíveis com seus códigos correspondentes
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibir lista de emojis disponíveis para o usuário
print("Emojis disponíveis:")
for emoji_char, emoji_code in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_code}")

# Solicitar uma frase ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

# Substituir as palavras-chave na frase pelos códigos de emoji correspondentes
for emoji_char, emoji_code in emojis_disponiveis.items():
    frase_codificada = frase_codificada.replace(emoji_code, emoji_char)

# Emojizar a frase usando emoji.emojize()
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Exibir a frase emojizada
print("Frase emojizada:")
print(frase_emojizada)

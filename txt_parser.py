def create_lines(text):
  for word in text.split():
    word = word.replace(',', '')
    with open("script.txt", "a") as file:
      file.write(f'{word}\n')

if __name__ == "__main__":
  text = input("Enter text: ")
  create_lines(text)

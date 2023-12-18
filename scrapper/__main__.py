
import es
import proc


def ReturnCount(url, word):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    words = CleanText(soup.text.lower())
    words = words.split()
    return words.count(word.lower())

wordCount = ReturnCount('http://example.com/', 'in')
print(wordCount) # 3

def main():
    endereco_web = es.leitor_web()
    pagina_web = proc.leitor_web(endereco_web[0])
    dados = proc.extrator(pagina_web)
    counter = proc.counter(pagina_web, endereco_web[1])
    es.saida(dados, counter)
    
if __name__ == "__main__":
    main()
    
    

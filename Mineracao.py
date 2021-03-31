import nltk

#nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsNltk = nltk.corpus.stopwords.words('portuguese')
#print((stopwordsNltk))
def removeStopWord(texto):
    frases = []
    for(frase, emocao) in texto:
        semStop = [p for p in frase.split() if p not in stopwordsNltk]
        frases.append((semStop, emocao))
    return  frases

#print(removeStopWord(base))

def aplicaStemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasesStemmer = []
    for(palavras, emocao) in texto:
        comStemmer = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsNltk]
        frasesStemmer.append((comStemmer, emocao))
    return frasesStemmer

frasesComStemmer = aplicaStemmer(base)

def buscaPalavras(frases):
    todasPalavras = []

    for(palavras, emocao) in frases:
        todasPalavras.extend(palavras)
    return todasPalavras

print(buscaPalavras(frasesComStemmer))
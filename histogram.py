davinci = '''
Properly named Leonardo di ser Piero da Vinci, Leonardo was born out of wedlock to a notary,
Piero da Vinci, and a peasant woman, Caterina, in Vinci, in the region of Florence, Italy.
Leonardo was educated in the studio of the renowned Italian painter Andrea del Verrocchio.
Much of his earlier working life was spent in the service of Ludovico il Moro in Milan,
and he later worked in Rome, Bologna and Venice. He spent his last three years in France,
where he died in 1519. Although he had no formal academic training, many historians and
scholars regard Leonardo as the prime exemplar of the "Renaissance Man" or "Universal Genius",
an individual of "unquenchable curiosity" and "feverishly inventive imagination.
" He is widely considered one of the most diversely talented individuals ever to have lived.
According to art historian Helen Gardner, the scope and depth of his interests were without
precedent in recorded history, and "his mind and personality seem to us superhuman, while the man
himself mysterious and remote." Scholars interpret his view of the world as being based in logic,
though the empirical methods he used were unorthodox for his time. Leonardo is revered for his
technological ingenuity. He conceptualized flying machines, a type of armoured fighting vehicle,
concentrated solar power, an adding machine, and the double hull. Relatively few of his designs
were constructed or even feasible during his lifetime, as the modern scientific approaches to metallurgy
and engineering were only in their infancy during the Renaissance. Some of his smaller inventions, however,
entered the world of manufacturing unheralded, such as an automated bobbin winder and a machine for testing
the tensile strength of wire. He is also sometimes credited with the inventions of the parachute, helicopter,
and tank. He made substantial discoveries in anatomy, civil engineering, geology, optics,
and hydrodynamics, but he did not publish his findings and they had little to no direct influence on
subsequent science.'''.lower()

irrelevant_words = {".", ",", " a ", " the ", " and ", " he ", " she ", " it ",
                    " is ", " but ", " at ", " to ", " was ", " can ", " ", " with ", " not ", " may ", " as ",
                    " from ", " be ", " in ", " so ", ' day ',
                    " days ", " of ", " by ", " that ", " his ", " has ", '"', " or ", " on ", " or ", " his ",
                    " also "}


def clean(data, irrelevant):
    for word in irrelevant:
        if word in data:
            data = data.replace(word, ' ')
    return data


print(clean(davinci, irrelevant_words).split())


def word_histogram(data):
    words_histogram ={}

    for word in data.split():
        if word in words_histogram:
            words_histogram[word] += 1
        else:
            words_histogram[word] = 1
    return words_histogram


print(word_histogram(davinci))


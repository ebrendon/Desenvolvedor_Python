programadores = ['Victor', 'Juliana', 'Samuel',                             # Declaração de uma lista
                 'Caio', 'Luana']  
print(type(programadores))                                                  # type é usado para obter o tipo de variável
print(len(programadores))                                                   # len é usado para obter o tamanho da lista
print(programadores)                                                        # Imprime todo o conteúdo da lista

# imprime o índice 2 da lista que equivale ao elemento 3
print(programadores[2])
print(programadores[2:])                                                    # Faz um slice exibindo a partir do índice 2 até o final
print(programadores[:2])                                                    # Faz um slice exibindo a partir do início da lista até índice 2
print(programadores[1:3])                                                   # Faz um slice exibindo a partir do índice 1 até o índice 2
                                                                            # Ou seja, o valor do índice 3 não será exibido (intervalo [1,3[)

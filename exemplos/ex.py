def swap(a, b): # Função que troca o valor de duas variáveis
  temp = a # Variável temporária que guarda o valor de a
  a = b # Atribui o valor de b a a
  b = temp # Atribui o valor de temp a b
  return a, b # Retorna os valores trocados

def acquire(lock): # Função que tenta adquirir o lock
  my_lock = True # Variável local que indica o desejo de adquirir o lock
  while my_lock: # Enquanto não conseguir o lock
    lock, my_lock = swap(lock, my_lock) # Troca o valor do lock compartilhado com o valor local
    # Se my_lock for False, significa que conseguiu o lock

def release(lock): # Função que libera o lock
  lock = False # Atribui False ao lock compartilhado, indicando que está livre

# Cria uma variável compartilhada entre as threads que indica o estado do lock
lock = False # Inicialmente, o lock está livre

# Cria duas variáveis com valores diferentes
x, y = 10, 20

print(f"x = {x}, y = {y}") # Imprime os valores originais das variáveis

acquire(lock) # Tenta adquirir o lock

x, y = swap(x, y) # Chama a função swap para trocar os valores das variáveis

release(lock) # Libera o lock

print(f"x = {x}, y = {y}") # Imprime os valores trocados das variáveis

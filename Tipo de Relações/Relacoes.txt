RELAÇÕES 

- São formados por outros objetos (nao existem ISOLADOS)
    - carro, motor
- objetos usam outros objetos 
- PO possui varios objetos que interagem entre si 
    - class produtos
    - class carrinho 
- Modelagem (DIAGRAMA DE CLASSES)    
    - define quais objetos usamos em um Programa e como elas se relacionam

RELACOES - diferente relações entre os objetos - niveis diferentes

associação (namoro)
composição (casamento)
agregação (noivado)
    - um objeto pode conter outros objetos
    - carro, motor
dependencia (ficante)
    - objetos podem usar outros objetos
    - trem, trilhos
herança 
    - uma subclasse (classe filha) e uma superclasse (classe pai)
    - leao é um animal


ASSOCIAÇÃO - namoro (ESTAVEL) - DEFINIR POR ULTIMO (em ultimo caso)

    - relacao estavel entre duas classes
    - ambas classes INDEPENDENTES
        - (EXEMPLO) um PROFESSOR esta associado a um DEPARTAMENTO, mas ambos podem existir separadamente
    - objeto de uma classe dentro de outra classe 

REPRESENTACAO (DIAGRAMA DA UML)
- representa por uma linha que liga um ao outro (reta)

AGREGAÇÃO - começando o noivado (MAIS FRACA QUE A COMPOSIÇÃO)

- objetos sao INDEPENDENTES
    - carro contem o pneu, motor, porta
        - carro nao depende total de motor e porta
            - nao deixa de ser um carro, pode ser um carro defeituoso 
- um objeto agrega o outro 

REPRESENTACAO (DIAGRAMA DA UML) 

- losangulo não preenchido
- numero fixo (especificar) ou asterico para mais de um (*) - quantidade 


COMPOSIÇÃO - casamento (FORTE) - exemplo o ex 4, sem produto nao existe carrinho de compras

- obejto pai for excluido os objetos filhos também são 
- relação de dependencia de um e do outro 
    - livro é composto por cap, se nao existe livro nao existe cap 

REPRESENTACAO (DIAGRAMA DA UML)
    - linha com losangulo preenchido na linha reta
    - conjunto de cap forma o livro, logo o losangulo fica na classe maior que o livro é composto por mais de um cap

IMPORTANTE - 
    - referencia pode ou nao ser bidirecional 
    - cap pode ou nao ter um livro
    - numero fixo (especificar) ou asterico para mais de um (*) - quantidade 



DEFINIR PELA DIFERENÇA DA FORÇA DO RELACIONAMENTO - IMPORTANTE - 


DEPENDENCIA -(MAIS FRACA) ficante
    - quando uma classe apenas usa outra de forma temporaria (parametro de um metodo)
        - para executar uma tarefa 

REPRESENTACAO (DIAGRAMA DA UML) 

- linha reta com <<usa>> no meio 
    - trem e estrada de ferro 
        - um usa o outro, mas nao se dependem para coexistir 

